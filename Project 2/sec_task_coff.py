import numpy as np
from scipy import signal,stats
import matplotlib.pyplot as plt
from math import log2
import seaborn as sns

coff_matrix = np.zeros((31,31))

def create_coff_matrix(max_index):
    z = 0
    for i in range(31):
        for j in range(i+1,31):
            coff_matrix[i,j] = initi[max_index][z]
            coff_matrix[j,i] = initi[max_index][z]
            z+=1

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

#wavelet_data = np.zeros_like(data)
wavelet_data = np.load("wavelet_data_beta.npy",allow_pickle=True)

print(wavelet_data.shape)

all_rmd=list()
initi = list()

#calculate RMD
for x in range(wavelet_data.shape[0]):
    p_coffs = list()
    for i in range(wavelet_data[x].shape[1]-1):
        for j in range(i+1,wavelet_data[x].shape[1]):
            l = np.linalg.norm(wavelet_data[x][:,i]-wavelet_data[x][:,j])
            #forget about the comparison
            #maybe we keep the values and normalize
            p_coffs.append(l)
    initi.append(p_coffs)
    all_rmd.append(np.average(p_coffs))


maxy = all_rmd.index(max(all_rmd))
p1 = np.argmax(all_rmd[:10])
p2 = np.argmax(all_rmd[10:20])
p3 = np.argmax(all_rmd[20:30])
p4 = np.argmax(all_rmd[30:40])
p5 = np.argmax(all_rmd[40:])

participants = [p1,p2,p3,p4,p5]
print(participants)
maxy = 4 
create_coff_matrix(maxy)
raw, column = np.argmax(coff_matrix)//31, np.argmax(coff_matrix)%31
print(raw,column)
maxy = 12 
create_coff_matrix(maxy)
raw2, column2 = np.argmax(coff_matrix)//31, np.argmax(coff_matrix)%31
print(raw2,column2)
maxy = 20 
create_coff_matrix(maxy)
raw3, column3 = np.argmax(coff_matrix)//31, np.argmax(coff_matrix)%31
print(raw3,column3)
maxy = 33 
create_coff_matrix(maxy)
raw4, column4 = np.argmax(coff_matrix)//31, np.argmax(coff_matrix)%31
print(raw4,column4)
maxy = 42 
create_coff_matrix(maxy)
raw5, column5 = np.argmax(coff_matrix)//31, np.argmax(coff_matrix)%31
print(raw5,column5)
"""    
print(maxy)
create_coff_matrix(maxy)
norm_matrix= 2.0*(coff_matrix-np.min(coff_matrix))/np.ptp(coff_matrix)-1        
#sns.heatmap(coff_matrix, annot = False)
sns.heatmap(norm_matrix, annot = False)
plt.show()
"""