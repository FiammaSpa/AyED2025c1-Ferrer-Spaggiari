import time
import datetime
import random
from modules.paciente import Paciente
from modules.sistema_emergencia import ColaEmergencias

n = 20  #Cantidad de ciclos
sistema = ColaEmergencias()

for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    paciente = Paciente()
    print("Nuevo paciente:", paciente)
    sistema.ingresar_paciente(paciente)

    if random.random() < 0.5:
        paciente_atendido = sistema.atender_paciente()
        if paciente_atendido:
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)

    print()
    print('Pacientes que faltan atenderse:', len(sistema.pacientes_en_espera()))
    for paciente in sistema.pacientes_en_espera():
        print('\t', paciente)

    print()
    print('-*-'*15)
    time.sleep(1)
