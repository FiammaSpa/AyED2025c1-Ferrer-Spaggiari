class NodoAVL:
    """
    Representa un nodo en un arbol AVL. Cada nodo almacena una clave y un valor.
    """
    def __init__(self, clave, valor):
        self._clave = clave  
        self._valor = valor  
        self._izquierda = None 
        self._derecha = None   
        self._altura = 1      
    @property 
    def clave(self):
        """
        Obtiene y rotorna la clave del nodo.
        """
        return self._clave
    # La clave (self._clave) no tiene un setter porque no cambia una vez que el nodo es creado

    @property
    def valor(self):
        """
        Obtiene y rotorna el valor del nodo.
        """
        return self._valor 
    @valor.setter
    def valor(self, nuevo_valor):
        """
        Establece un nuevo valor para el nodo.
        """
        self._valor = nuevo_valor

    @property
    def izquierda(self):
        """
        Obtiene y retorna el nodo hijo izquierdo.
        """
        return self._izquierda
    @izquierda.setter
    def izquierda(self, nuevo_nodo):
        """
        Establece el nodo hijo izquierdo.
        """
        self._izquierda = nuevo_nodo

    @property
    def derecha(self):
        """
        Obtiene y retorna el nodo hijo derecho.
        """
        return self._derecha 
    @derecha.setter
    def derecha(self, nuevo_nodo):
        """
        Establece el nodo hijo derecho.
        """
        self._derecha = nuevo_nodo

    @property
    def altura(self):
        """
        Obtiene y retorna la altura.
        """
        return self._altura
    @altura.setter
    def altura(self, nueva_altura):
        """
        Establece una nueva altura para el nodo.
        """
        self._altura = nueva_altura

   
 