import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

#! Partie calculs

res = 9
T = 15

concentration = np.zeros((res, res))
concentration[res//2][res//2] = 100.
vitesse = np.zeros((res, res))

concentrations_par_temps = []
for dt in range(T):
    concentrations_par_temps.append(deepcopy(concentration))

    for i, ligne in enumerate(concentration):
        for j in range(len(ligne)):
            if i < res-1 and j < res-1:
                concentration[i][j] = concentrations_par_temps[dt][i][j] * \
                    0.95 + concentrations_par_temps[dt][i+1][j+1]*0.05

concentrations_par_temps.append(deepcopy(concentration))


#! Partie affichage

fig = plt.figure(figsize=(res, res))
ax = fig.add_subplot(111)

max_concentration = max([np.amax(c) for c in concentrations_par_temps])

cmap = plt.get_cmap("gist_yarg")

cax = ax.matshow(
    concentration, vmin=0, vmax=max_concentration, cmap=cmap)
fig.colorbar(cax)


for t in range(T):
    cax = ax.matshow(
        concentrations_par_temps[t], vmin=0, vmax=max_concentration, cmap=cmap)

    plt.draw()
    plt.pause(1)
