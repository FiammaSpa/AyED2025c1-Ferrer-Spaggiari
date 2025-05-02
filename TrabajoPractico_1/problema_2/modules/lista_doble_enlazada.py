from nodo import Nodo

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.tamanio == 0

    def __len__(self):
        return self.tamanio

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posición inválida")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamanio += 1

    def extraer(self, posicion=None):
        if posicion is None or posicion == -1:
            posicion = self.tamanio - 1
        if self.esta_vacia():
            raise Exception("La lista está vacía")
        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición inválida")

        if posicion == 0:
            extraido = self.cabeza
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            extraido = self.cola
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            extraido = actual
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

        self.tamanio -= 1
        return extraido.dato

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, otra_lista):
        otra = otra_lista.copiar()  
        if otra.esta_vacia():
            return
        if self.esta_vacia():
            self.cabeza = otra.cabeza
            self.cola = otra.cola
        else:
            self.cola.siguiente = otra.cabeza
            otra.cabeza.anterior = self.cola
            self.cola = otra.cola
            self.tamanio += len(otra)
        if self.cabeza:
            self.cabeza.anterior = None

    def __add__(self, otra_lista):
        if not isinstance(otra_lista, ListaDobleEnlazada):
            raise TypeError("Solo se puede sumar con otra ListaDobleEnlazada")
        nueva = self.copiar()
        nueva.concatenar(otra_lista.copiar())
        return nueva

    def __iter__(self): 
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente
