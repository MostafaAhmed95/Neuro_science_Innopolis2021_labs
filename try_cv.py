import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#contstants
i_stim = 0
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


#euations
def m_inf(v):
    minf = 0.5 * (1+np.tanh((v-beta_m)/gamma_m))
    return minf

def w_inf(v):
    winf = 0.5 * (1+np.tanh((v-beta_w)/gamma_w))
    return winf

def taw_eq(v):
    #print(v)
    taw = 1/np.cosh((v - beta_w)/ (2 * gamma_w))
    return taw

def dvt_dwt(x,t):
    #print(x)
    v,w = x[0],x[1]
    #v = x
    dv_dt = (i_stim - gfast * m_inf(v)*(v-ena) - gslow * w * (v - ek) - gleak * (v - eleak))/c
    dw_dt = phi_w * ((w_inf(v)-w)/taw_eq(v))
    dtv = dv_dt,dw_dt
    return dtv

#initial values of v and w
v_0 = -2
w = 0.02
x = [v_0,w]
t = np.linspace(0,20,10)

#vari the i_stim
#i_stim = np.linspace(0,200,200)
#l = dvt_dwt(x,t=0)
vs_ws = odeint(dvt_dwt, x, t)
#vs_ws = odeint(dvt_dwt, x, t)


print(vs_ws[:,0])
plt.plot(t,vs_ws[:,0])
plt.xlabel('time')
plt.ylabel('v(t)')
plt.show()
