#!/usr/bin/env python3
'''
This is a slightly modified version of NERSC's
`generate_sorted_list_for_hpss.py` script that divides the final sorted list
into N separate lists, appropriate for parallel submission to HPSS.
Each list may contain files on multiple tapes, but a given tape will never
be divided across multiple files.  For this reason, there may be empty
files if there are more lists requested than tapes.
'''

import tempfile, shlex, os, pathlib, argparse
from subprocess import Popen, PIPE, STDOUT

def hpss_sort(infiles, nlist=1):
    #Make a tempfile to hold commands for HPSS (HPSS requires it to be given as a file)
    (fd, filename) = tempfile.mkstemp()
    hsi_list=open(filename,"a")

    hsi_list_string = "ls -NP "
    data = []
    with open(infiles) as f:
        for line in f:
            hsi_list.write(hsi_list_string+"\'"+line.strip('\n')+"\'\n")
    hsi_list.close()

    #Get list of tape position from HPSS
    cmd = "hsi -P in "+filename
    cmd = shlex.split(cmd)
    q = Popen(cmd, shell=False,  stdout=PIPE, stderr=PIPE, bufsize = 1, universal_newlines = True)
    output,error = q.communicate()
    if error:
        #do nothing, but you might want some error handling in the future, tough because HPSS lumps all output together
        rerror = 1
        print("Error accessing HPSS", error)


    #Sort this list by tape order
    #typically this line looks like "FILE    /home/l/lgerhard/159240_test.tar        2465280 2465280 111+1121698225  EG010100        4       0       1       11/06/2013    08:47:20 02/24/2017      13:01:15"
    #we care about filename, EG0101, 111, 1121698225 (111 is the tape mark, 1121698225 is how many bytes past the mark the file starts)
    #however, some file names can have spaces in them. There's no way to format the output from HPSS, so have to work backwards for these cases
    sorted_list = []
    for line in output.split('\n'):
        if "FILE" not in line:
            continue
        sline = line.split("\t")
        #To handle case where file name has spaces, read tape name and pos from back instead
        tape_string = sline[-8]
        tape_pos = sline[-9]
        i = 0
        tape_filename = ""
        expect_len = 13
        while(i < len(sline) - 12):
            tape_filename = tape_filename + sline[1+i]
            i = i + 1
            #this next bit is to avoid a trailing space
            if i < len(sline) - 12:
                tape_filename = tape_filename + "\ "

        if len(tape_string) < 3:
            tape = "0"
        else:
            tape = tape_string[:-2]
        if "+" in tape_pos:
            ssline = tape_pos.split('+')
            tapenum = ssline[0]
            tapeoff = ssline[1]
        else:
            tapenum = "0"
            tapeoff = "0"
        hpath = tape_filename
        sorted_list.append([tape,int(tapenum),int(tapeoff),hpath])

    sorted_list.sort()

    all_lists = divide_into_nlists(sorted_list, nlist)

    return all_lists


def divide_into_nlists(sorted_list, nlist=1):
    tapes = {}  # {tape:[fns]}
    for t,*_,fn in sorted_list:
        tapes[t] = tapes.get(t,[]) + [fn]
    
    target_size = len(sorted_list) // nlist
    all_lists = [[]]
    for tape in tapes:
        if len(all_lists[-1]) > target_size:
            all_lists += [[]]
        all_lists[-1] += tapes[tape]

    assert sum(len(l) for l in all_lists) == len(sorted_list)
    assert len(all_lists) <= nlist

    return all_lists


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HPSS file sorter and retriever')
    parser.add_argument('-i','--infile',help='file with list of file to extract from HPSS',required=True,dest='infile',type=str)
    parser.add_argument('-n','--nlist',help='Number of output files to write', type=int, default=1)

    args = parser.parse_args()
    infile = args.infile
    nlist = args.nlist
    
    print("Generating sorted list from input file")
    all_lists = hpss_sort(infile, nlist=nlist)
    for i,l in enumerate(all_lists):
        with open(infile + f'_sorted_{i:03d}.txt', 'w') as fp:
            fp.writelines(ll + '\n' for ll in l)
