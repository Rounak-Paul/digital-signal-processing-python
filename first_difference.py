import mysignals as sigs

def first_difference(sig_src_arr):
    sig_dest_arr = []

    for i in range(len(sig_src_arr)):
        sig_dest_arr.append(0)
    
    for i in range(len(sig_dest_arr)):
        sig_dest_arr[i] = sig_dest_arr[i] - sig_src_arr[i-1]

    return sig_dest_arr 

import matplotlib.pyplot as plt
plt.plot(first_difference(sigs.InputSignal_1kHz_15kHz))
plt.show()