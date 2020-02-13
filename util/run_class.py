import glob
import os
import H0_search
import table_to_ini
import shutil

# Find the H0 value corresponding to the table choices
H0_search.main()#os.system("python H0_search.py")
# Transform new table into ini files
table_to_ini.main()#os.system("python table_to_ini.py")

# Find all new ini files
os.chdir("../Cosmologies/")
inputs = sorted(glob.glob("*.ini"))

# This is where my class directory is
class_dir = "/home/boryanah/repos/class_public/class "
# For now use fast option -- otherwise fast = ''
fast = "_fast"

print("All inputs: ",inputs)

# For each ini file
for ini in inputs:
    root = ini[:-4]
    # If the directory exists, skip
    if os.path.isdir(root): print("Skipped and deleted "+ini); os.unlink(ini); continue
    # Otherwise, make new directory and run class in it
    os.mkdir(root)
    os.chdir(root)
    shutil.copy("../"+ini, ini)
    os.system(class_dir+ini+" ../abacus_base"+fast+".pre > "+root+".out")
    os.chdir("..")
    
    #if a TBD row (add that to maybe what is written in the ini files)
    if 'With A_s calibration' in open(ini).read():    
        os.chdir("../util/")
        os.system("python calibrate_A_s.py "+root)
        table_to_ini.main()
        os.chdir("../Cosmologies/"+root)
        shutil.copy("../"+ini, ini)
        os.system(class_dir+ini+" ../abacus_base"+fast+".pre > "+root+".out")
        os.chdir("..")
        
    # Delete the ini file (it has been moved into the directory)
    # add the sigma8 values to the final table, rename Pk and Tk, and delete obsolete files
    os.system("python ../util/write_s8.py "+root)

for f in inputs: os.unlink(f)
print("Deleted all input files")
