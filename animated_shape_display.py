# Written by ChatGPT 3.5. 11/21.


import matplotlib.pyplot as plt
import numpy as np
from time import sleep
# from shifting_surface_code import generate_coordinates, Patch


# test_edge_data = [[3, +1], [3, -1], [2, -1], [3, +1], [3, +1], [3, -1],
#                   [2, -1], [3, +1], [3, +1], [8, +1], [13, +1], [8, +1]]
#
# init_shape_x_pos, init_shape_y_pos, init_shape_x_dir, init_shape_y_dir = generate_coordinates(test_edge_data)
#
# P = Patch(test_edge_data)
#
# P.scale_up()
#
# scaled_shape_x_pos, scaled_shape_y_pos, scaled_shape_x_dir, scaled_shape_y_dir = generate_coordinates(P.generate_edge_data())


def plot_quiver(x_pos, y_pos, x_dir, y_dir, initial_data_plot, label, pause_time=0.2):
    plt.clf()
    plt.quiver(initial_data_plot[0], initial_data_plot[1], initial_data_plot[2], initial_data_plot[3],
               scale=40, label=label, color="blue")  # plot initial data
    plt.quiver(x_pos, y_pos, x_dir, y_dir, scale=40, label=label)
    # plt.xlabel('X-axis')
    # plt.ylabel('Y-axis')
    plt.title('Patch Scaling')
    plt.legend()
    plt.axis([-5, 35, -20, 20])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.pause(pause_time)

#
# plot_quiver(init_shape_x_pos, init_shape_y_pos, init_shape_x_dir, init_shape_y_dir, label='Data')
#
# plot_quiver(scaled_shape_x_pos, scaled_shape_y_pos, scaled_shape_x_dir, scaled_shape_y_dir, label='New Data')
#
# plt.show()
