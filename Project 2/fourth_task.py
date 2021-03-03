import scipy as sp
import scipy.stats
import numpy as np


#####Chi-test######
raw_data = np.load("raw_data_beta.npy",allow_pickle=True)

"""
#max particiant max intensity
chi, p_value = sp.stats.chisquare([raw_data[2][:,19], raw_data[2][:,23]],axis=1)
chi2, p_value2 = sp.stats.chisquare([raw_data[11][:,7],raw_data[11][:,15]],axis=1)
chi3, p_value3= sp.stats.chisquare([raw_data[20][:,19],raw_data[20][:,23]],axis=1)
chi4, p_value4 = sp.stats.chisquare([raw_data[35][:,4],raw_data[35][:,24]],axis=1)
chi5, p_value5 = sp.stats.chisquare([raw_data[47][:,7],raw_data[47][:,19]],axis=1)
print(chi,p_value)
print(chi2.shape)
print(chi2,p_value2)
print(chi3,p_value3)
print(chi4,p_value4)
print(chi5,p_value5)


"""
#####T-test######
"""
stat1, p1 = sp.stats.ttest_ind(raw_data[2][:,19], raw_data[2][:,23])
stat2, p2 = sp.stats.ttest_ind(raw_data[11][:,7],raw_data[11][:,15])
stat3, p3 = sp.stats.ttest_ind(raw_data[20][:,19],raw_data[20][:,23])
stat4, p4 = sp.stats.ttest_ind(raw_data[35][:,4],raw_data[35][:,24])
stat5, p5 = sp.stats.ttest_ind(raw_data[47][:,7],raw_data[47][:,19])
"""
"""
stat1, p1 = sp.stats.ttest_ind(raw_data[8][:,8], raw_data[8][:,20])
stat2, p2 = sp.stats.ttest_ind(raw_data[10][:,7],raw_data[10][:,15])
stat3, p3 = sp.stats.ttest_ind(raw_data[22][:,19],raw_data[22][:,23])
stat4, p4 = sp.stats.ttest_ind(raw_data[37][:,7],raw_data[37][:,19])
stat5, p5 = sp.stats.ttest_ind(raw_data[48][:,7],raw_data[47][:,22])

print(stat1,p1)
print(stat2,p2)
print(stat3,p3)
print(stat4,p4)
print(stat5,p5)
"""


#####Mann-Whitney U Test#####
stat1, p1 = sp.stats.mannwhitneyu(raw_data[2][:,19], raw_data[2][:,23])
stat2, p2 = sp.stats.mannwhitneyu(raw_data[11][:,7],raw_data[11][:,15])
stat3, p3 = sp.stats.mannwhitneyu(raw_data[20][:,19],raw_data[20][:,23])
stat4, p4 = sp.stats.mannwhitneyu(raw_data[35][:,4],raw_data[35][:,24])
stat5, p5 = sp.stats.mannwhitneyu(raw_data[47][:,7],raw_data[47][:,19])

print(stat1,p1)
print(stat2,p2)
print(stat3,p3)
print(stat4,p4)
print(stat5,p5)