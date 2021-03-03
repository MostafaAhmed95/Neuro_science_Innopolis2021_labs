import numpy as np
from scipy import signal,stats
import matplotlib.pyplot as plt
import seaborn as sns

initi = list()
all_avg = list()
raw_data = np.load("raw_data_alpha.npy",allow_pickle=True)
fil_data = np.load("fil_data_alpha.npy",allow_pickle=True)


for r in range(raw_data.shape[0]):
    raw_data[r] = raw_data[r][:,:31]
    fil_data[r] = fil_data[r][:,:31]

for i in range (raw_data.shape[0]):
    p_coffs = list()
    for x in range(fil_data[i].shape[1]-1):
        for y in range(x+1,fil_data[i].shape[1]):
            p_c, _ = stats.pearsonr(fil_data[i][:,x],fil_data[i][:,y])
            p_coffs.append(p_c)
    initi.append(p_coffs)
    all_avg.append(np.average(p_coffs))
        
print(len(initi))

#maxy = all_avg.index(max(all_avg))
#print(initi[maxy].index(max(initi[maxy])))
#print(maxy)

maxy = 2

#coff_matrix = np.identity(34)
coff_matrix = np.zeros((31,31))
def create_coff_matrix(max_index):
    z = 0
    for i in range(31):
        for j in range(i+1,31):
            coff_matrix[i,j] = initi[max_index][z]
            coff_matrix[j,i] = initi[max_index][z]
            z+=1

maxy = 8 
create_coff_matrix(maxy)
raw, column = np.argmax(coff_matrix)//31, np.argmax(coff_matrix)%31    
maxy = 10 
create_coff_matrix(maxy)
raw2, column2 = np.argmax(coff_matrix)//31, np.argmax(coff_matrix)%31
maxy = 22 
create_coff_matrix(maxy)
raw3, column3 = np.argmax(coff_matrix)//31, np.argmax(coff_matrix)%31
maxy = 37 
create_coff_matrix(maxy)
raw4, column4 = np.argmax(coff_matrix)//31, np.argmax(coff_matrix)%31
maxy = 48 
create_coff_matrix(maxy)
raw5, column5 = np.argmax(coff_matrix)//31, np.argmax(coff_matrix)%31 
print(raw,column)
print(raw2,column2)
print(raw3,column3)
print(raw4,column4)
print(raw5,column5)

norm_matrix= 2.0*(coff_matrix-np.min(coff_matrix))/np.ptp(coff_matrix)-1        
#print(coff_matrix.argmax())
#sns.heatmap(coff_matrix, annot = False)
sns.heatmap(norm_matrix, annot = False)
plt.show()

