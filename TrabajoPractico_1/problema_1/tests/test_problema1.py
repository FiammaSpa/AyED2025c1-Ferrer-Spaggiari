import random
from modules.ordenamiento_burbuja import burbuja
from modules.ordenamiento_quicksort import quicksort
from modules.ordenamiento_por_residuos import radix_sort

def test_algoritmos_ordenamiento():
    lista = [random.randint(10000, 99999) for _ in range(500)]
    esperado = sorted(lista)

    resultado_burbuja = burbuja(lista.copy())
    assert resultado_burbuja == esperado, "ERROR en burbuja"

    resultado_quick = quicksort(lista.copy())
    assert resultado_quick == esperado, "ERROR en quicksort"

    copia_radix = lista.copy()
    radix_sort(copia_radix)
    assert copia_radix == esperado, "ERROR en radix_sort"

    print("Todos los algoritmos pasaron la prueba.")

if __name__ == '__main__':
    test_algoritmos_ordenamiento()
