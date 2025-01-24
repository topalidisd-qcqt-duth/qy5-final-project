from infinite_square_well import calc_entropy_x, calc_entropy_p


s_x_first_excited_state = calc_entropy_x(2 ,0.05)
s_p_first_excited_state = calc_entropy_p(2 ,0.05)
s_t_first_excited_state = s_x_first_excited_state + s_p_first_excited_state

print(round(s_x_first_excited_state,4))
print(round(s_p_first_excited_state,4))
print(round(s_t_first_excited_state,4))