import numpy as np
import os
import re
import fileinput
import sys
import glob
from table_to_ini import  list_param_names

# names: root directory in the table, abacus power spectrum and abacus transfer function
ROOT = 'root'

# strings for finding where the sigma 8 values are
sig8 = 'sigma8='
h = 'h'
s8_cal = 'sigma8_cb'
As = 'A_s'
for_m = 'total matter'
for_cb = 'baryons+cdm'

# name of the table with cosmologies
# This needs to be changed to README.md
table = 'README.txt'

# root name is given as input
root = sys.argv[1] # give it abacus_cosm001
root_base = 'abacus_cosm000'
os.chdir('../Cosmologies/')
output = os.path.join(root,root+'.out')

def get_A_s(As_i,s8_i,s8_f):
    As_f = As_i*(s8_f/s8_i)**2
    return As_f

def construct_dict(root_name,fn,output_s8=False):
    # parameter names and row where they can be found
    param_names, names_row = list_param_names(fn,output_s8)
    par_dict = {}
 
    for line in (open(fn)):
        
        if root_name in line:
            # separating the individual param values in the line
            line = re.sub('^\|\s*', '', line)
            line = re.sub('\s*\|\s*$', '', line)
            line = re.split('\s*\|\s*',line)
            for p, param in enumerate(param_names):
                if 'TBD' in line[p] and param == h: print("You should first fill in h"); exit()
                else: par_dict[param] = line[p];
    return par_dict

    
for line in open(output):
    # look for the sigma8 values for total matter and CDM+baryons
    if sig8 in line and for_m in line:
        line = line.split(sig8)
        line = line[-1].split(' ')
        # take value after equal sign
        s8_m = np.float(line[0]) 
        s8_m = format(s8_m,'8.6f')

    elif sig8 in line and for_cb in line:
        line = line.split(sig8)
        line = line[-1].split(' ')
        # take value after equal sign
        s8_cb = np.float(line[0]) 
        s8_cb = format(s8_cb,'9.6f')

param_dict_base = construct_dict(root_base,table,output_s8=True)
param_dict = construct_dict(root,table)

# add the two numbers to the end of the table
for line in fileinput.FileInput(table,inplace=1):
    if root in line:
        # if A_s is not specified, steal s8_base from the baseline, find real A_s
        A_s_ini = np.float(param_dict[As])
        s8_base = np.float(param_dict_base[s8_cal])
        A_s = get_A_s(A_s_ini,np.float(s8_cb),s8_base)
        # plug into table
        A_s = format(A_s,'11.4e')
        line = line.replace(param_dict[As],A_s)
    print(line,end='')
