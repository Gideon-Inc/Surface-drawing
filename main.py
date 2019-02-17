from stl_tools import numpy2stl
import numpy as np


def build_surface(x, y):
    #output = x^3 + y^3 - 9 x y
    output = x*x*x + y*y*y - 9*x*y
    if output < -500:
        return -500
    else:
        return output


z_array = np.zeros((300, 260))

for y in range(-130, 130, 1):
    line_of_z_values = []
    for x in range(-150, 150, 1):
        z_array[x + 150][y + 130] = build_surface(x / 10, y / 10)

numpy2stl(z_array, "my_surfac1e.stl", scale=0.05, mask_val=5., solid=True)
