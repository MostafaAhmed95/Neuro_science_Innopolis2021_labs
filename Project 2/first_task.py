import numpy as np
from scipy import signal,stats
import matplotlib.pyplot as plt

"""
files = ['Backgr_int_0.1.dat', 'Backgr_int_0.2.dat', 'Backgr_int_0.3.dat', 'Backgr_int_0.4.dat', 'Backgr_int_0.5.dat', 'Backgr_int_0.6.dat','Backgr_int_0.7.dat','Backgr_int_0.8.dat','Backgr_int_0.9.dat','Backgr_int_1.dat']
all_avg = list()
raw_data = list()
fil_data = list()

for parti in range(1,6):
    for d in files:

        #all_avg = list()
        #for name in data_set:                                        
        data = np.loadtxt("Participant "+str(parti)+"/"+d)
        raw_data.append(data)
        fil_cof = signal.firwin(data.shape[0], [15, 30], pass_zero=False, fs=250)
        for i in range (data.shape[1]):
            data[:,i] = np.convolve(data[:,i],fil_cof,'same') 
        
        fil_data.append(data) 
        #calculate the combinations of p values

        p_coffs = list()
        for i in range(data.shape[1]-1):
            for j in range (i+1,data.shape[1]):
                p_c, _ = stats.pearsonr(data[:,i],data[:,j])
                p_coffs.append(p_c)
            
        all_avg.append(np.average(p_coffs))

np.save("raw_data_beta",np.array(raw_data))
np.save("fil_data_beta",np.array(raw_data))
print(len(all_avg))
x = np.linspace(0.1,1,10)
plt.plot(x,all_avg[:10],'r')
plt.plot(x,all_avg[10:20],'g')
plt.plot(x,all_avg[20:30],'b')
plt.plot(x,all_avg[30:40],'y')
plt.plot(x,all_avg[40:50],'k')
plt.xlabel('values')
plt.ylabel('avareges')
"""


all_avg = list()
raw_data = np.load("raw_data_alpha.npy",allow_pickle=True)
fil_data = np.load("fil_data_alpha.npy",allow_pickle=True)

for i in range (raw_data.shape[0]):
    p_coffs = list()
    for x in range(fil_data[i].shape[1]-1):
        for y in range(x+1,fil_data[i].shape[1]):
            p_c, _ = stats.pearsonr(fil_data[i][:,x],fil_data[i][:,y])
            p_coffs.append(p_c)
    all_avg.append(np.average(p_coffs))

all_avg_array = np.array(all_avg)
part_1 = np.argmax(all_avg_array[:10])
part_2 = np.argmax(all_avg_array[10:20])
part_3 = np.argmax(all_avg_array[20:30])
part_4 = np.argmax(all_avg_array[30:40])
part_5 = np.argmax(all_avg_array[40:])

print(part_1)
print(part_2)
print(part_3)
print(part_4)
print(part_5)

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
