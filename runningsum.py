import mysignals as sigs

def runningsum(sig_src_arr):
    sig_dest_arr = []

    for i in range(len(sig_src_arr)):
        sig_dest_arr.append(0)
    
    for i in range(len(sig_dest_arr)):
        sig_dest_arr[i] = sig_dest_arr[i-1] + sig_src_arr[i]

    return sig_dest_arr 

import matplotlib.pyplot as plt
plt.plot(runningsum(sigs.InputSignal_1kHz_15kHz))
plt.show()