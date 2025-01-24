from infinite_square_well import calc_entropy_x, calc_entropy_p


s_x_ground_state = calc_entropy_x(1,0.05)
s_p_ground_state = calc_entropy_p(1,0.05)
s_t_ground_state = s_x_ground_state + s_p_ground_state

print(round(s_x_ground_state,4))
print(round(s_p_ground_state,4))
print(round(s_t_ground_state,4))