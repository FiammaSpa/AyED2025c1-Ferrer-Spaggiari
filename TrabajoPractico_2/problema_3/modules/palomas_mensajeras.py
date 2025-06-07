import heapq
import os

class PalomasMensajeras:
    """
    Gestiona la red de aldeas para el envio eficiente de mensajes mediante palomas. Se utiliza:
    -Grafo para representar las aldeas y las distancias entre ellas.
    -Algoritmo de Dijkstra para encontrar las rutas mas eficientes.
    """
    def __init__(self, ruta_archivo_aldeas):
        self.grafo = {} # Diccionario de adyacencia: {aldea: {vecino: distancia}}
        self.aldeas_unicas = set() 
        self.ruta_archivo = ruta_archivo_aldeas 
        self._cargar_grafo()

    def _cargar_grafo(self):
        """
        Carga las aldeas y sus distancias desde el archivo de texto
        y construye el grafo de adyacencia.
        """
        try:
            if not os.path.exists(self.ruta_archivo):
                raise FileNotFoundError(f"El archivo '{self.ruta_archivo}' no se encontro.")

            with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line: #Ignora lineas vacias
                        continue
                    parts = line.split(', ')
                    if len(parts) == 3: #Formato: Aldea1, Aldea2, Distancia
                        aldea1, aldea2, distancia_str = parts
                        distancia = int(distancia_str)
                        
                        self.aldeas_unicas.add(aldea1)
                        self.aldeas_unicas.add(aldea2)

                        # Construir el grafo (bidireccional)
                        if aldea1 not in self.grafo:
                            self.grafo[aldea1] = {}
                        if aldea2 not in self.grafo:
                            self.grafo[aldea2] = {}
                        
                        self.grafo[aldea1][aldea2] = distancia
                        self.grafo[aldea2][aldea1] = distancia 

                    elif len(parts) == 1 and parts[0]: #caso "Diosleguarde" en aldeas.txt
                        self.aldeas_unicas.add(parts[0])
                        if parts[0] not in self.grafo:
                            self.grafo[parts[0]] = {}
                    else:
                        print(f"Advertencia: Linea con formato inesperado ignorada: '{line}'")

        except FileNotFoundError as e:
            print(f"Error: {e}")
            self.grafo = {} #Asegurarse de que el grafo este vacio si el archivo no se encontro
        except ValueError:
            print(f"Error: La distancia en la linea '{line}' no es un numero valido.")
            self.grafo = {}
        except Exception as e:
            print(f"Ocurrio un error inesperado al cargar el grafo: {e}")
            self.grafo = {}

    def mostrar_aldeas_alfabeticamente(self):
        """
        Muestra todas las aldeas cargadas en la base de datos en orden alfabetico.
        """
        print("Lista de Aldeas en Orden Alfabetico: ")
        aldeas_ordenadas = sorted(list(self.aldeas_unicas))
        for aldea in aldeas_ordenadas:
            print(f"- {aldea}")
        print("-" * 40)

    def _dijkstra(self, origen):
        """
        Implementa el algoritmo de Dijkstra para encontrar las rutas mas cortas desde un origen dado a todas las demas aldeas.
        """
        if origen not in self.grafo:
            print(f"Error: La aldea de origen '{origen}' no existe en el grafo.")
            return {}, {}

        distancias = {aldea: float('inf') for aldea in self.aldeas_unicas}
        distancias[origen] = 0
        
        predecesores = {aldea: None for aldea in self.aldeas_unicas}
        
        pq = [(0, origen)] 

        while pq:
            distancia_actual, aldea_actual = heapq.heappop(pq)

            # Si ya encontramos un camino mas corto a esta aldea, ignorar
            if distancia_actual > distancias[aldea_actual]:
                continue

            # Explorar vecinos
            for vecino, peso in self.grafo.get(aldea_actual, {}).items():
                distancia = distancia_actual + peso
                
                # Si encontramos un camino mas corto al vecino
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    predecesores[vecino] = aldea_actual
                    heapq.heappush(pq, (distancia, vecino))
        
        return distancias, predecesores

    def enviar_mensaje_eficientemente(self, origen="Peligros"):
        """
        Encuentra y muestra la forma mas eficiente de enviar un mensaje desde el origen a todas las demas aldeas.
        """
        print(f"Envio de Mensaje desde '{origen}' ")
        distancias, predecesores = self._dijkstra(origen)

        if not distancias: #Error en Dijkstra (origen no encontrado)
            return

        total_distancia_recorrida = 0
        
        # Primero, generar y ordenar las aldeas para la salida requerida
        aldeas_para_mostrar = sorted([a for a in self.aldeas_unicas if a != origen])

        # Recopilar la informacion para cada aldea
        comunicaciones = {}
        for aldea in aldeas_para_mostrar:
            if distancias[aldea] == float('inf'):
                comunicaciones[aldea] = {
                    "recibe_de": "inaccesible",
                    "envia_a": [],
                    "distancia_a_origen": "inaccesible"
                }
            else:
                comunicaciones[aldea] = {
                    "recibe_de": predecesores[aldea],
                    "envia_a": [], 
                    "distancia_a_origen": distancias[aldea]
                }
                total_distancia_recorrida += distancias[aldea] 

        # Identificar las aldeas a las que cada nodo "replica" el mensaje
        for aldea_actual in self.aldeas_unicas:
            for aldea_vecina, predecesor_vecina in predecesores.items():
                if predecesor_vecina == aldea_actual and aldea_vecina != origen: 
                    if aldea_actual == origen: 
                        comunicaciones[aldea_vecina]["recibe_de"] = origen 
                    else:
                        if aldea_actual in comunicaciones and aldea_vecina != origen:
                            comunicaciones[aldea_actual]["envia_a"].append(aldea_vecina)


        # Mostrar el detalle por cada aldea
        for aldea in aldeas_para_mostrar:
            info = comunicaciones[aldea]
            recibe_de_str = info["recibe_de"] if info["recibe_de"] else "N/A (origen)"
            envia_a_str = ", ".join(sorted(info["envia_a"])) if info["envia_a"] else "Ninguna"
            distancia_str = info["distancia_a_origen"]

            print(f"\nAldea: {aldea}")
            print(f"  Recibe la noticia de: {recibe_de_str}")
            print(f"  Envía réplicas a: {envia_a_str}")
            print(f"  Distancia desde {origen}: {distancia_str}")

        print("\n Resumen de Distancias ")
        print(f"Suma total de distancias recorridas por todas las palomas (desde Peligros a cada aldea): {total_distancia_recorrida}")
        print("-" * 40)


if __name__ == "__main__":
    ruta_aldeas_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'aldeas.txt')

    sistema_palomas = PalomasMensajeras(ruta_aldeas_txt)

    # 1. Mostrar la lista de aldeas en orden alfabético
    sistema_palomas.mostrar_aldeas_alfabeticamente()

    # 2. Enviar el mensaje eficientemente desde "Peligros" y mostrar detalles
    sistema_palomas.enviar_mensaje_eficientemente(origen="Peligros")