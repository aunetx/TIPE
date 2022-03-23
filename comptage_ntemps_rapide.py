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
ax = plt.axes()
plt.axis('equal')

max_particules = max([np.amax(heatmap) for heatmap in heatmaps])

ax.set_xlim(np.amin(X), np.amax(X))
ax.set_ylim(np.amin(Y), np.amax(Y))
sc = ax.scatter(X[0], Y[0], s=0.1)
im = ax.imshow(np.log10(heatmaps[0].T), extent=extents[0],
               origin='lower', cmap='gist_yarg')
plt.colorbar(im)


def init():
    sc.set_offsets(np.c_[X[0], Y[0]])
    im.set_data(heatmaps[0].T)
    im.set_extent(extents[0])
    return [sc, im]


def update(i, sc, im, heatmaps, extents, X, Y):
    sc.set_offsets(np.c_[X[i], Y[i]])
    im.set_data(np.log10(heatmaps[i].T))
    im.set_extent(extents[i])
    return [sc, im]


anim = animation.FuncAnimation(
    fig, update, init_func=init, fargs=(
        sc, im, heatmaps, extents, X, Y), interval=1, frames=t,
    blit=True, repeat=False)
plt.show()
