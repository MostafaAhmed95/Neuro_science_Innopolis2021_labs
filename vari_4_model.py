
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#contstants
i_stim = 75
c = 2
gleak = 2
gfast = 20
gslow = 20
ena = 50
ek = -100
eleak = -70
phi_w = 0.15
beta_m = 30
gamma_m = 18
beta_w = -10
gamma_w = 13


#euations
def m_inf(v):
    minf = 0.5 * (1+np.tanh((v-beta_m)/gamma_m))
    return minf

def w_inf(v):
    winf = 0.5 * (1+np.tanh((v-beta_w)/gamma_w))
    return winf

def taw_eq(v):
    taw = 1/(np.cosh((v-beta_w)/2*gamma_w))
    return taw

def dvt_dwt(k,t):
    # vari the I_stim
    #print(int(t/0.6))
    #i_stim = i_stim_vari[int(t/0.6)]
    print(k)
    #print(int(t))
    v,w = k[0],k[1]
    dv_dt = (i_stim - gfast * m_inf(v)*(v-ena) - gslow * w * (v - ek) - gleak * (v - eleak))/c
    dw_dt = phi_w * (w_inf(v)-w) / taw_eq(v)
    dtv = dv_dt,dw_dt
    print(dtv)
    return dtv
    
    

#initial values of v and w
v_0 = 10
w_0 = 2
x = [v_0,w_0]

#Ploting
#t = np.linspace(0,12,20)
t = np.linspace(0,10,10)
#print(t)
vs_ws = odeint(dvt_dwt, x, t)
plt.plot(t,vs_ws[:,0],'r')
plt.xlabel('time')
plt.ylabel('v(t)')
plt.show()


#t = np.linspace(0,12,100)
#i_stim_vari = np.linspace(0,100,20)
#i_stim_vari = np.linspace(0,12,20)
#print(type(0/0.6))
#print(i_stim_vari[int(0/0.6)])

#2nd plot
beta_m = -10
t = np.linspace(0,12,100)
i_stim_vari = np.linspace(0,100,100)
#print(type(0/0.6))
#print(i_stim_vari[int(0/0.6)])
vs_ws = odeint(dvt_dwt, x, t)
plt.plot(t,vs_ws[:,0],'b')
plt.xlabel('time')
plt.ylabel('v(t)')

plt.show()

