from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

n = 500
t = 2000
X = np.zeros((t, n))
Y = np.zeros((t, n))

#X[0] = np.random.randn(n)
#Y[0] = np.random.randn(n)

# X = tableau des positions en x des particules pour chaque temps

for dt in range(1, t):
    X[dt] = X[dt-1] + np.random.randn(n)
    Y[dt] = Y[dt-1] + np.random.randn(n)


def compter(_min, _max, pos):
    return np.logical_and(_min <= pos, pos < _max)


t = 1999

res_x = 20
res_y = 20

l_x = np.linspace(min(X[t]), max(X[t]), res_x)
l_y = np.linspace(min(Y[t]), max(Y[t]), res_y)

pas_x = l_x[1] - l_x[0]
pas_y = l_y[1] - l_y[0]


a = 0
grille = np.zeros((res_y, res_x))
for i, x in enumerate(l_x):
    satisfont_x = compter(x, x+pas_x, X[t])
    for j, y in enumerate(l_y):
        satisfont_y = compter(y, y+pas_y, Y[t])
        compte = np.count_nonzero(np.logical_and(satisfont_x, satisfont_y))
        grille[j][i] = compte
        a += compte

print(grille)
print("Total =", a)

fig = plt.figure(figsize=(res_y, res_x))
ax = fig.add_subplot(111)
cax = ax.matshow(grille, vmin=np.amin(grille), vmax=np.amax(grille))
fig.colorbar(cax)
ticks_x = np.arange(0, res_y, 1)
ticks_y = np.arange(0, res_x, 1)
ax.set_xticks(ticks_y)
ax.set_yticks(ticks_x)

#plt.plot(X[t:t+2], Y[t:t+2])
plt.show()
