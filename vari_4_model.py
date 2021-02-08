
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
    taw = 1/np.cosh((v - beta_w)/ (2 * gamma_w))
    return taw

def dvt_dwt(k,t):
    v,w = k[0],k[1]
    dv_dt = (i_stim - gfast * m_inf(v)*(v-ena) - gslow * w * (v - ek) - gleak * (v - eleak))/c
    dw_dt = phi_w * (w_inf(v)-w) / taw_eq(v)
    dtv = dv_dt,dw_dt
    return dtv

# vari the I_stim
def dvt_dwt_var(k,t):
    i_stim = i_stim_vari[int ((int(t) * (len(i_stim_vari)-1)) / 20) ]

    v,w = k[0],k[1]
    dv_dt = (i_stim - gfast * m_inf(v)*(v-ena) - gslow * w * (v - ek) - gleak * (v - eleak))/c
    dw_dt = phi_w * (w_inf(v)-w) / taw_eq(v)
    dtv = dv_dt,dw_dt
    return dtv
    

#initial values of v and w
v_0 =-2
w_0 = 0.02
x = [v_0,w_0]

#Ploting
t = np.linspace(0,20,100)
vs_ws = odeint(dvt_dwt, x, t)
plt.plot(t,vs_ws[:,0],'r')
plt.xlabel('time')
plt.ylabel('v(t)')
plt.title('Constant I_stim')
plt.show()




#2nd plot

t = np.linspace(0,20,100)
i_stim_vari = np.linspace(0,100,100)
vs_ws = odeint(dvt_dwt_var, x, t)
plt.plot(t,vs_ws[:,0],'b')
plt.xlabel('time')
plt.ylabel('v(t)')
plt.title("Varying I_stim")

plt.show()

