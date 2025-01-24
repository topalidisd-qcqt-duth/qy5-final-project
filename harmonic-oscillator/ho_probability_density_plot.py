import matplotlib.pyplot as plt
import numpy as np
from harmonic_oscillator import psi_x, psi_p

def plot_probability_density_x(ω):
    
    x_values= np.linspace(-8,8, 1000)
    psi_values_ground_state = []
    psi_values_first_excited_state = []
    psi_values_second_excited_state = []

    for x in x_values:
            psi_values_ground_state.append(psi_x(x,0,ω)**2)
            
    for x in x_values:
            psi_values_first_excited_state.append(psi_x(x,1,ω)**2)
            
    for x in x_values:
            psi_values_second_excited_state.append(psi_x(x,2,ω)**2)

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, psi_values_ground_state, linestyle='-', label='n=1')
    plt.plot(x_values, psi_values_first_excited_state,linestyle='-', label='n=2')
    plt.plot(x_values, psi_values_second_excited_state, linestyle='-', label='n=3')
    plt.xlabel('x (a.u.)', fontsize=12)
    plt.ylabel('Probability density', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()    

def plot_probability_density_x_omega():
    
    omegas=[0.5,2.5,5]
    x_values_1= np.linspace(-4, 4, 100)
    x_values_2= np.linspace(-4, 4, 100)
    x_values_3= np.linspace(-4, 4, 100)

    psi_values_1 = []
    psi_values_2 = []
    psi_values_3 = []

    for x in x_values_1:
            psi_values_1.append(psi_x(x,0,omegas[0])**2)
            
    for x in x_values_2:
            psi_values_2.append(psi_x(x,0,omegas[1])**2)
            
    for x in x_values_3:
            psi_values_3.append(psi_x(x,0,omegas[2])**2)

    plt.figure(figsize=(10, 5))
    plt.plot(x_values_1, psi_values_1, linestyle='-', label='ω='+str(omegas[0]))
    plt.plot(x_values_2, psi_values_2,linestyle='-', label='ω='+str(omegas[1]))
    plt.plot(x_values_3, psi_values_3, linestyle='-', label='ω='+str(omegas[2]))
    plt.xlabel('x (a.u.)', fontsize=12)
    plt.ylabel('Probability density', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()    



def plot_probability_density_p(ω):
    
    p_values= np.linspace(-6,6, 1000)
    psi_values_ground_state = []
    psi_values_first_excited_state = []
    psi_values_second_excited_state = []

    for p in p_values:
            psi_values_ground_state.append(psi_p(p,0,ω)**2)
            
    for p in p_values:
            psi_values_first_excited_state.append(psi_p(p,1,ω)**2)
            
    for p in p_values:
            psi_values_second_excited_state.append(psi_p(p,2,ω)**2)

    plt.figure(figsize=(10, 5))
    plt.plot(p_values, psi_values_ground_state, linestyle='-', label='n=1')
    plt.plot(p_values, psi_values_first_excited_state,linestyle='-', label='n=2')
    plt.plot(p_values, psi_values_second_excited_state, linestyle='-', label='n=3')
    plt.xlabel('p (a.u.)', fontsize=12)
    plt.ylabel('Probability density', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()    


def plot_probability_density_p_omega():
    
    omegas=[0.5,2.5,5]
    p_values_1= np.linspace(-6, 6, 100)
    p_values_2= np.linspace(-6, 6, 100)
    p_values_3= np.linspace(-6, 6, 100)

    psi_values_1 = []
    psi_values_2 = []
    psi_values_3 = []

    for p in p_values_1:
            psi_values_1.append(psi_p(p,0,omegas[0])**2)
            
    for p in p_values_2:
            psi_values_2.append(psi_p(p,0,omegas[1])**2)
            
    for p in p_values_3:
            psi_values_3.append(psi_p(p,0,omegas[2])**2)

    plt.figure(figsize=(10, 5))
    plt.plot(p_values_1, psi_values_1, linestyle='-', label='ω='+str(omegas[0]))
    plt.plot(p_values_2, psi_values_2,linestyle='-', label='ω='+str(omegas[1]))
    plt.plot(p_values_3, psi_values_3, linestyle='-', label='ω='+str(omegas[2]))
    plt.xlabel('p (a.u.)', fontsize=12)
    plt.ylabel('Probability density', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()    


plot_probability_density_x(0.5)
plot_probability_density_x_omega()

plot_probability_density_p(0.5)
plot_probability_density_p_omega()

