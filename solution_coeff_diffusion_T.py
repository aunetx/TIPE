import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

res = 1000
x_min = 0
x_max = 0.003
t_min = 0.1
t_max = 1000
T_min = 285
T_max = 375

N0 = 1
k = 1.38e-23
V = 46e-3 / 0.789
r_i = 1/2 * (V/6 * 1e-23)**(1/3)
mu_j = 1e-3


def n(x, t, d):
    return N0/(np.sqrt(np.pi*d*t)) * np.exp(-x**2 / (d*t))


def Diff(Temp):
    return k*Temp / (6*np.pi*r_i*mu_j)


ax = plt.axes(projection='3d')

print(Diff(300))

t = 1000

X = np.outer(np.linspace(x_min, x_max, res), np.ones(res))
#T = np.outer(np.linspace(t_min, t_max, res), np.ones(res))
Temp = np.outer(np.linspace(T_min, T_max, res), np.ones(res)).T
D = Diff(Temp)
N = n(X, t, D)

ax.plot_surface(Temp, X, N, cmap='viridis', edgecolor='green')
plt.show()
