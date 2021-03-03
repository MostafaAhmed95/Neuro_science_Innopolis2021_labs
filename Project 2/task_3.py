import numpy as np
import matplotlib.pyplot as plt

wavelet_data = np.load("wavelet_data_beta.npy",allow_pickle=True)

all_rmd=list()
# only for maximum participant, maxiumum intensity
#calculate RMD
# maximum element for alpha is element 34 which is particpant 4 intensity 0.4
# maximum element for beta is element 16 which is particpant 2 intensity 0.7

#specific_file = wavelet_data[34] 
p_coffs = list()
for window in range(500): 
    for i in range(wavelet_data[16].shape[1]-1):
        for j in range(i+1,wavelet_data[16].shape[1]):
            l = np.linalg.norm(wavelet_data[16][window:window+15,i]-wavelet_data[16][window:window+15,j])
            #forget about the comparison
            #maybe we keep the values and normalize
            p_coffs.append(l)
    all_rmd.append(np.average(p_coffs))

print(len(all_rmd))

x = np.linspace(0,500,500)
plt.plot(x,all_rmd,'r')
plt.xlabel('numbet of windows')
plt.ylabel('values')
plt.show()
