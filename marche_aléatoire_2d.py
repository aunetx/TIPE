from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

n = 3
t = 1000
x = np.zeros((t, n))
y = np.zeros((t, n))

#x[0] = np.random.randn(n)
#y[0] = np.random.randn(n)

for dt in range(1, t):
    x[dt] = x[dt-1] + np.random.randn(n)
    y[dt] = y[dt-1] + np.random.randn(n)

plt.plot(x, y)
plt.show()
