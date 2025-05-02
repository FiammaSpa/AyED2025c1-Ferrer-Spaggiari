import time
import random
from ordenamiento_burbuja import burbuja
from ordenamiento_quicksort import quicksort
from ordenamiento_por_residuos import radix_sort

# Rangos de prueba
sizes = list(range(1, 1001, 50))
tiempos_burbuja = []
tiempos_quick = []
tiempos_radix = []
#tiempos_sorted = []

for n in sizes:
    datos = [random.randint(10000, 99999) for _ in range(n)]
    for nombre, func, lista_tiempos in [
        ("burbuja", burbuja, tiempos_burbuja),
        ("quicksort", quicksort, tiempos_quick),
        ("radix", radix_sort, tiempos_radix),
        #("sorted", sorted, tiempos_sorted),  
    ]:
        copia = datos.copy()
        inicio = time.time()
        func(copia)
        fin = time.time()
        lista_tiempos.append(fin - inicio)
# Guardar los resultados para graficar
with open("tiempos_resultados.py", "w") as f:
    f.write(f"sizes = {sizes}\n")
    f.write(f"tiempos_burbuja = {tiempos_burbuja}\n")
    f.write(f"tiempos_quick = {tiempos_quick}\n")
    f.write(f"tiempos_radix = {tiempos_radix}\n")
    #f.write(f"tiempos_sorted = {tiempos_sorted}\n")
