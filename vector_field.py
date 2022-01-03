import matplotlib.pyplot as plt
import numpy as np
from scipy import sparse

taille = (8, 10)

"""
Pour 2 dimension, ex. taille = (8, 10)

Une matrice de taille 2×8×10.
- le premier axe (longueur 2) représente chaque dimension : x, y
- le second axe et troisième axe (longueur 8×10) représente la norme du vecteur vitesse
  dans la direction donnée

Les cellules sur lesquelles s'appliquent cette matrice sont supposées réparties uniformément.
"""
vitesse = np.zeros((len(taille), *taille))

x = np.linspace(0, 1, taille[0], endpoint=False)
y = np.linspace(0, 1, taille[1], endpoint=False)
X, Y = np.meshgrid(x, y, indexing='ij')


def show_2d_vector_field(field, X, Y, name="Vector field"):
    plt.quiver(X, Y, field[0], field[1], color='b', units='xy', scale=1)
    plt.title(name)

    plt.grid()
    plt.show()


def build_grad(N):
    # builds N-1 x N finite difference matrix
    data = np.array([-np.ones(N), np.ones(N-1)])
    return sparse.diags(data, np.array([0, 1]), shape=(N-1, N))


print(build_grad(10))

show_2d_vector_field(vitesse, X, Y)
