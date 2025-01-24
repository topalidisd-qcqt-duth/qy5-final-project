import matplotlib.pyplot as plt
from harmonic_oscillator import entropy_p, entropy_x

def plot_entropies():
    
    omegas = [0.06,0.08,0.2,0.4,0.5,1,2,3,4,5,6,7,8]

    entropy_x_values_ground_state= [entropy_x(0, ω) for ω in omegas]
    entropy_x_values_first_excited_state = [entropy_x(1, ω) for ω in omegas]
    entropy_x_values_second_excited_state = [entropy_x(2, ω) for ω in omegas]
    entropy_p_values_ground_state = [entropy_p(0, ω) for ω in omegas]
    entropy_p_values_first_excited_state = [entropy_p(1, ω) for ω in omegas]
    entropy_p_values_second_excited_state = [entropy_p(2, ω) for ω in omegas]


    plt.figure(figsize=(10, 5))
    plt.plot(omegas, entropy_x_values_ground_state, marker="o", linestyle='-', label='Sx (n=0)')
    plt.plot(omegas, entropy_x_values_first_excited_state, marker="s", linestyle='-', label='Sx (n=1)')
    plt.plot(omegas, entropy_x_values_second_excited_state, marker="D", linestyle='-', label='Sx (n=2)')
    plt.plot(omegas, entropy_p_values_ground_state, marker="o",linestyle='-', label='Sp (n=0)')
    plt.plot(omegas, entropy_p_values_first_excited_state, marker="s", linestyle='-', label='Sp (n=1)')
    plt.plot(omegas, entropy_p_values_second_excited_state, marker="D", linestyle='-', label='Sp (n=2)')
    plt.xlabel('ω (a.u.)', fontsize=12)
    plt.ylabel('Sx, Sp', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()    
 
def plot_total_entropy():
    
    
    omegas = [0.06,0.08,0.2,0.4,0.5,1,2,3,4,5,6,7,8]

    entropy_t_values_ground_state = [entropy_x(0, ω)+entropy_p(0, ω) for ω in omegas]
    entropy_t_values_first_excited_state = [entropy_x(1, ω) +entropy_p(1, ω) for ω in omegas]
    entropy_t_values_second_excited_state = [entropy_x(2, ω)+entropy_p(2, ω) for ω in omegas]


    plt.figure(figsize=(10, 5))

    plt.plot(omegas, entropy_t_values_ground_state, marker="o",linestyle='-', label='n=1')
    plt.plot(omegas, entropy_t_values_first_excited_state, marker="s", linestyle='-', label='n=2')
    plt.plot(omegas, entropy_t_values_second_excited_state, marker="D", linestyle='-', label='n=3')
    plt.xlabel('ω (a.u.)', fontsize=12)
    plt.ylabel('St', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()    
 

plot_entropies()
plot_total_entropy()
