import matplotlib.pyplot as plt

from tiempos import (
    sizes,
    tiempos_burbuja,
    tiempos_quick,
    tiempos_radix,
   # tiempos_sorted
    
)

plt.figure(figsize=(10, 6))
plt.plot(sizes, tiempos_burbuja, label="Burbuja", color="red")
plt.plot(sizes, tiempos_quick, label="Quicksort", color="blue")
plt.plot(sizes, tiempos_radix, label="Radix Sort", color="green")
#plt.plot(sizes, tiempos_sorted, label="sorted() (Timsort)", color="purple")

plt.xlabel("Tamaño de lista")
plt.ylabel("Tiempo de ejecución (s)")
plt.title("Comparación de algoritmos de ordenamiento")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
