from modules.lista_doble_enlazada import ListaDobleEnlazada

class DequeEmptyError(Exception):
    """Excepción lanzada al intentar sacar una carta de un mazo vacío."""
    pass

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()

    def __len__(self):
        return len(self.cartas)

    def poner_carta_arriba(self, carta):
        """Agrega una carta al inicio del mazo."""
        self.cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Agrega una carta al final del mazo."""
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """Saca la carta del inicio del mazo."""
        if len(self.cartas) == 0:
            raise DequeEmptyError("El mazo está vacío.")
        carta = self.cartas.extraer(0)
        if mostrar:
            carta.visible = True
        return carta

    def __str__(self):
        return str([str(carta) for carta in self.cartas])
