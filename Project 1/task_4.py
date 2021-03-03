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
        if (i == len(x)-2):
            v2,w2 = 0,0
        else:
            v2,w2 = x[i+2], x[i+3] 
        v1,w1 = x[i],x[i+1]
        dv_dt = (i_stim - gfast * m_inf(v1)*(v1-ena) - gslow * w1 * (v1 - ek) - gleak * (v1 - eleak)) - i_syn(v1,v2)/c
        dw_dt = phi_w * ((w_inf(v1)-w1)/taw_eq(v1))
        dtv.extend([dv_dt,dw_dt]) 
    return dtv

#initial values of v and w
vi_0 = -2
wi_0 = 0.02
vj_0 = 5
wj_0 = 0.03
x = [vi_0,wi_0,vj_0,wj_0]
t = np.linspace(0,20,100)



vs_ws = odeint(dvt_dwt, x, t)
#print((D * np.random.normal(0,1,10)).shape)
vs_ws[:,0] = vs_ws[:,0]+(D * np.random.normal(0,1,100))
print(vs_ws[:,0].shape)
plt.plot(t,vs_ws[:,0],'b')
plt.xlabel('time')
plt.ylabel('v(t)')
plt.title("1st Neuron")

"""
plt.plot(t,vs_ws[:,3],'r')
plt.xlabel('time')
plt.ylabel('v(t)')
plt.title('2nd Neuron')
"""
plt.show()