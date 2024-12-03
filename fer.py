import numpy as np

# Definir las ecuaciones diferenciales
def dc_dt(C, Z):
    return 0.1 * C - 0.02 * C * Z

def dZ_dt(C, Z):
    return -0.3 * Z + 0.01 * C * Z

# Definir los parámetros y condiciones iniciales
a = 0.1
b = 0.02
c = 0.3
d = 0.01
t = np.linspace(0, 50, 1000)  # Tiempo de 0 a 50 unidades de tiempo
C0 = 40  # Población inicial de conejos
Z0 = 9  # Población inicial de zorros

# Resolver las ecuaciones diferenciales numéricamente
dt = t[1] - t[0]
C, Z = [C0], [Z0]
for i in range(1, len(t)):
    dC = dc_dt(C[-1], Z[-1]) * dt
    dZ = dZ_dt(C[-1], Z[-1]) * dt
    C.append(C[-1] + dC)
    Z.append(Z[-1] + dZ)

# Mostrar los resultados
print("Tiempo\tPoblación de Conejos\tPoblación de Zorros")
for i in range(len(t)):
    print(f"{t[i]}\t{C[i]}\t{Z[i]}")