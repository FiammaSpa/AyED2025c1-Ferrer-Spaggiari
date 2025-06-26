class ColaPrioridad:
    """
    Implementa una cola de prioridad utilizando un montículo binario (min-heap) implementado manualmente.
    
    """
    def __init__(self, funcion_prioridad):
        self.elementos_en_cola = []
        self.contador = 0  #Para desempatar elementos 
        self.funcion_prioridad = funcion_prioridad #Función para obtener la prioridad del elemento

    def _obtener_indice_padre(self, indice):
        """Calcula y retorna el indice del nodo padre"""
        return (indice - 1) // 2

    def _obtener_indice_hijo_izquierdo(self, indice):
        """Calcula y retorna el indice del nodo hijo izquierdo"""
        return 2 * indice + 1

    def _obtener_indice_hijo_derecho(self, indice):
        """Calcula y retorna el indice del nodo hijo derecho"""
        return 2 * indice + 2

    def _subir(self, indice):
        """Mueve el elemento en 'indice' hacia arriba en el monticulo si su prioridad es menor que la del padre."""
        while indice > 0 and self.elementos_en_cola[indice] < self.elementos_en_cola[self._obtener_indice_padre(indice)]:
            indice_padre = self._obtener_indice_padre(indice)
            # Intercambiar el elemento actual con su padre
            self.elementos_en_cola[indice], self.elementos_en_cola[indice_padre] = \
                self.elementos_en_cola[indice_padre], self.elementos_en_cola[indice]
            indice = indice_padre

    def _bajar(self, indice):
        """Mueve el elemento en 'indice' hacia abajo en el monticulo si su prioridad es mayor que la de alguno de sus hijos,"""
        tamano_cola = len(self.elementos_en_cola)
        while True:
            indice_hijo_izquierdo = self._obtener_indice_hijo_izquierdo(indice)
            indice_hijo_derecho = self._obtener_indice_hijo_derecho(indice)
            indice_menor = indice

            # Comparamos con el hijo izquierdo para encontrar el menor
            if indice_hijo_izquierdo < tamano_cola and \
               self.elementos_en_cola[indice_hijo_izquierdo] < self.elementos_en_cola[indice_menor]:
                indice_menor = indice_hijo_izquierdo

            # Comparamos con el hijo derecho para encontrar el menor 
            if indice_hijo_derecho < tamano_cola and \
               self.elementos_en_cola[indice_hijo_derecho] < self.elementos_en_cola[indice_menor]:
                indice_menor = indice_hijo_derecho

            # Si el elemento de menor prioridad no es el actual -> realizamos un intercambio
            if indice_menor != indice:
                self.elementos_en_cola[indice], self.elementos_en_cola[indice_menor] = \
                    self.elementos_en_cola[indice_menor], self.elementos_en_cola[indice]
                indice = indice_menor
            else:
                break

    def insertar(self, elemento):
        """ Inserta un elemento en la cola de prioridad.  """
        prioridad = self.funcion_prioridad(elemento)
        self.elementos_en_cola.append((prioridad, self.contador, elemento))
        self.contador += 1
        self._subir(len(self.elementos_en_cola) - 1)

    def extraer(self):
        """Extrae y retorna el elemento de mayor prioridad de la cola."""
        if not self.elementos_en_cola:
            return None

        # Si solo hay un elemento, lo sacamos directamente
        if len(self.elementos_en_cola) == 1:
            return self.elementos_en_cola.pop()[2] 
        
        # Intercambiar el elemento de mayor prioridad con el ultimo elemento
        self.elementos_en_cola[0], self.elementos_en_cola[-1] = \
            self.elementos_en_cola[-1], self.elementos_en_cola[0]

        # Eliminar y guardar el elemento de mayor prioridad 
        elemento_extraido = self.elementos_en_cola.pop()[2] 

        self._bajar(0)

        return elemento_extraido

    def esta_vacia(self):
        """Verifica si la cola de prioridad esta vacia"""
        return len(self.elementos_en_cola) == 0

    def obtener_elementos(self):
        """Retorna una lista con todos los elementos originales presentes en la cola de prioridad
        sin alterar el orden interno de la cola."""
        return [x[2] for x in self.elementos_en_cola]