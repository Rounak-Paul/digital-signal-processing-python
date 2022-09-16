import mysignals as sigs
import math

def dft(sig_src_arr):
    t = int(len(sig_src_arr)/2)
    sig_dest_imx_arr = [None]*t
    sig_dest_rex_arr = [None]*t
    sig_dest_mag_arr = [None]*t

    for j in range(t):
        sig_dest_imx_arr[j] = 0
        sig_dest_rex_arr[j] = 0

    for k in range(t):
        for i in range(len(sig_src_arr)):
            sig_dest_rex_arr[k] = sig_dest_rex_arr[k] + sig_src_arr[i]*math.cos(2*math.pi*k*i/len(sig_src_arr))
            sig_dest_imx_arr[k] = sig_dest_imx_arr[k] - sig_src_arr[i]*math.sin(2*math.pi*k*i/len(sig_src_arr))

    for x in range(t):
        sig_dest_mag_arr[x] = math.sqrt(math.pow(sig_dest_rex_arr[x],2) + math.pow(sig_dest_imx_arr[x],2))
    
    return sig_dest_rex_arr, sig_dest_imx_arr, sig_dest_mag_arr

import matplotlib.pyplot as plt

re,im,mag = dft(sigs.InputSignal_1kHz_15kHz)

plt.plot(mag)
plt.show()