import numpy as np
import matplotlib.pyplot as plt

n = 5000
t = 2000
X = np.random.randn(n)
Y = np.random.randn(n)


# X = tableau des positions en x des particules pour chaque temps

for dt in range(1, t):
    X += np.random.randn(n)
    Y += np.random.randn(n)

heatmap, xedges, yedges = np.histogram2d(X, Y, bins=50)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.scatter(X, Y, s=0.1)
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.show()
