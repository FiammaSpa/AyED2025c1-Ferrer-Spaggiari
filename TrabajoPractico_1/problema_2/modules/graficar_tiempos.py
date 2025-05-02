import time
import matplotlib.pyplot as plt
from lista_doble_enlazada import ListaDobleEnlazada

def medir_tiempos(max_n, paso):
    ns = list(range(paso, max_n + 1, paso))
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    for n in ns:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(i)

        # Medir len()
        inicio = time.time()
        _ = len(lista)
        tiempos_len.append(time.time() - inicio)

        # Medir copiar()
        inicio = time.time()
        _ = lista.copiar()
        tiempos_copiar.append(time.time() - inicio)

        # Medir invertir()
        inicio = time.time()
        lista.invertir()
        tiempos_invertir.append(time.time() - inicio)

    return ns, tiempos_len, tiempos_copiar, tiempos_invertir

def graficar(ns, tiempos_len, tiempos_copiar, tiempos_invertir):
    plt.figure(figsize=(10, 6))
    plt.plot(ns, tiempos_len, label="len() - O(1)", marker='o')
    plt.plot(ns, tiempos_copiar, label="copiar() - O(n)", marker='s')
    plt.plot(ns, tiempos_invertir, label="invertir() - O(n)", marker='^')
    plt.xlabel("Cantidad de elementos (N)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Rendimiento de métodos sobre ListaDobleEnlazada")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ns, tiempos_len, tiempos_copiar, tiempos_invertir = medir_tiempos(max_n=50000, paso=5000)
    graficar(ns, tiempos_len, tiempos_copiar, tiempos_invertir)
