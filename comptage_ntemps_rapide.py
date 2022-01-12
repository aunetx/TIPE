import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

res = 50
n = 1500
t = 500
X = np.zeros((t, n))
Y = np.zeros((t, n))

# X = tableau des positions en x des particules pour chaque temps

"""
Mouvement brownien pour chaque temps
"""
for dt in range(1, t):
    X[dt] = X[dt-1] + np.random.randn(n)
    Y[dt] = Y[dt-1] + np.random.randn(n)

"""
Calcul des concentrations pour chaque case
"""
heatmaps = []
extents = []
for dt in range(0, t):
    heatmap, xedges, yedges = np.histogram2d(X[dt], Y[dt], bins=res)
    extents.append([xedges[0], xedges[-1], yedges[0], yedges[-1]])
    heatmaps.append(heatmap)

"""
Affichage avec matplotlib
"""

fig = plt.figure(figsize=(res, res))
ax = fig.add_subplot(111)
plt.axis('equal')

max_particules = max([np.amax(heatmap) for heatmap in heatmaps])
norm = plt.Normalize(vmin=0, vmax=max_particules)

ax.set_xlim(np.amin(X), np.amax(X))
ax.set_ylim(np.amin(Y), np.amax(Y))
#sc = ax.scatter(X[dt], Y[dt], s=0.1)
im = ax.imshow(heatmaps[dt].T, extent=extents[dt],
               origin='lower', cmap='gist_yarg')
plt.colorbar(im)

for dt in range(1, t):
    #sc.set_offsets(np.c_[X[dt], Y[dt]])
    im.set_data(heatmaps[dt].T)
    im.set_extent(extents[dt])

    fig.canvas.draw_idle()
    plt.pause(0.05)
