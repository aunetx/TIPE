import numpy as np
import matplotlib.pyplot as plt

n = 500
T = 50
X = np.zeros((T, n))
Y = np.zeros((T, n))

# X[0] = np.random.randn(n)
# Y[0] = np.random.randn(n)

for dt in range(1, T):
    X[dt] = X[dt-1] + np.random.randn(n)
    Y[dt] = Y[dt-1] + np.random.randn(n)


def compter(_min, _max, pos):
    return np.logical_and(_min <= pos, pos < _max)


res_x = 20
res_y = 20

l_x = np.linspace(np.amin(X), np.amax(X), res_x)
l_y = np.linspace(np.amin(Y), np.amax(Y), res_y)

pas_x = l_x[1] - l_x[0]
pas_y = l_y[1] - l_y[0]


liste_grilles = []
for t in range(T):
    grille = np.zeros((res_y, res_x))
    for i, x in enumerate(l_x):
        satisfont_x = compter(x, x+pas_x, X[t])
        for j, y in enumerate(l_y):
            satisfont_y = compter(y, y+pas_y, Y[t])
            compte = np.count_nonzero(np.logical_and(satisfont_x, satisfont_y))
            grille[j][i] = compte
    liste_grilles.append(grille)


#! Partie affichage

fig = plt.figure(figsize=(res_y, res_x))
ax = fig.add_subplot(111)
ticks_x = l_x
ticks_y = l_y
ax.set_xticks(ticks_y)
ax.set_yticks(ticks_x)

max_particules = max([np.amax(grille) for grille in liste_grilles])

cmap = plt.get_cmap("gist_yarg")


def correction(x): return np.log10(x)


cax = ax.matshow(
    correction(liste_grilles[0]), vmin=0, vmax=correction(max_particules), cmap=cmap)
fig.colorbar(cax)

for t in range(T):
    plt.cla()
    cax = ax.matshow(
        correction(liste_grilles[t]), vmin=0, vmax=correction(max_particules), cmap=cmap)

    plt.draw()
    plt.pause(0.1)
