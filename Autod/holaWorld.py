print ("Hola mundo")

import time

inicio = time.perf_counter()
# Código a medir
for _ in range(1000000):
    pass
fin = time.perf_counter()

print(f"Tiempo transcurrido: {fin - inicio:.9f} segundos")
