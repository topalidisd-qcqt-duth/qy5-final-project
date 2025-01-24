from harmonic_oscillator import entropy_x, entropy_p


s_x_second_excited_state = entropy_x(2 ,0.06)
s_p_second_excited_state = entropy_p(2 ,0.06)
s_t_second_excited_state = s_x_second_excited_state + s_p_second_excited_state

print(round(s_x_second_excited_state,4))
print(round(s_p_second_excited_state,4))
print(round(s_t_second_excited_state,4))