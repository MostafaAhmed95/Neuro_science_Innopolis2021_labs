import numpy as np
from scipy import signal,stats
import matplotlib.pyplot as plt
from math import log2
"""
files = ['Backgr_int_0.1.dat', 'Backgr_int_0.2.dat', 'Backgr_int_0.3.dat', 'Backgr_int_0.4.dat', 'Backgr_int_0.5.dat', 'Backgr_int_0.6.dat','Backgr_int_0.7.dat','Backgr_int_0.8.dat','Backgr_int_0.9.dat','Backgr_int_1.dat']
all_avg = list()
for parti in range(1,6):
    for d in files:

        
        #all_avg = list()
        #for name in data_set:                                        
        data = np.loadtxt("Participant "+str(parti)+"/"+d)
        fil_cof = signal.firwin(data.shape[0], [8, 12], pass_zero=False, fs=250)
        new_data = np.zeros_like(data)
        for i in range (data.shape[1]):
            new_data[:,i] = np.convolve(data[:,i],fil_cof,'same') 
        break
    break

print(data.shape)
print(new_data.shape)
print(new_data[0,0])
x = np.sqrt(new_data[:,0])
print("passed")
#morelt = 0

for i in range (data.shape[1]):
    wavelet_data[:,i] = wavelet(new_data[:,i],data[:,i])

print(wavelet_data.shape) 
all_avg = list() #list will contain the whole averages
p_coffs = list()
#calculate RMD
for i in range(data.shape[1]):
    for j in range(i+1,data.shape[1]):
        x = numpy.linalg.norm(wavelet_data[:,i],wavelet_data[:,j])
        #forget about the comparison
        #maybe we keep the values and normalize
        p_coffs.append(x)

all_avg.append(np.average(p_coffs))


# the RMD in the second equation we put two channels 1 with 2 for example
# then we keep summtion for all values and get output 1 value

print(type(p))
for x in range (raw_data.shape[0]):
    for i in range(raw_data[0].shape[1]):
        wavelet_data[x][:,i] =wavelet(fil_data[x][:,i],raw_data[x][:,i])

np.save("wavlet_data_alpha",wavelet_data)


raw_data = np.load("raw_data_alpha.npy",allow_pickle=True)
fil_data = np.load("raw_data_alpha.npy",allow_pickle=True)

ally = list()
for x in range (raw_data.shape[0]):
    wavelet_data = np.empty_like(raw_data[x], dtype=complex)
    for i in range(raw_data[x].shape[1]):
        wavelet_data[:,i] =wavelet(fil_data[x][:,i],raw_data[x][:,i])
    ally.append(wavelet_data)


np.save("wavelet_data_alpha",np.array(ally))

"""

def morlet(f):
    #calculate morlet complex
    return (1/(np.pi**(1/4))) * np.exp((2*np.pi*f)*1j) * (np.exp(-(f**2)/2))

def wavelet(filter,raw):
    # calculate the wavelet
    # both filter and raw are column representing a channel 
    # for loop for different morlet
    value = 0
    for i in range (filter.shape[0]):
        value += raw[i] * morlet(filter[i])
    # return a column value of a channel 
    return np.sqrt(filter.astype(complex)) * value

"""
raw_data = np.load("raw_data_beta.npy",allow_pickle=True)
fil_data = np.load("fil_data_beta.npy",allow_pickle=True)

ally = list()
for x in range (raw_data.shape[0]):
    wavelet_data = np.empty_like(raw_data[x], dtype=complex)
    for i in range(raw_data[x].shape[1]):
        wavelet_data[:,i] =wavelet(fil_data[x][:,i],raw_data[x][:,i])
    ally.append(wavelet_data)


np.save("wavelet_data_beta",np.array(ally))
"""

#wavelet_data = np.zeros_like(data)
wavelet_data = np.load("wavelet_data_beta.npy",allow_pickle=True)

print(wavelet_data.shape)

all_rmd=list()
#calculate RMD
for x in range(wavelet_data.shape[0]):
    p_coffs = list()
    for i in range(wavelet_data[x].shape[1]-1):
        for j in range(i+1,wavelet_data[x].shape[1]):
            l = np.linalg.norm(wavelet_data[x][:,i]-wavelet_data[x][:,j])
            #forget about the comparison
            #maybe we keep the values and normalize
            p_coffs.append(l)
    all_rmd.append(np.average(p_coffs))

"""
print(len(all_rmd))

x = np.linspace(0.1,1,10)
plt.plot(x,all_rmd[:10],'r')
plt.plot(x,all_rmd[10:20],'g')
plt.plot(x,all_rmd[20:30],'b')
plt.plot(x,all_rmd[30:40],'y')
plt.plot(x,all_rmd[40:50],'k')
plt.xlabel('intensity')
plt.ylabel('values')
plt.show()
"""
###Normalized##
all_avg_array = np.array(all_rmd)
norm_matrix= 2.0*(all_avg_array-np.min(all_avg_array))/np.ptp(all_avg_array)-1
x = np.linspace(0.1,1,10)
plt.plot(x,norm_matrix[:10],'r')
plt.plot(x,norm_matrix[10:20],'g')
plt.plot(x,norm_matrix[20:30],'b')
plt.plot(x,norm_matrix[30:40],'y')
plt.plot(x,norm_matrix[40:50],'k')
plt.xlabel('normalize_values')
plt.ylabel('intensties')
plt.show()

