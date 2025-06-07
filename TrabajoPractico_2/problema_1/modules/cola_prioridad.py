import heapq

class ColaPrioridad:
    """
        Implementa una cola de prioridad utilizando un heap binario (min-heap).
        Permite insertar elementos con una prioridad asociada y extraer el elemento de mayor prioridad.
        Sus atributos son cola (lista que representa el heap binario), contador y funcion_prioridad.
    """
    def __init__(self, funcion_prioridad):
        self.cola = []
        self.contador = 0  #Para desempatar por orden de llegada
        self.funcion_prioridad = funcion_prioridad

    def insertar(self, elemento):
        """
            Inserta un elemento en la cola de prioridad y utiliza un contador para desempatar elementos
            con la misma prioridad.
        """
        prioridad = self.funcion_prioridad(elemento)
        heapq.heappush(self.cola, (prioridad, self.contador, elemento))
        self.contador += 1

    def extraer(self):
        """
            Extrae y retorna el elemento de mayor prioridad de la cola.
        """
        if self.cola:
            return heapq.heappop(self.cola)[2]
        return None

    def esta_vacia(self):   #Verifica si la cola de prioridad esta vacia.
        return len(self.cola) == 0

    def elementos(self):
        """
            Retorna una lista con todos los elementos en la cola de prioridad sin alterar el orden interno 
            de la cola.
        """
        return [x[2] for x in self.cola]
