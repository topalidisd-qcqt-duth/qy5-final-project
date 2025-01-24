import matplotlib.pyplot as plt
from infinite_square_well import calc_entropy_x, calc_entropy_p

def plot_entropies():
    
    widths = [0.05,0.1,0.15,0.2,0.25,0.5,2,4,6,8,10]

    entropy_x_values_first_excited_state = [calc_entropy_x(2, L) for L in widths]
    entropy_p_values_ground_state = [calc_entropy_p(1, L) for L in widths]
    entropy_p_values_first_excited_state = [calc_entropy_p(2, L) for L in widths]
    entropy_p_values_second_excited_state = [calc_entropy_p(3, L) for L in widths]


    plt.figure(figsize=(10, 5))
    plt.plot(widths, entropy_x_values_first_excited_state, marker="s", linestyle='-', label='Sx (n=2)')
    plt.plot(widths, entropy_p_values_ground_state, marker="o",linestyle='-', label='Sp (n=1)')
    plt.plot(widths, entropy_p_values_first_excited_state, marker="s", linestyle='-', label='Sp (n=2)')
    plt.plot(widths, entropy_p_values_second_excited_state, marker="D", linestyle='-', label='Sp (n=3)')
    plt.xlabel('L (a.u.)', fontsize=12)
    plt.ylabel('Sx, Sp', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()    
 
def plot_total_entropy():
    
    widths = [0.05,0.1,0.15,0.2,0.25,0.5,2,4,6,8,10]

    entropy_t_values_ground_state = [calc_entropy_x(1, L)+calc_entropy_p(1, L) for L in widths]
    entropy_t_values_first_excited_state = [calc_entropy_x(2, L) +calc_entropy_p(2, L) for L in widths]
    entropy_t_values_second_excited_state = [calc_entropy_x(3, L)+calc_entropy_p(3, L) for L in widths]


    plt.figure(figsize=(10, 5))

    plt.plot(widths, entropy_t_values_ground_state, marker="o",linestyle='-', label='n=1')
    plt.plot(widths, entropy_t_values_first_excited_state, marker="s", linestyle='-', label='n=2')
    plt.plot(widths, entropy_t_values_second_excited_state, marker="D", linestyle='-', label='n=3')
    plt.xlabel('L (a.u.)', fontsize=12)
    plt.ylabel('St', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()    
 

plot_entropies()
plot_total_entropy()
