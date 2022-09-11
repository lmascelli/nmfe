import numpy as np
import matplotlib.pyplot as plt

root1 = 1
root2 = -1 / 2 + 1j * np.sqrt(3) / 2
root3 = -1 / 2 - 1j * np.sqrt(3) / 2

nx = 1000
ny = 1000
xmin = -2
xmax = 2
ymin = -2
ymax = 2

x = np.linspace(xmin, xmax, nx)
y = np.linspace(ymin, ymax, ny)
X, Y = np.meshgrid(x, y)

Z = X + 1j * Y


def f(x):
    return np.power(x, 3) - 1


def fp(x):
    return 3 * np.power(x, 2)


for i in range(40):
    Z -= f(Z) / fp(Z)

eps = 1e-3
Z1 = np.abs(Z - root1) < eps
Z2 = np.abs(Z - root2) < eps
Z3 = np.abs(Z - root3) < eps
Z4 = np.logical_not(Z1 + Z2 + Z3)
map_colors = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
cmap = plt.cm.colors.ListedColormap(map_colors)

Z = Z1 + 2 * Z2 + 3 * Z3 + 4 * Z4
plt.imshow(Z, cmap=cmap, origin="lower")
plt.show()
