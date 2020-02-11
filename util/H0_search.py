"""
This program does a bisection search in the parameter space of the Hubble parameter (h)
between h = 0.6 and h = 0.8 with a 6-figure precision in an effort to match the value 
of the parameter 100*theta_s in the target cosmology. If not using the table option, the 
script produces:  <root>.ini and <root>.parameters.ini (<root> is specified in input (see
below). The first file (<root>.ini) contains only the NEW parameters together with h, 
whereas the <root>.parameters.ini file has the full of set of cosmological parameters,
i.e. BASE and NEW. The current default BASE is 'abacus_base_fast.pre' which produces a
fast CLASS output. If one hands the script a table, then it produces a new table called 
README.md in the 'Cosmologies' directory with the h values overwritten and all others 
kept as in the original table.

The target cosmology is selected with the option --target TARGET, which expects a
file of type .ini with full information about all parameters. It is only needed
in order to select a target value of the 100*theta_s parameter to be matched by
the BASE + NEW cosmology. The default is 'abacus_base_full.ini', which assumes
the case of one massive neutrino species with a mass of 60 meV, and has a corresponding
value of 100*theta_s of 1.041533. It also uses the faster settings of CLASS.

Usage
=====
# There are three ways to pass a --new cosmology to this script,
# which can be seen by running the command
>>> python H0_search.py --help

# ini-file format
>>> python H0_search.py --new ini-file abacus_cosm020.ini

# comm-line format
>>> python H0_search.py --new comm-line 'omega_cdm 0.12 omega_b 0.02 root test_0'

# table format
>>> python H0_search.py --new table ../Cosmologies/emulator_grid

# In addition, one can change the target file
>>> python H0_search.py --target 'abacus_cosm010.parameters.ini' --new ini-file abacus_cosm020.ini

# Or the base file
>>> python H0_search.py --base 'abacus_cosm010.parameters.ini' --new ini-file abacus_cosm020.ini

Notes
=====

There are three different types of input (NEW) one can pass to this program: table, ini-file
or command-line argument. The recommended settings are the default ones with an input
of table such as emulator_table.

* The ini file produces a <root>.parameters.ini and a <root>.ini file in a new directory and
should follow the same format as the BASE and TARGET files format, e.g.

                 ini-file
-------------------------------------------
omega_cdm = 0.12
omega_ncdm = 0.00004
omega_b = 0.02
...

* The command line produces a <root>.parameters.ini and a <root>.ini file in a new directory and
should follow the format of:

                      comm-line 
-----------------------------------------------------
'param1 param1val param2 param2val ... root name_set'

* The option of passing a table uses the same format as the script table_to_ini.py and
allows the user to run several different cosmologies serially. It makes a copy of the
table stored in the 'Cosmologies/' directory with the newly computed H0 values.
Here is the table format:

                       Table
------------------------------------------------------
Comments: The first row after the comments and parameter names refers to the first set
of cosmological params; the second to the next, etc.
| param1 |  param2 |  param3 |  ...  |  notes  |
| ------ |  ------ |  -----  |  ---  |  ------ | 
|val1-1  |  val1-2 |  val1-3 |  ...  |LCDM base|
|val2-1  |  val2-2 |  val2-3 |  ...  |neutriono|
|  ...   |    ...  |   ...   |  ...  |   ...   |
"""

import os
import fileinput
import argparse
import numpy as np
from classy import Class
import re
from table_to_ini import  list_param_names, read_table

cosmo_dir = '../Cosmologies/'
emulator_table = cosmo_dir+'emulator_grid'
cosmology_table = cosmo_dir+'README.txt'
commentedParam = ['notes']
rootName = 'root'
HubbleParam = 'h'
OmegaNu = 'omega_ncdm'

def read_file(fn):
    # Parse parameters from file
    names = []
    vals = []
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
        vals.append(v)
        names.append(n)
        param_dict = {names[i]:vals[i] for i in range(len(vals))}
    try: # if no neutrinos, classy doesn't like being passed omega_ncdm
        if np.float(param_dict[OmegaNu]) == 0.0: del param_dict[OmegaNu]
    except:
        pass
    return param_dict

def modify_table(table,root,h_old,h):
    for line in fileinput.FileInput(table,inplace=1):
        # look for a line which has the root name in it
        if root in line:
            # automize precision TODO: B.H.
            # find where the old value is recorded
            h_old = format(h_old,'6.4f')
            # take the new one in the right format
            h = format(h,'6.4f')
            # substitute new for old
            line = line.replace(h_old,h)
            # this is to make sure no new lines are inserted
            print(line,end='')
        # copy the rest of the lines
        else: print(line,end='')
            
def read_input(arg):
    # Which of three input formats did the user choose
    if arg[0] == 'ini-file':
        # Read ini file
        Params = read_file(arg[1])
        numCosm = 1
    elif arg[0] == 'comm-line':
        # Read command line
        line = arg[1]
        # split the line into ['name1','val1','name2','val2',...]
        sp = np.array(line.split())
        # splitting so that even contain paramNames and odd paramVals
        args = np.arange(len(sp),dtype=int)
        names = sp[args%2==0] 
        vals = sp[args%2==1] 
        assert len(sp) > 0 and len(sp)%2 == 0, \
            "The expected format is 'paramNam1 paramVal1 paramNam2 paramVal2 ...'"
        assert rootName in names, "One needs to pass rootName name in the command line, too"
        Params = {names[i]:vals[i] for i in range(len(vals))}
        numCosm = 1
    elif arg[0] == 'table':
        # Read table
        table = arg[1]
        # parameter names and row where they can be found
        paramNames, namesRow = list_param_names(table)
        # Create a numpy array with all entries in the table and names taken from it
        Params, numCosm = read_table(paramNames,table,namesRow)
    return Params, numCosm

