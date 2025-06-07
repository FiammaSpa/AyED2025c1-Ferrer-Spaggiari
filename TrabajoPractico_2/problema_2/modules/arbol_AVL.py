from nodo_AVL import NodoAVL 

class arbolAVL:
    """
    Implementacion generica de un árbol AVL.
    Permite insertar, eliminar y buscar elementos, manteniendo el arbol balanceado.
    """
    def __init__(self):
        self._raiz = None 

    @property
    def raiz(self):
        """
        Obtiene y retorna la raiz del arbol AVL.
        """
        return self._raiz

    @raiz.setter
    def raiz(self, nuevo_nodo):
        """
        Establece la raiz del arbol AVL.
        """
        self._raiz = nuevo_nodo

    def _altura(self, nodo):
        """
        Metodo auxiliar para obtener y retornar la altura de un nodo.
        """
        if not nodo: #Si el nodo es None, su altura es 0
            return 0
        return nodo.altura 

    def _actualizar_altura(self, nodo):
        """
        Actualiza la altura de un nodo basandose en las alturas de sus hijos.
        """
        if nodo:
            nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

    def _obtener_balance(self, nodo):
        """
        Calcula y retorna el factor de balance de un nodo.
        """
        if not nodo:
            return 0
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)
    
    def _rotar_derecha(self, y):
        """
        Realiza una rotacion simple a la derecha y retorna la raiz del subarbol despues de la rotacion.
        """
        x = y.izquierda 
        T2 = x.derecha 
        # Realizar rotación 
        x.derecha = y
        y.izquierda = T2
        # Actualizar alturas
        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x 

    def _rotar_izquierda(self, x):
        """
        Realiza una rotacion simple a la izquierda y retorna la raiz del subarbol despues de la rotacion.
        """
        y = x.derecha   
        T2 = y.izquierda 
        # Realizar rotación 
        y.izquierda = x
        x.derecha = T2
        # Actualizar alturas
        self._actualizar_altura(x)
        self._actualizar_altura(y)
        return y 

    
    def insertar(self, clave, valor):
        """
        Inserta un nuevo par clave-valor en el arbol AVL, si la clave ya existe actualiza su valor asociado.
        El arbol se rebalancea automáticamente.
        """
        self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo_actual, clave, valor):
        """
        Metodo auxiliar recursivo para insertar un nodo y rebalancear el subarbol.
        """
        if not nodo_actual:
            return NodoAVL(clave, valor) #Si el nodo actual es None, crea y devuelve el nuevo nodo.

        if clave < nodo_actual.clave:
            nodo_actual.izquierda = self._insertar(nodo_actual.izquierda, clave, valor)
        elif clave > nodo_actual.clave:
            nodo_actual.derecha = self._insertar(nodo_actual.derecha, clave, valor)
        else:
            nodo_actual.valor = valor #Si la clave ya existe, actualizamos su valor.
            return nodo_actual 
        
        self._actualizar_altura(nodo_actual)
        balance = self._obtener_balance(nodo_actual)

        #El arbol puede desbalancearse por 4 tipos de inserciones:
        # Caso 1: Desbalance Izquierda-Izquierda (LL)
        if balance > 1 and clave < nodo_actual.izquierda.clave:
            return self._rotar_derecha(nodo_actual)
        # Caso 2: Desbalance Derecha-Derecha (RR)
        if balance < -1 and clave > nodo_actual.derecha.clave:
            return self._rotar_izquierda(nodo_actual)
        # Caso 3: Desbalance Izquierda-Derecha (LR)
        if balance > 1 and clave > nodo_actual.izquierda.clave:
            nodo_actual.izquierda = self._rotar_izquierda(nodo_actual.izquierda)
            return self._rotar_derecha(nodo_actual)
        # Caso 4: Desbalance Derecha-Izquierda (RL)
        if balance < -1 and clave < nodo_actual.derecha.clave:
            nodo_actual.derecha = self._rotar_derecha(nodo_actual.derecha)
            return self._rotar_izquierda(nodo_actual)
        
        return nodo_actual
    
    def eliminar(self, clave):
        """
        Elimina un nodo con la clave especificada del arbol AVL.
        El arbol se rebalancea automáticamente.
        """
        self.raiz = self._eliminar(self.raiz, clave)

    def _eliminar(self, nodo_actual, clave):
        """
        Metodo auxiliar recursivo para eliminar un nodo y rebalancear el subarbol.
        """
        if not nodo_actual:
            return nodo_actual

        if clave < nodo_actual.clave:
            nodo_actual.izquierda = self._eliminar(nodo_actual.izquierda, clave)
        elif clave > nodo_actual.clave:
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, clave)
        else:
            # Caso A: El nodo tiene 0 o 1 hijo
            if nodo_actual.izquierda is None:
                temp = nodo_actual.derecha
                nodo_actual = None
                return temp
            elif nodo_actual.derecha is None:
                temp = nodo_actual.izquierda
                nodo_actual = None 
                return temp 

            # Caso B: El nodo tiene 2 hijos
            nodo_min_valor = self._obtener_nodo_min_valor(nodo_actual.derecha)
            nodo_actual._clave = nodo_min_valor.clave
            nodo_actual._valor = nodo_min_valor.valor
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, nodo_min_valor.clave)

        if nodo_actual is None:
            return nodo_actual
        
        self._actualizar_altura(nodo_actual)

        balance = self._obtener_balance(nodo_actual)

        #Balance
        if balance > 1 and self._obtener_balance(nodo_actual.izquierda) >= 0:
            return self._rotar_derecha(nodo_actual)
        
        if balance > 1 and self._obtener_balance(nodo_actual.izquierda) < 0:
            nodo_actual.izquierda = self._rotar_izquierda(nodo_actual.izquierda)
            return self._rotar_derecha(nodo_actual)
        
        if balance < -1 and self._obtener_balance(nodo_actual.derecha) <= 0:
            return self._rotar_izquierda(nodo_actual)
        
        if balance < -1 and self._obtener_balance(nodo_actual.derecha) > 0:
            nodo_actual.derecha = self._rotar_derecha(nodo_actual.derecha)
            return self._rotar_izquierda(nodo_actual)
        
        return nodo_actual

    def _obtener_nodo_min_valor(self, nodo):
        """
        Encuentra y retorna el nodo con el valor de clave minimo en un subarbol dado (nodo mas a la izquierda del subarbol)
        """
        if nodo is None or nodo.izquierda is None:
            return nodo
        return self._obtener_nodo_min_valor(nodo.izquierda)

    def buscar(self, clave):
        """
        Busca y retorna un nodo con la clave especificada en el arbol AVL.
        """
        return self._buscar(self.raiz, clave)

    def _buscar(self, nodo, clave):
        """
        Metodo auxiliar recursivo para buscar un nodo por clave.
        """
        if not nodo or nodo.clave == clave:
            return nodo
       
        if clave < nodo.clave:
            return self._buscar(nodo.izquierda, clave) 
        return self._buscar(nodo.derecha, clave) 

    def _inorder_rango(self, nodo, clave_inicio, clave_fin, resultados):
        """
        Realiza un recorrido in-order en el arbol para encontrar y recolectar
        pares (clave, valor) dentro de un rango de claves especificado.
        """
        if not nodo:
            return

        if clave_inicio < nodo.clave:
            self._inorder_rango(nodo.izquierda, clave_inicio, clave_fin, resultados) 

        if clave_inicio <= nodo.clave <= clave_fin:
            resultados.append((nodo.clave, nodo.valor))

        if clave_fin > nodo.clave:
            self._inorder_rango(nodo.derecha, clave_inicio, clave_fin, resultados) 
    def obtener_nodos_en_rango(self, clave_inicio, clave_fin):
        """
        Obtiene una lista de todos los pares (clave, valor) cuyos claves
        caen dentro del rango especificado (inclusive).
        """
        resultados = []
        self._inorder_rango(self.raiz, clave_inicio, clave_fin, resultados) 
        return resultados

    def _encontrar_min_valor_en_rango(self, nodo, clave_inicio, clave_fin, valor_min_actual):
        """
        Método auxiliar recursivo para encontrar el valor minimo dentro de un rango de claves.
        """
        if not nodo:
            return valor_min_actual

        if clave_inicio < nodo.clave:
            valor_min_actual = self._encontrar_min_valor_en_rango(nodo.izquierda, clave_inicio, clave_fin, valor_min_actual) 

        if clave_inicio <= nodo.clave <= clave_fin:
            valor_min_actual = min(valor_min_actual, nodo.valor)

        if clave_fin > nodo.clave:
            valor_min_actual = self._encontrar_min_valor_en_rango(nodo.derecha, clave_inicio, clave_fin, valor_min_actual) 

        return valor_min_actual

    def obtener_min_valor_en_rango(self, clave_inicio, clave_fin):
        """
        Obtiene el valor minimo entre todas las claves dentro de un rango especificado
        """
        return self._encontrar_min_valor_en_rango(self.raiz, clave_inicio, clave_fin, float('inf')) 


    def _encontrar_max_valor_en_rango(self, nodo, clave_inicio, clave_fin, valor_max_actual):
        """
        Metodo auxiliar recursivo para encontrar el valor maximo dentro de un rango de claves.
        """
        if not nodo:
            return valor_max_actual

        if clave_fin > nodo.clave:
            valor_max_actual = self._encontrar_max_valor_en_rango(nodo.derecha, clave_inicio, clave_fin, valor_max_actual) 

        if clave_inicio <= nodo.clave <= clave_fin:
            valor_max_actual = max(valor_max_actual, nodo.valor)

        if clave_inicio < nodo.clave:
            valor_max_actual = self._encontrar_max_valor_en_rango(nodo.izquierda, clave_inicio, clave_fin, valor_max_actual) 

        return valor_max_actual

    def obtener_max_valor_en_rango(self, clave_inicio, clave_fin):
        """
        Obtiene el valor maximo entre todas las claves dentro de un rango especificado.
        """
        return self._encontrar_max_valor_en_rango(self.raiz, clave_inicio, clave_fin, float('-inf')) 