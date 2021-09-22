import numpy as np
import matplotlib.pyplot as plt


# Distribution des températures en fonction de la profondeur
# https://www.futura-sciences.com/sciences/dossiers/physique-milieu-marin-proprietes-physiques-416/page/8/
def temperature(x):
    return 13. + 4.5 / (1 + np.exp((x - 80)/9.))


X = np.linspace(0, 200, 400)
Y = temperature(X)
plt.plot(X, Y)
plt.grid(True)
plt.show()
