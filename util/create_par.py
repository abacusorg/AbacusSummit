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
| SimName |  PPD    |  Box (Mpc) |  ...  |  Notes  |
| ------  |  -----  |  -----     |  ---  |  ------ | 
| name1   |  6912   |  2000      |  ...  |LCDM base|
| name2   |  6912   |  2000      |  ...  |neutrinos|
|  ...    |  ...    |  ...       |  ...  |   ...   |
"""
import numpy as np
import re
import sys
import argparse
import fileinput
import os
import shutil

sim_dir = '../Simulations/'
abacus_dir = os.path.join(sim_dir,'abacus_par/')
abacus_short_dir = os.path.join(sim_dir,'abacus_short_par/')
cosmo_dir = '../Cosmologies/'
simulations_table = os.path.join(sim_dir,'README.txt')
base = os.path.join(sim_dir,'AbacusSummit_base.par2')
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
    'none':'[]'
    }
Seed = 12321
MANTRA = '#include "../AbacusSummit_base.par2"\n\n'

def main(table):
    # parameter names and row where they can be found
    paramNames, namesRow = list_param_names(table)
    # Create a numpy array with all entries in the table and names taken from it
    read_table(paramNames,table,namesRow)
    
def list_param_names(fn,output_s8=False):
    # count total number of commented rows
    parRow = 0
    for line in open(fn):
        # if this is the start of the table, exit and parse the parameter names
        if line[:1] == '|':
            paramLine = line
            break
        parRow += 1
    # Assuming that the first line in the table has the parameter names
    try:
        paramLine
    except NameError:
        print("The table should have a line '| par1 | par2 | par3' at the beginning to extract column names!"); exit()
    paramLine = re.sub('^\|\s*', '', paramLine)
    paramLine = re.sub('\s*\|\s*$', '', paramLine)
    paramNames = re.split('\s*\|\s*',paramLine)
    
    return paramNames, parRow

def read_table(paramNames,fn,namesRow):
    # for parameter name row and the horizontal line row
    extraRows = 2
    # This is where the sim numbers start
    startRow = namesRow + extraRows # since next row is |---|...|---|
    # number of parameters and cosmologies
    numParams = len(paramNames)

    if not os.path.exists(abacus_dir): os.mkdir(abacus_dir)
    if not os.path.exists(abacus_short_dir): os.mkdir(abacus_short_dir)

    for i,line in enumerate(open(fn)):
        if i < startRow or line[:1] != '|': continue
        # separating the individual row entries in 'line'
        line = re.sub('^\|\s*', '', line)
        line = re.sub('\s*\|\s*$', '', line)
        line = re.split('\s*\|\s*',line)
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
            newFile = simName+'.par2'
            shutil.copy(os.path.join(sim_dir,"abacus_example.par2"),os.path.join(abacus_dir,newFile))
            # fetch the cosmology
            classParams,classFile = fetch_cosm(parDict['Cosm'])
            h = np.float(classParams['h'])
            omega_b = np.float(classParams['omega_b'])
            omega_cdm = np.float(classParams['omega_cdm'])
            omega_ncdm = np.float(classParams['omega_ncdm'])
            Omega_M = (omega_b+omega_cdm)/h**2
            Omega_M = format(Omega_M,'7.5f')
            Omega_Smooth = omega_ncdm/h**2
            Omega_Smooth = format(Omega_Smooth,'9.7f')
            N_eff = np.float(classParams['N_ur'])+np.float(classParams['N_ncdm'])
            addSeed = extract_phase(simName)
            thisSeed = Seed+addSeed
            # use file input to add value to edge of things
            # write_par
            for line in fileinput.FileInput(os.path.join(abacus_dir,newFile),inplace=1):
                if line.startswith('SimName'):
                    line = line.replace(line[:-1],line[:-1]+'"'+simName+'"')
                elif line.startswith('SimComment'):
                    line = line.replace(line[:-1],line[:-1]+'"'+parDict['Notes']+'"')
                elif line.startswith('BoxSize'):
                    line = line.replace(line[:-1],line[:-1]+parDict['Box (Mpc)'])
                elif line.startswith('NP'):
                    line = line.replace(line[:-1],line[:-1]+parDict['PPD']+'**3')
                elif line.startswith('w0'):
                    line = line.replace(line[:-1],line[:-1]+classParams['w0_fld'])
                elif line.startswith('wa'):
                    line = line.replace(line[:-1],line[:-1]+classParams['wa_fld'])
                elif line.startswith('H0'):
                    line = line.replace(line[:-1],line[:-1]+str(h*100))
                elif line.startswith('Omega_M'):
                    line = line.replace(line[:-1],line[:-1]+str(Omega_M))
                elif line.startswith('N_eff'):
                    line = line.replace(line[:-1],line[:-1]+str(N_eff))
                elif line.startswith('ns'):
                    line = line.replace(line[:-1],line[:-1]+classParams['n_s'])
                elif line.startswith('Omega_Smooth'):
                    line = line.replace(line[:-1],line[:-1]+str(Omega_Smooth))
                elif line.startswith('ombh2'):
                    line = line.replace(line[:-1],line[:-1]+str(omega_b))
                elif line.startswith('omch2'):
                    line = line.replace(line[:-1],line[:-1]+str(omega_cdm))
                elif line.startswith('omnuh2'):
                    line = line.replace(line[:-1],line[:-1]+str(omega_ncdm))
                elif line.startswith('TimeSliceRedshifts '):
                    line = line.replace(line[:-1],line[:-1]+str(redshifts))
                elif line.startswith('LightConeOrigins'):
                    line = line.replace(line[:-1],line[:-1]+str(LightConeOrigins))
                elif line.startswith('NLightCones'):
                    line = line.replace(line[:-1],line[:-1]+str(NLightCones))
                elif line.startswith('ZD_Pk_filename'):
                    line = line.replace(line[:-1],line[:-1]+'"'+classFile+'"')
                elif line.startswith('ZD_Seed'):
                    line = line.replace(line[:-1],line[:-1]+str(thisSeed))
                print(line,end='')
            # take what's different for each sim and save in new file
            with open(os.path.join(abacus_dir,newFile)) as f1, open(os.path.join(sim_dir,"abacus_example.par2")) as f2:
                l1 = list(f1)
                l2 = list(f2)

            # Differences - individual file for each sim
            with open(os.path.join(abacus_short_dir,newFile),'w') as f:
                fout = sorted(set(l1) - set(l2), key = l1.index)
                for line in fout:
                    f.write(line)
                    if line.startswith('SimName'): f.write(MANTRA)

            # Similarities - base file for all sims
            if os.path.isfile(base): continue
            with open(base,'w') as f:
                fout = sorted(set(l1) & set(l2), key = l1.index)
                f.writelines(fout)
    return

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
    return int((re.findall(r"ph\d\d\d",sim)[0]).split('ph')[-1])*100
    
def extract_names(sim):
    match = "\{(.*?)\}"
    try:
        rang = re.search(match, sim).groups()[0]
    except:
        return [sim]
    nums = np.arange(int(rang.split('-')[0]),int(rang.split('-')[-1])+1)
    names = [re.sub(match,format(nums[i],"03d"),sim) for i in range(len(nums))]
    return names

def fetch_cosm(cosm):
    cosmName = 'abacus_cosm'+cosm+'/'
    fn = os.path.join(cosmo_dir,cosmName+'CLASS.ini')

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
        param_dict[n] = v

    return param_dict, fn
    
    
class ArgParseFormatter(argparse.RawDescriptionHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=ArgParseFormatter)
    parser.add_argument('--table', help='table name to read from', default=simulations_table)
    args = parser.parse_args()
    args = vars(args)
    exit(main(**args))
