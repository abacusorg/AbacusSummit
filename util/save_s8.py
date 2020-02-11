import numpy as np
import os
import fileinput
import sys
import glob

# names: root directory in the table, abacus power spectrum and abacus transfer function
ROOT = 'root'
INPUT = 'abacus_input'
TRANSFER = 'abacus_transfer'

# strings for finding where the sigma 8 values are
sig8 = 'sigma8='
for_m = 'total matter'
for_cb = 'baryons+cdm'

# name of the table with cosmologies
# This needs to be changed to README.md
table = 'README.txt'

# root name is given as input
root = sys.argv[1]
os.chdir("../Cosmologies/")
out = os.path.join(root,root+'.out')
    
for line in open(out):
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

# add the two numbers to the end of the table
for line in fileinput.FileInput(table,inplace=1):
    if root in line:
        line = line.replace(line,line[:-1]+s8_m+' |'+s8_cb+'  | '+'\n')
    print(line,end='')

# rename the power spectrum and transfer function
os.rename(os.path.join(root,root+'.z2_tk.dat'),os.path.join(root,TRANSFER))
# if there are no neutrinos, class doesn't produce a cb power spectrum, so take the matter one
try:
    os.rename(os.path.join(root,root+'.z2_pk_cb.dat'),os.path.join(root,INPUT))
except:
    os.rename(os.path.join(root,root+'.z2_pk.dat'),os.path.join(root,INPUT))

# optionally delete all other files
#files = glob.glob(os.path.join(root,root+'*'))
#for f in files: os.remove(f)