def read_line(params,iCosm):
    # Read this line and fill out the parameter dictionary for it
    param_dict = {}
    # loop over all parameters
    for p,parName in enumerate(params.dtype.names):
        # if no neutrinos, classy doesn't like being passed omega_ncdm
        if parName == OmegaNu and params[parName][iCosm] == 0.: continue
        # skip the notes parameters since class won't recognize
        if parName in commentedParam: continue 
        param_dict[parName] = params[parName][iCosm]
    return param_dict

def write_dict_to_ini(param_dict,h):
    # record the shortcut file (the full (.parameters.ini) file is automatically recorded)
    param_dict[HubbleParam] = h
    wfn = param_dict[rootName]+'ini'
    # record all cosmologies as separate files
    with open(wfn, 'w') as f:
        for parName in param_dict.keys():
            # write the notes as a comment at the end of the file
            if parName in commentedParam: line = '#'+ ' '+str(param_dict[parName])+'\n'
            # write all the other parameter values
            else: line = parName+' = '+str(param_dict[parName])+'\n'
            f.write(line)
            
    
def main(target,base,new):
    # create instance of the class "Class"
    TargetCosmo = Class()

    # pass input parameters
    print("The default cosmology is read from "+target)
    target_param_dict = read_file(target)
    TargetCosmo.set(target_param_dict)

    # run class
    TargetCosmo.compute()
    os.remove(target_param_dict[rootName]+"parameters.ini")
    os.remove(target_param_dict[rootName]+"unused_parameters")
    theta_target = TargetCosmo.theta_s_100()
    print("Target 100*theta_s = ",theta_target)

    # The second (new) cosmology
    print("The new cosmology is read from "+base+" and "+new[1])
    base_param_dict = read_file(base)

    # Create a new table with the final cosmologies
    if new[0] == 'table':
        os.system("cp "+new[1]+" "+cosmology_table)
    
    new_params, numCosm = read_input(new)
    # for each new cosmology
    for iCosm in range(numCosm):
        NewCosmo = Class()
        # Load the base parameter values
        NewCosmo.set(base_param_dict)
        # Create a dictionary
        new_param_dict = read_line(new_params,iCosm) if new[0] == 'table' else new_params
        if new_param_dict[rootName][-1:] != '.' : new_param_dict[rootName] += '.'
        # create new directory with the root name unless it exists already
        dir_par = new_param_dict[rootName][:-1]
        if os.path.isdir(dir_par) != True: os.mkdir(dir_par)
        os.chdir(dir_par)
        NewCosmo.set(new_param_dict)
        
        # run class
        NewCosmo.compute()
        h_old = NewCosmo.h()
        h = search(NewCosmo,theta_target)
        write_dict_to_ini(new_param_dict,h)        
        os.chdir('..')

        # if running in table regime, modify the README table and delete everything else
        if new[0] == 'table':
            # Get rid of the evidence
            os.system("rm -r "+dir_par)
            # modify the H column in the final table
            modify_table(cosmology_table,new_param_dict[rootName][:-1],h_old,h)

def search(NewCosmo,theta_def):
    # array of hubble parameter values to search through
    hs = np.arange(600000,800000)/1000000.
    N_h = len(hs)
    
    # allowed tolerance b/n the new theta and the def
    this_theta = NewCosmo.theta_s_100()
    print("New 100*theta_s = ",this_theta)
    tol_t = 1.e-6


    iterations = 0
    left = 0 # Determines the starting index of the list we have to search in
    right = N_h-1 # Determines the last index of the list we have to search in
    mid = (right + left)//2

    while(np.abs(this_theta-theta_def)>tol_t): # If this is not our search element
        # If the current middle element is less than x then move the left next to mid
        # Else we move right next to mid
        NewCosmo.set({HubbleParam:hs[mid]}) # .6736
        NewCosmo.compute()
        print("iter, h = ",iterations,", ",hs[mid])
        this_theta = NewCosmo.theta_s_100()
        if  this_theta < theta_def:
            left = mid + 1
        else:
            right = mid - 1
        mid = (right + left)//2
        iterations += 1
        print('Delta(100*theta_s) = ',np.abs(this_theta-theta_def))
        if right-left == 1: break

    # Final output
    print('iterations = ',str(iterations))
    print('h = ',NewCosmo.h())
    print('100*theta_s = ',NewCosmo.theta_s_100())
    print('Delta(100*theta_s) = ',np.abs(NewCosmo.theta_s_100()-theta_def))
    return NewCosmo.h()

# For the parser
class ArgParseFormatter(argparse.RawDescriptionHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=ArgParseFormatter)
    parser.add_argument('--target', help='file defining the target-theta cosmology', default='abacus_base_full.ini')
    parser.add_argument('--base', help='file defining the base cosmology params', default='abacus_bisection_fast.pre')
    parser.add_argument('--new', help='format of the new cosmology params (comm-line,table,ini-file) and file name', nargs=2,default=['table',emulator_table])
    
    args = parser.parse_args()
    args = vars(args)

    assert args['new'][0] in ['ini-file','comm-line','table'], "The first argument for 'new' should be one of comm-line, table, or ini-file"
    exit(main(**args))
