import os
from modules.palomas import PalomasMensajeras

def main():
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(current_dir, 'data', 'aldeas.txt')

    sistema = PalomasMensajeras(ruta_archivo)

    #Mostrar la lista de aldeas en orden alfabetico
    sistema.mostrar_aldeas_alfabeticamente()

    # Calcular y mostrar la propagacion del mensaje de la forma mas eficiente
    sistema.enviar_mensaje_eficientemente(origen="Peligros")

if __name__ == "__main__":
    main()