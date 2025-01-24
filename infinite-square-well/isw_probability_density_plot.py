import matplotlib.pyplot as plt
import numpy as np
from infinite_square_well import psi_x_odd, psi_x_even, psi_p_odd, psi_p_even

def plot_probability_density_x(L):
    
    x_values= np.linspace(-L/2, L/2, 100)
    psi_values_ground_state = []
    psi_values_first_excited_state = []
    psi_values_second_excited_state = []

    for x in x_values:
            psi_values_ground_state.append(psi_x_odd(x,1,L)**2)
            
    for x in x_values:
            psi_values_first_excited_state.append(psi_x_even(x,2,L)**2)
            
    for x in x_values:
            psi_values_second_excited_state.append(psi_x_odd(x,3,L)**2)

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, psi_values_ground_state, linestyle='-', label='n=1')
    plt.plot(x_values, psi_values_first_excited_state,linestyle='-', label='n=2')
    plt.plot(x_values, psi_values_second_excited_state, linestyle='-', label='n=3')
    plt.xlabel('x (a.u.)', fontsize=12)
    plt.ylabel('Probability density', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()    

def plot_probability_density_p(L):
    
    p_values= np.linspace(-10/L, 10/L, 100)
    psi_values_ground_state = []
    psi_values_first_excited_state = []
    psi_values_second_excited_state = []

    for x in p_values:
            psi_values_ground_state.append(psi_p_odd(x,1,L)**2)
            
    for x in p_values:
            psi_values_first_excited_state.append(psi_p_even(x,2,L)**2)
            
    for x in p_values:
            psi_values_second_excited_state.append(psi_p_odd(x,3,L)**2)

    plt.figure(figsize=(10, 5))
    plt.plot(p_values, psi_values_ground_state, linestyle='-', label='n=1')
    plt.plot(p_values, psi_values_first_excited_state,linestyle='-', label='n=2')
    plt.plot(p_values, psi_values_second_excited_state, linestyle='-', label='n=3')
    plt.xlabel('p (a.u.)', fontsize=12)
    plt.ylabel('Probability density', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()    


plot_probability_density_x(5)
plot_probability_density_p(5)