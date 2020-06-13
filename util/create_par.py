#!/usr/bin/env python3

"""

This script transforms a table of simulation specifications into .par2 files which can be passed
as input to the N-body simulation code Abacus.

Example
=======
>>> python create_par.py --help
>>> python create_par.py --table ../Simulations/README.md

Notes
=====

The table with different simulation parameters should follow the following format:

                       Table
------------------------------------------------------
Comments: The first line after the comments refers to the specs of the first simulation box; the second
to the next, etc.
| SimName |  PPD    |  Box (Mpc/h) |  ...  |  Notes  |
| ------  |  -----  |  -----     |  ---  |  ------ | 
| name1   |  6912   |  2000      |  ...  |LCDM base|
| name2   |  6912   |  2000      |  ...  |neutrinos|
|  ...    |  ...    |  ...       |  ...  |   ...   |
"""

import re
import sys
import argparse
import fileinput
import os
import os.path
from os.path import join as pjoin
import shutil

import numpy as np

sim_dir = '../Simulations/'
cosmo_dir = '../Cosmologies/'
cosmo_dir_for_par = '$ABACUS$/external/AbacusSummit/Cosmologies/'
simulations_table = pjoin(sim_dir,'README.md')
base = pjoin(sim_dir,'AbacusSummit_base.par2')
light_dict = {
    'def': [3, '(-990.,-990.,-990.), (-990., -990., -2990.), (-990., -2990., -990.)'],
    'box': [1, '(0.,0.,0.)'],
    'none': [0, '(-990.,-990.,-990.), (-990., -990., -2990.), (-990., -2990., -990.)']
    }
z_dict = {
    'Full': '[3.0, 2.5, 2.0, 1.7, 1.4, 1.1, 0.8, 0.5, 0.4, 0.3, 0.2, 0.1]',
    'Full to 0.8': '[3.0, 2.5, 2.0, 1.7, 1.4, 1.1, 0.8]',
    'Partial': '[2.5, 1.4, 0.8, 0.2]',
    'Partial+HiZ': '[3.0, 2.0, 2.5, 1.4, 0.8, 0.2]',
    'none':'None'
    }

CPD_dict = {'6912': '1701',
            '3456': '825',
            '6300': '1701',
            '2304': '455',
            '4096': '945',
            '10000': '1911',
            '8640': '1701',
            '1728': '405',
            }
ZD_NumBlock_dict = {'6912': '384',
            '3456': '72',
            '6300': '350',
            '2304': '48',
            '4096': '128',
            '10000' : '1250',
            '8640': '864',
            '1728': '4',
            }
GroupRadius_dict = {
            '6912': '10',
            '2304': '10',
            '3456': '8',
            '6300': '15',
            '4096': '5',
            '10000': '3',
            '8640': '3',
            '1728': '10',
            }

mpirun_cmd_dict = {'3456':"jsrun -nALL_HOSTS -cALL_CPUS -a1 -r1 -gALL_GPUS -b rs",
                   '6300':"jsrun -nALL_HOSTS -cALL_CPUS -a1 -r1 -gALL_GPUS -b rs",
                   '4096':"jsrun -nALL_HOSTS -cALL_CPUS -a1 -r1 -gALL_GPUS -b rs",
                    }

extra_dict = {'10000': {'OutputFullLightCones': '1'},
               '8640': {'OutputFullLightCones': '1'}}

parallel_dict = {'1728': '0'}

small_dict = {'1728': 'SmallBox'}

Seed = 12321

def main(table):
    # parameter names and row where they can be found
    paramNames, namesRow = list_param_names(table)
    # Create a numpy array with all entries in the table and names taken from it
    read_table(paramNames,table,namesRow)

    return 0
    
def list_param_names(fn,output_s8=False):
    # count total number of commented rows
    parRow = 0
    for line in open(fn):
        # if this is the start of the table, exit and parse the parameter names
        if line[:1] == '|':
            paramLine = line
            break
        parRow += 1
    else:
        print("Error: the table should have a line '| par1 | par2 | par3' at the beginning to extract column names!")
        exit(1)
    
    # Assuming that the first line in the table has the parameter names
    paramLine = re.sub(r'^\|\s*', '', paramLine)
    paramLine = re.sub(r'\s*\|\s*$', '', paramLine)
    paramNames = re.split(r'\s*\|\s*',paramLine)
    
    return paramNames, parRow

