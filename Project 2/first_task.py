import numpy as np
from scipy import signal,stats
import matplotlib.pyplot as plt

files = ['Backgr_int_0.1.dat', 'Backgr_int_0.2.dat', 'Backgr_int_0.3.dat', 'Backgr_int_0.4.dat', 'Backgr_int_0.5.dat', 'Backgr_int_0.6.dat','Backgr_int_0.7.dat','Backgr_int_0.8.dat','Backgr_int_0.9.dat','Backgr_int_1.dat']
all_avg = list()
for parti in range(1,6):
    for d in files:

        
        #all_avg = list()
        #for name in data_set:                                        
        data = np.loadtxt("Participant "+str(parti)+"/"+d)
        fil_cof = signal.firwin(data.shape[0], [8, 12], pass_zero=False, fs=250)

        for i in range (data.shape[1]):
            data[:,i] = np.convolve(data[:,i],fil_cof,'same') 

            #calculate the combinations of p values

        p_coffs = list()
        for i in range(data.shape[1]-1):
            for j in range (i+1,data.shape[1]):
                p_c, _ = stats.pearsonr(data[:,i],data[:,j])
                p_coffs.append(p_c)
            
        all_avg.append(np.average(p_coffs))

print(len(all_avg))
x = np.linspace(0.1,1,10)
plt.plot(x,all_avg[:10],'r')
plt.plot(x,all_avg[10:20],'g')
plt.plot(x,all_avg[20:30],'b')
plt.plot(x,all_avg[30:40],'y')
plt.plot(x,all_avg[40:50],'k')
plt.xlabel('values')
plt.ylabel('avareges')
plt.show()
