import glob
import os

# Find the H0 value corresponding to the table choices
os.system("python H0_search.py")
# Transform new table into ini files
os.system("python table_to_ini.py")

# Find all new ini files
os.chdir("../Cosmologies/")
inputs = glob.glob("*.ini")

# This is where my class directory is
class_dir = "/home/boryanah/repos/class_public/class "
# For now use fast option -- otherwise fast = ''
fast = "_fast"

print("All inputs: ",inputs)

# For each ini file
for ini in inputs:
    root = ini[:-4]
    # If the directory exists, skip
    if os.path.isdir(root): print("Skipped and deleted "+ini); os.remove(ini); continue
    # Otherwise, make new directory and run class in it
    os.mkdir(root)
    os.chdir(root)
    os.system("cp ../"+ini+" .")
    os.system(class_dir+ini+" ../abacus_base"+fast+".pre > "+root+".out")
    os.chdir("..")
    # Delte the ini file (it has been moved into the directory)
    os.remove(ini)
    # add the sigma8 values to the final table, rename Pk and Tk, and delete obsolete files
    os.system("python ../util/save_s8.py "+root)