def read_table(paramNames,fn,namesRow):
    # for parameter name row and the horizontal line row
    extraRows = 2
    # This is where the sim numbers start
    startRow = namesRow + extraRows # since next row is |---|...|---|
    # number of parameters and cosmologies
    numParams = len(paramNames)

    for i,line in enumerate(open(fn)):
        if i < startRow or line[:1] != '|': continue
        # separating the individual row entries in 'line'
        line = re.sub(r'^\|\s*', '', line)
        line = re.sub(r'\s*\|\s*$', '', line)
        line = re.split(r'\s*\|\s*',line)
        parDict = {}
        for p,parName in enumerate(paramNames):
            parDict[parName] = line[p]
        # read the lightcone
        NLightCones, LightConeOrigins = extract_light(parDict['Notes'])
        # checking how many in simname
        simNames = extract_names(parDict['SimName'])
        redshifts = extract_zs(parDict['Full Outputs'])
        # for each copy par2 into a new file with name given by sim
        for simName in simNames:
            # fetch the cosmology
            cosm_num = extract_cosm(simName)
            classParams,classFile = fetch_cosm(cosm_num)
            h = np.float(classParams['h'])
            omega_b = np.float(classParams['omega_b'])
            omega_cdm = np.float(classParams['omega_cdm'])
            omega_ncdm = np.atleast_1d(classParams['omega_ncdm']).astype(float)
            Omega_M = (omega_b+omega_cdm+omega_ncdm.sum())/h**2
            Omega_M = f'{Omega_M:f}'  # 7.5f  # any reason to limit sig figs? Probably prefer not to
            Omega_Smooth = omega_ncdm.sum()/h**2
            if len(omega_ncdm) == 1:
                omega_ncdm = omega_ncdm[0]
            Omega_Smooth = f'{Omega_Smooth:f}'  #9.7f
            phase_info = extract_phase(simName)
            thisSeed = Seed + phase_info.pop('add_seed')
            # use file input to add value to edge of things
            # write_par

            newparams = {        'SimComment': '"'+parDict['Notes']+'"\n',
                                    'BoxSize': parDict['Box (Mpc/h)'],
                              'FinalRedshift': parDict['z_Final'],
                                         'NP': parDict['PPD']+'**3',
                                        'CPD': CPD_dict[parDict['PPD']],
                                'GroupRadius': GroupRadius_dict[parDict['PPD']],
                                         'w0': classParams['w0_fld'],
                                         'wa': classParams['wa_fld'],
                                         'H0': str(h*100),
                                    'Omega_M': str(Omega_M),
                               'Omega_Smooth': str(Omega_Smooth) + '\n',
                         'TimeSliceRedshifts': str(redshifts),
                           'LightConeOrigins': str(LightConeOrigins),
                                'NLightCones': str(NLightCones) + '\n',
                             'ZD_Pk_filename': f'"{classFile}"',
                                    'ZD_Seed': str(thisSeed),
                                'ZD_NumBlock': ZD_NumBlock_dict[parDict['PPD']]  + '\n',
                                       'N_ur': classParams['N_ur'],
                                     'N_ncdm': classParams['N_ncdm'],
                                        'n_s': classParams['n_s'],
                                    'omega_b': str(omega_b),
                                  'omega_cdm': str(omega_cdm),
                                 'omega_ncdm': str(omega_ncdm) + '\n',
                         }

            if parDict['PPD'] in mpirun_cmd_dict:
                newparams['mpirun_cmd'] = mpirun_cmd_dict[parDict['PPD']]

            if parDict['PPD'] in extra_dict:
                newparams.update(extra_dict[parDict['PPD']])

            if parDict['PPD'] in parallel_dict:
                newparams['Parallel'] = parallel_dict[parDict['PPD']]
                
            if parDict['PPD'] in small_dict:
                simName_dir = pjoin(small_dict[parDict['PPD']],simName)
                include_str = "../../AbacusSummit_base.par2"
            else:
                simName_dir = simName.encode().decode()
                include_str = "../AbacusSummit_base.par2"
                
            newparams.update(phase_info)

            os.makedirs(pjoin(sim_dir, simName_dir), exist_ok=True)

            # Differences - individual file for each sim
            with open(pjoin(sim_dir, simName_dir, 'abacus.par2'), 'w') as f:
                # Start the file with the SimName and the #include of the base
                f.write(f'SimName = "{simName}"\n')
                f.write(f'#include "{include_str}"\n\n')
                # Now write all the sim-specific params
                for key,value in newparams.items():
                    f.write(f'{key} = {value}\n')

def extract_light(notes):
    if 'no lightcone' in notes:
        n_light, pos = light_dict['none']
    elif 'box-centered lightcone' in notes:
        n_light, pos = light_dict['box']
    else: n_light, pos = light_dict['def']
    return n_light, pos
    
def extract_zs(output):
    try:
        return z_dict[output]
    except:
        return '['+output+']'
    
def extract_phase(sim):
    ret = {}
    ret['add_seed'] = int((re.findall(r"ph\d{3}",sim)[0]).split('ph')[-1])*100

    # Set param for fixed amplitude sims
    if 'fixed' in sim:
        ret['ZD_qPk_fix_to_mean'] = '1'

    # Special case: phase 98 is phase 99, inverted
    if ret['add_seed'] == 98*100:
        ret['add_seed'] = 99*100
        ret['FlipZelDisp'] = '1'
    return ret

def extract_cosm(sim):
    return int(re.search(r"c(\d{3})",sim).group(1))
    
def extract_names(sim):
    match = r"\{(.*?)\}"
    try:
        endpoints = re.search(match, sim).group(1).split('-')
    except:
        return [sim]
    nums = range(int(endpoints[0]), int(endpoints[1])+1)
    names = [re.sub(match,format(i,"03d"),sim) for i in nums]
    return names

def fetch_cosm(cosm):
    cosmName = f'abacus_cosm{cosm:03d}/'
    fn = pjoin(cosmo_dir,cosmName+'CLASS.ini')

    # Parse parameters from file
    param_dict = {}
    for line in open(fn):
        # if line empty or commented out, skip
        if line[0] == '#' or line == '\n': continue
        # make sure that things are split name = val1, val2, val3, ... into LHS and RHS
        sp = re.split(r'\s*=\s*', line)
        # We should have 2 things = LHS and RHS or 1 thing if RHS is empty after '='
        assert len(sp) <= 2, \
            "This file cannot be parsed correctly, see the example .ini files"
        # separating into parameter name and value
        n = sp[0]; v = sp[-1]
        if '#' in v: # remove commented out sections
            v = v[:v.find('#')]
        if v == '': continue # remove empty value lines
        v = re.sub('\n','',v)

        if ',' in v:
            v = v.split(',')  # split comma separated lists

        param_dict[n] = v

    return param_dict, pjoin(cosmo_dir_for_par,cosmName+'CLASS_power')
    
    
class ArgParseFormatter(argparse.RawDescriptionHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=ArgParseFormatter)
    parser.add_argument('--table', help='table name to read from', default=simulations_table)
    args = parser.parse_args()
    args = vars(args)
    exit(main(**args))
