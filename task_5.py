import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#contstants
i_stim = 0

#vari the i_stim
#i_stim_vari = np.linspace(0,200,200)

c = 2
gleak = 2
gfast = 20
gslow = 20
ena = 50
ek = -100
eleak = -70
phi_w = 0.15
beta_m = -10
gamma_m = 18
beta_w = -10
gamma_w = 13
D = 0

g_syn = 2

#equations
def m_inf(v):
    minf = 0.5 * (1+np.tanh((v-beta_m)/gamma_m))
    return minf

def w_inf(v):
    winf = 0.5 * (1+np.tanh((v-beta_w)/gamma_w))
    return winf

def i_syn(v_i,v_j):
    return g_syn * (v_i - v_j)

def taw_eq(v):
    #print(v)
    taw = 1/np.cosh((v - beta_w)/ (2 * gamma_w))
    return taw

def dvt_dwt(x,t):
    dtv = list()
    for i in range (0,len(x),2):
        if (i == (len(x))-2):
            v2,w2 = 0,0
        else:
            v2,w2 = x[i+2], x[i+3] 
        v1,w1 = x[i],x[i+1]
        dv_dt = (i_stim - gfast * m_inf(v1)*(v1-ena) - gslow * w1 * (v1 - ek) - gleak * (v1 - eleak)) - i_syn(v1,v2)/c
        dw_dt = phi_w * ((w_inf(v1)-w1)/taw_eq(v1))
        dtv.extend([dv_dt,dw_dt]) 
    return dtv

#initial values of v and w
vs = np.random.randint (low= -52.14, high= -20, size= 25)
ws = np.random.uniform(0.02,0.01, size=25)

x = list()
# for loop to concate vs and ws in one list
for i in range(len(vs)):
    x.append(vs[i])
    x.append(ws[i])

t = np.linspace(0,20,100)
vs_ws = odeint(dvt_dwt, x, t)
#adding the noise and varying the D value from 0.01 to 1
#Let's start correlation
accum_corr = 0
corr_time = list()
noise = np.linspace(0.01,1,100)
for i in noise:
    D = i
    accum_corr = 0
    for i in range(0,vs_ws.shape[1],2):
        x = vs_ws[:,i] + (D * np.random.normal(0,1,100))
        accum_corr += ((np.correlate(x[3:], x[:-3])) ** 2) 
    corr_time.append(accum_corr)

plt.plot(noise,corr_time,'r')
plt.xlabel('D noise')
plt.ylabel('t correlation time')
plt.title("Correlation time and the noise")
plt.show()
