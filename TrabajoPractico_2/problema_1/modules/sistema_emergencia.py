from modules.cola_prioridad import ColaPrioridad

class ColaEmergencias:
    """
        Gestiona la cola de pacientes en una sala de emergencias.
        Utiliza ColaPrioridad para asegurar que los pacientes mas criticos
        sean atendidos primero y con desempate por orden de llegada.
    """
    def __init__(self):
        self.cola = ColaPrioridad(lambda paciente: paciente.get_riesgo())

    def ingresar_paciente(self, paciente): 
        """
        Ingresa un nuevo paciente a la cola de emergencias.
        """
        self.cola.insertar(paciente)

    def atender_paciente(self):    
        """
        Atiende y remueve al paciente con la mayor prioridad (el mas critico) de la cola.
        """
        return self.cola.extraer()

    def pacientes_en_espera(self): 
        """
        Retorna una lista de todos los pacientes que actualmente se encuentran en la cola de espera.
        """
        return self.cola.elementos()
