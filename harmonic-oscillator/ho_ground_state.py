from harmonic_oscillator import entropy_x, entropy_p


s_x_ground_state = entropy_x(0 ,0.06)
s_p_ground_state = entropy_p(0 ,0.06)
s_t_ground_state = s_x_ground_state + s_p_ground_state

print(round(s_x_ground_state,4))
print(round(s_p_ground_state,4))
print(round(s_t_ground_state,4))