"""

This script transforms a table of cosmological parameters into ini files which can be passed
as input to the Boltzmann code CLASS.

Example
=======
>>> python table_to_ini.py --help
>>> python table_to_ini.py --table README.md

Notes
=====

The table with different parameter values should follow the following format:

                       Table
------------------------------------------------------
Comments: The first line after the comments refers to the first set of cosmological params; the second
to the next, etc.
| param1 |  param2 |  param3 |  ...  |  notes  |
| ------ |  ------ |  -----  |  ---  |  ------ | 
|val1-1  |  val1-2 |  val1-3 |  ...  |LCDM base|
|val2-1  |  val2-2 |  val2-3 |  ...  |neutriono|
|  ...   |    ...  |   ...   |  ...  |   ...   |
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
cosmo_dir = '../Cosmologies/'
simulations_table = sim_dir+'README.txt'
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
            shutil.copy(sim_dir+"abacus_example.par2",os.path.join(abacus_dir,newFile))
            # fetch the cosmology
            classParams,classFile = fetch_cosm(parDict['Cosm'])
            h = np.float(classParams['h'])
            omega_b = np.float(classParams['omega_b'])
            omega_cdm = np.float(classParams['omega_cdm'])
            omega_ncdm = np.float(classParams['omega_ncdm'])
            Omega_M = (omega_b+omega_cdm)/h**2
            Omega_M = format(Omega_M,'1.5f')
            Omega_Smooth = omega_ncdm/h**2
            Omega_Smooth = format(Omega_Smooth,'1.7f')
            N_eff = np.float(classParams['N_ur'])+np.float(classParams['N_ncdm'])
            addSeed = extract_phase(simName)
            thisSeed = Seed+addSeed
            # use file input to add value to edge of things
            # write_par
            for line in fileinput.FileInput(os.path.join(abacus_dir,newFile),inplace=1):
                if 'SimName' in line:
                    line = line.replace(line[:-1],line[:-1]+'"'+parDict['SimName']+'"')
                elif 'SimComment' in line:
                    line = line.replace(line[:-1],line[:-1]+'"'+parDict['Notes']+'"')
                elif 'BoxSize' in line:
                    line = line.replace(line[:-1],line[:-1]+parDict['Box (Mpc)'])
                elif line.startswith('NP'):
                    line = line.replace(line[:-1],line[:-1]+parDict['PPD']+'**3')
                elif 'w0' in line:
                    line = line.replace(line[:-1],line[:-1]+classParams['w0_fld'])
                elif 'wa' in line:
                    line = line.replace(line[:-1],line[:-1]+classParams['wa_fld'])
                elif 'H0' in line:
                    line = line.replace(line[:-1],line[:-1]+str(h*100))
                elif line.startswith('Omega_M'):
                    line = line.replace(line[:-1],line[:-1]+str(Omega_M))
                elif 'N_eff' in line:
                    line = line.replace(line[:-1],line[:-1]+str(N_eff))
                elif line.startswith('ns'):
                    line = line.replace(line[:-1],line[:-1]+classParams['n_s'])
                elif 'Omega_Smooth' in line:
                    line = line.replace(line[:-1],line[:-1]+str(Omega_Smooth))
                elif 'ombh2' in line:
                    line = line.replace(line[:-1],line[:-1]+str(omega_b))
                elif 'omch2' in line:
                    line = line.replace(line[:-1],line[:-1]+str(omega_cdm))
                elif 'omnuh2' in line:
                    line = line.replace(line[:-1],line[:-1]+str(omega_ncdm))
                elif 'N_eff' in line:
                    line = line.replace(line[:-1],line[:-1]+str(N_eff))
                elif 'TimeSliceRedshifts' in line:
                    line = line.replace(line[:-1],line[:-1]+str(redshifts))
                elif 'LightConeOrigins' in line:
                    line = line.replace(line[:-1],line[:-1]+str(LightConeOrigins))
                elif 'NLightCones' in line:
                    line = line.replace(line[:-1],line[:-1]+str(NLightCones))
                elif 'ZD_Pk_filename' in line:
                    line = line.replace(line[:-1],line[:-1]+'"'+classFile+'"')
                elif 'ZD_Seed' in line:
                    line = line.replace(line[:-1],line[:-1]+str(thisSeed))
                print(line,end='')    
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
