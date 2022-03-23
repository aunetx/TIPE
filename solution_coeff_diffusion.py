import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

N0 = 1
res = 500
x_min = -0.1
x_max = 0.1
t_min = 0.1
t_max = 10
D_min = 1e-6
D_max = 1e-4


def n(x, t, d):
    return N0/(np.sqrt(np.pi*d*t)) * np.exp(-x**2 / (d*t))


ax = plt.axes(projection='3d')

#X = np.outer(np.linspace(x_min, x_max, res), np.ones(res))
x = 0
T = np.outer(np.linspace(t_min, t_max, res), np.ones(res))
D = np.outer(np.linspace(D_min, D_max, res), np.ones(res)).T
N = n(x, T, D)

ax.plot_surface(D, T, N, cmap='viridis', edgecolor='green')
plt.show()
