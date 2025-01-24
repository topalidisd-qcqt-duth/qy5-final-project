from infinite_square_well import calc_entropy_x, calc_entropy_p


s_x_second_excited_state = calc_entropy_x(3 ,0.05)
s_p_second_excited_state = calc_entropy_p(3 ,0.05)
s_t_second_excited_state = s_x_second_excited_state + s_p_second_excited_state

print(round(s_x_second_excited_state,4))
print(round(s_p_second_excited_state,4))
print(round(s_t_second_excited_state,4))