import os
from cola_prioridad import ColaPrioridad

class PalomasMensajeras:
    def __init__(self, ruta_archivo_aldeas):
        self.grafo = {}
        self.aldeas_unicas = set()
        self.ruta_archivo = ruta_archivo_aldeas
        self._cargar_grafo()

    def _cargar_grafo(self):
        """Carga el grafo de aldeas y distancias desde el archivo de texto."""
        if not os.path.exists(self.ruta_archivo):
            print(f"Error: El archivo '{self.ruta_archivo}' no fue encontrado.")
            return

        with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                partes = line.split(', ')
                if len(partes) == 3:
                    a1, a2, d = partes
                    try:
                        distancia = int(d)
                        self.aldeas_unicas.update([a1, a2])
                        self.grafo.setdefault(a1, {})[a2] = distancia
                        self.grafo.setdefault(a2, {})[a1] = distancia 
                    except ValueError:
                        print(f"Linea ignorada por distancia invalida (no es un numero): {line}")
                elif len(partes) == 1: #Para aldeas que quizás no tienen conexiones directas listadas
                    aldea = partes[0]
                    self.aldeas_unicas.add(aldea)
                    self.grafo.setdefault(aldea, {})
                else:
                    print(f"Linea ignorada por formato invalido: {line}")

        if not self.aldeas_unicas:
            print(f"Advertencia: No se cargaron aldeas del archivo '{self.ruta_archivo}'. El grafo esta vacio.")

    def mostrar_aldeas_alfabeticamente(self):
        """Muestra la lista de todas las aldeas unicas en orden alfabetico."""
        print("Aldeas en orden alfabetico:")
        if not self.aldeas_unicas:
            print("No hay aldeas cargadas.")
            print("-" * 40)
            return

        for aldea in sorted(self.aldeas_unicas):
            print(f"- {aldea}")
        print("-" * 40)

    def _prim(self, origen_inicial):
        """Implementacion del algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST)."""
        if not self.grafo:
            return {}, {}, 0

        if origen_inicial not in self.aldeas_unicas:
             print(f"Error: La aldea origen '{origen_inicial}' no existe en la lista de aldeas cargadas.")
             return {}, {}, 0
        
        if origen_inicial not in self.grafo or not self.grafo[origen_inicial]:
            if len(self.aldeas_unicas) == 1:
                return {}, {}, 0
            else:
                pass


        visitadas = set()
        
        min_heap_personalizado = ColaPrioridad(funcion_prioridad=lambda item: item[0]) 
        
        predecesores = {} 
        distancias_aristas_mst = {} 
        costo_total_mst = 0

        visitadas.add(origen_inicial)
        
        for vecino, peso in self.grafo.get(origen_inicial, {}).items():
            min_heap_personalizado.insertar((peso, origen_inicial, vecino))
        
        #El bucle continua hasta que el heap este vacio o todas las aldeas hayan sido visitadas
        while not min_heap_personalizado.esta_vacia() and len(visitadas) < len(self.aldeas_unicas):
            peso, desde, hasta = min_heap_personalizado.extraer()

            if hasta not in visitadas:
                visitadas.add(hasta)
                predecesores[hasta] = desde
                distancias_aristas_mst[hasta] = peso
                costo_total_mst += peso

                for vecino, d in self.grafo.get(hasta, {}).items():
                    if vecino not in visitadas:
                        min_heap_personalizado.insertar((d, hasta, vecino))
        
        if len(visitadas) < len(self.aldeas_unicas):
            print(f"Advertencia: No todas las aldeas estan conectadas en el grafo. Se encontro un MST parcial que conecta {len(visitadas)} de {len(self.aldeas_unicas)} aldeas.")
            
        return predecesores, distancias_aristas_mst, costo_total_mst

    def enviar_mensaje_eficientemente(self, origen="Peligros"):
        """Calcula y muestra la forma mas eficiente de entregar un mensaje desde
        una aldea de origen a todas las demás, utilizando el algoritmo de Prim.
        """
        if not self.aldeas_unicas:
            print("No hay aldeas cargadas para enviar mensajes.")
            return
        
        if origen not in self.aldeas_unicas:
            print(f"Error: La aldea origen '{origen}' no se encuentra entre las aldeas cargadas.")
            return

        print(f"\n--- Propagacion de Noticia desde '{origen}'  ---")
        
        predecesores, distancias_aristas_mst, costo_total_mst = self._prim(origen)

        if not predecesores and len(self.aldeas_unicas) > 1:
            print("No se pudo construir un árbol de expansion minima que conecte todas las aldeas o el grafo es vacio")
            print("-" * 40)
            return

        comunicaciones = {aldea: {"recibe_de": None, "envia_a": []} for aldea in self.aldeas_unicas}
        
        comunicaciones[origen]["recibe_de"] = "NADIE (es el origen)"

        for destino, origen_msg in predecesores.items():
            comunicaciones[destino]["recibe_de"] = origen_msg
            comunicaciones[origen_msg]["envia_a"].append(destino)

        print("\nDetalle de la Propagacion por Aldea:")
        for aldea in sorted(comunicaciones.keys()):
            info = comunicaciones[aldea]
            print(f"Aldea: {aldea}")
            print(f"  Recibe la noticia de: {info['recibe_de']}")
            
            envia = ", ".join(sorted(info["envia_a"])) if info["envia_a"] else "Ninguna"
            print(f"  Envia réplicas a: {envia}")
            
            if aldea != origen:
                dist_recibida = distancias_aristas_mst.get(aldea, "N/A (no conectada en MST)")
                print(f"  Distancia desde quien le envia (en MST): {dist_recibida} leguas\n")
            else:
                print(f"  Distancia desde quien le envia: N/A (es el origen)\n")

        print("--- Resumen General ---")
        print(f"Suma total de distancias recorridas por todas las palomas: {costo_total_mst} leguas")
        print("-" * 40)