from arbol_AVL import arbolAVL
from datetime import datetime

class Temperaturas_DB:
    """
    Base de datos en memoria para almacenar mediciones de temperatura
    asociadas a fechas, utilizando un arbol AVL.
    Las fechas se almacenan internamente como objetos datetime para
    asegurar un ordenamiento cronologico correcto.
    """
    def __init__(self):
        self._db = arbolAVL() 


    def _pasar_fecha(self, fecha_str):
        """
        Pasa de una cadena de fecha (dd/mm/aaaa) a un objeto datetime.
        """
        try:
            return datetime.strptime(fecha_str, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Formato de fecha inválido: {fecha_str}. Esperado dd/mm/aaaa.")

    def _formatear_fecha(self, fecha_obj):
        """
        Pasa de un objeto datetime a una cadena de fecha.
        """
        return fecha_obj.strftime("%d/%m/%Y")

    def guardar_temperatura(self, fecha_str, temperatura):
        """
        Dada una fecha guarda o actualiza una medicion de temperatura.
        """
        fecha_obj = self._pasar_fecha(fecha_str)
        self._db.insertar(fecha_obj, float(temperatura))
        print(f"Temperatura {temperatura}°C para la fecha {fecha_str} guardada/actualizada.")

    def devolver_temperatura(self, fecha_str):
        """
        Dada una fecha muestra la temperatura registrada para la misma.
        """
        fecha_obj = self._pasar_fecha(fecha_str)
        nodo = self._db.buscar(fecha_obj) 
        if nodo:
            print(f"Temperatura para {fecha_str}: {nodo.valor}°C") 
            return nodo.valor
        else:
            print(f"No se encontro temperatura para la fecha {fecha_str}.")
            return None

    def max_temp_rango(self, fecha1_str, fecha2_str):
        """
        Encuentra y retorna la tmeperatura maxima dentro de un rango de fechas.
        """
        fecha1_obj = self._pasar_fecha(fecha1_str)
        fecha2_obj = self._pasar_fecha(fecha2_str)

        start_date = min(fecha1_obj, fecha2_obj)
        end_date = max(fecha1_obj, fecha2_obj)

        max_temp = self._db.obtener_max_valor_en_rango(start_date, end_date) 
        if max_temp == float('-inf'):
            print(f"No se encontraron temperaturas en el rango [{self._formatear_fecha(start_date)} - {self._formatear_fecha(end_date)}].")
            return None
        else:
            print(f"Temperatura maxima en el rango [{self._formatear_fecha(start_date)} - {self._formatear_fecha(end_date)}]: {max_temp}°C")
            return max_temp

    def min_temp_rango(self, fecha1_str, fecha2_str):
        """
        Encuentra y retorna la temperatura minima dentro de un rango de fechas.
        """
        fecha1_obj = self._pasar_fecha(fecha1_str)
        fecha2_obj = self._pasar_fecha(fecha2_str)

        start_date = min(fecha1_obj, fecha2_obj)
        end_date = max(fecha1_obj, fecha2_obj)

        min_temp = self._db.obtener_min_valor_en_rango(start_date, end_date) 
        if min_temp == float('inf'):
            print(f"No se encontraron temperaturas en el rango [{self._formatear_fecha(start_date)} - {self._formatear_fecha(end_date)}].")
            return None
        else:
            print(f"Temperatura minima en el rango [{self._formatear_fecha(start_date)} - {self._formatear_fecha(end_date)}]: {min_temp}°C")
            return min_temp

    def temp_extremos_rango(self, fecha1_str, fecha2_str):
        """
        Encuentra y retorna las temperaturas maximas y minimas dentro de un rango.
        """
        fecha1_obj = self._pasar_fecha(fecha1_str)
        fecha2_obj = self._pasar_fecha(fecha2_str)

        start_date = min(fecha1_obj, fecha2_obj)
        end_date = max(fecha1_obj, fecha2_obj)

        min_val = self._db.obtener_min_valor_en_rango(start_date, end_date) 
        max_val = self._db.obtener_max_valor_en_rango(start_date, end_date) 

        if min_val == float('inf') and max_val == float('-inf'):
            print(f"No se encontraron temperaturas en el rango [{self._formatear_fecha(start_date)} - {self._formatear_fecha(end_date)}].")
            return (None, None)
        else:
            print(f"Temperaturas extremas en el rango [{self._formatear_fecha(start_date)} - {self._formatear_fecha(end_date)}]: Min {min_val}°C, Max {max_val}°C")
            return (min_val, max_val)

    def borrar_temperatura(self, fecha_str):
        """
        Dada una fecha borra la medicion de la temperatura.
        """
        fecha_obj = self._pasar_fecha(fecha_str)
        nodo_a_borrar = self._db.buscar(fecha_obj)
        if nodo_a_borrar:
            self._db.eliminar(fecha_obj) 
            print(f"Medicion de temperatura para la fecha {fecha_str} eliminada.")
        else:
            print(f"No se encontro medicion para la fecha {fecha_str} para eliminar.")

    def devolver_temperaturas_rango(self, fecha1_str, fecha2_str):
        """
        Retorna una lista de todas las mediciones de temperatura dentro de un rango de fechas ordenadas cronologicamente.
        """
        fecha1_obj = self._pasar_fecha(fecha1_str)
        fecha2_obj = self._pasar_fecha(fecha2_str)

        start_date = min(fecha1_obj, fecha2_obj)
        end_date = max(fecha1_obj, fecha2_obj)

        nodos_en_rango = self._db.obtener_nodos_en_rango(start_date, end_date) 

        formatted_results = []
        for fecha_obj, temp in nodos_en_rango:
            formatted_results.append(f"{self._formatear_fecha(fecha_obj)}: {temp}°C")

        if not formatted_results:
            print(f"No hay mediciones en el rango [{self._formatear_fecha(start_date)} - {self._formatear_fecha(end_date)}].")
        else:
            print(f"Mediciones en el rango [{self._formatear_fecha(start_date)} - {self._formatear_fecha(end_date)}]:")
            for res in formatted_results:
                print(f"- {res}")
        return formatted_results

    def cantidad_muestras(self):
        """
        Retorna la cantidad de total de mediciones.
        """
        def _contar_nodos(nodo):
            if not nodo:
                return 0
            return 1 + _contar_nodos(nodo.izquierda) + _contar_nodos(nodo.derecha)

        count = _contar_nodos(self._db.raiz)
        print(f"Cantidad total de muestras en la BD: {count}")
        return count