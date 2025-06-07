from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    """
    Representa a un paciente que ingresa a la sala de emergencias.
    Como atributos cuenta con el nombre y apellido del paciente y su nivel de riesgo con su respectiva 
    descripcion textual.
    """
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]

    def get_nombre(self):     
        """
        Obtiene el nombre del paciente y lo retorna.
        """
        return self.__nombre
    
    def get_apellido(self):     
        """
        Obtiene el apellido del paciente y lo retorna.
        """
        return self.__apellido
    
    def get_riesgo(self):       
        """
        Obtiene el nivel de riesgo del paciente y lo retorna. (1, 2 o 3)
        """
        return self.__riesgo
    
    def get_descripcion_riesgo(self):  
        """
        Obtiene el nivel de riesgo del paciente y lo retorna. (critico, moderado o bajo)
        """
        return self.__descripcion
    
    def __str__(self): 
        """
        Retorna una cadena con la descripcion del paciente.
        """
        return f"{self.__nombre} {self.__apellido}\t -> {self.__riesgo}-{self.__descripcion}"
