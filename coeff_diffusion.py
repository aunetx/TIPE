from math import pi

# Constante de Boltzmann
Kb = 1.380649e-23
# Nombre d'Avogadro
Na = 6.02214076e23


def celsius(T_C):
    return 273.15 + T_C


def coeff(T, masse_molaire, masse_volumique, viscosite_dynamique_solvant):
    ri = (3/(4*pi) * (masse_molaire) / (masse_volumique * Na))**(1/3)
    return (Kb * T) / (6*pi * ri * viscosite_dynamique_solvant)


print("Coefficient de diffusion de l'ethanol : C =",
      coeff(celsius(20), 46e-3, 789, 1e-3) * 1e4,
      "cm²/s")
