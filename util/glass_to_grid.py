import numpy as np
import fileinput

#num   sigma8m    ochh      ns     obhh      w0      wa     Nur     nrun

array = np.loadtxt("emulator_glass.dat")

cosmo = array[:,0].astype(int)
select = cosmo >= 16
cosmo = cosmo[select]
n_cosmos = np.sum(select)


sigma8_cb = array[select,1]
omch2 = array[select,2]
n_s = array[select,3]
ombh2 = array[select,4]
w0 = array[select,5]
wa = array[select,6]
N_ur = array[select,7]
n_run = array[select,8]

rootFormat = '03d'
ombFormat = '1.5f'
omcFormat = '1.4f'
HubbleTBD = 'TBD   '
AsTBD = ' 2.TBD e-9 '
nsFormat = '1.4f'
alphasFormat = '2.3f'
NurFormat = '1.4f'
w0Format = '2.3f'
waFormat = '2.3f'

table = "emulator_grid"
root_first = 'abacus_cosm115'

line_first = '| abacus_cosm115     | Baseline -0.3 nnu, -3.3% ln(omega_c), -0.01 n_s                      | 0.02237 |  0.1161   | TBD    | 2.TBD e-9 | 0.9549 | 0.000   | 1.7328 | 1      | 0.00064420 | -1.0   | 0.0    | \n'

for line in fileinput.FileInput(table,inplace=1):
    # look for a line which has the root name in it
    if root_first in line:
        assert line == line_first, "Make sure you have copied it right: \n"+line+"\n"+line_first
        print(line,end='')
        
        for i in range(n_cosmos):
            line = line_first
            # take the new one in the right format
            line = line.replace('Baseline -0.3 nnu, -3.3% ln(omega_c), -0.01 n_s','Emulator grid around baseline cosmology        ')
            cosm = format(cosmo[i],rootFormat)
            line = line.replace('115',cosm)
            omb = format(ombh2[i],ombFormat)
            line = line.replace('0.02237',omb)
            omc = format(omch2[i],omcFormat)
            line = line.replace('0.1161',omc)
            ns = format(n_s[i],nsFormat)
            line = line.replace('0.9549',ns)
            alpha_s = format(n_run[i],alphasFormat)
            line = line.replace('0.000',alpha_s)
            w_0 = format(w0[i],w0Format)
            line = line.replace('-1.0  ',w_0)
            w_a = format(wa[i],waFormat)
            line = line.replace('0.0  ',w_a)
            Nur = format(N_ur[i],NurFormat)
            line = line.replace('1.7328',Nur)
            print(line,end='')        
        # copy the rest of the lines
    else: print(line,end='')

