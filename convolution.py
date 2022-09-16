import mysignals as sigs

def convolution(sig_src_arr, imp_response_arr):
    sig_dest_arr = []

    for i in range(len(sig_src_arr) + len(imp_response_arr)):
        sig_dest_arr.append(0)
    
    for i in range(len(sig_src_arr)):
        for j in range(len(imp_response_arr)):
            sig_dest_arr[i+j] = sig_dest_arr[i+j] + sig_src_arr[i]*imp_response_arr[j]

    return sig_dest_arr

import matplotlib.pyplot as plt

plt.plot(convolution(sigs.InputSignal_1kHz_15kHz,sigs.Impulse_response))
plt.show()