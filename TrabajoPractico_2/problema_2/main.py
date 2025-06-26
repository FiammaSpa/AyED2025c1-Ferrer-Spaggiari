from modules.temperaturas_db import Temperaturas_DB

def main():
    db_temperaturas = Temperaturas_DB()

    print("--- Guardando temperaturas  ---")
    db_temperaturas.guardar_temperatura("05/01/2023", 19.8)
    db_temperaturas.guardar_temperatura("10/01/2023", 22.0)
    db_temperaturas.guardar_temperatura("12/01/2023", 23.0)
    db_temperaturas.guardar_temperatura("15/01/2023", 25.5)
    db_temperaturas.guardar_temperatura("20/01/2023", 28.1)
    db_temperaturas.guardar_temperatura("25/01/2023", 30.0)
    db_temperaturas.guardar_temperatura("28/01/2023", 29.5)
    db_temperaturas.guardar_temperatura("01/02/2023", 18.5)

    db_temperaturas.guardar_temperatura("15/01/2023", 26.0) #actualizamos después de la inserción inicial.

    print("\n--- Devolviendo temperaturas ---")
    db_temperaturas.devolver_temperatura("10/01/2023")
    db_temperaturas.devolver_temperatura("15/01/2023")
    db_temperaturas.devolver_temperatura("01/01/2023") # Fecha que no existe

    print("\n--- Cantidad de muestras ---")
    db_temperaturas.cantidad_muestras()

    print("\n--- Temperatura máxima en un rango ---")
    db_temperaturas.max_temp_rango("05/01/2023", "20/01/2023")
    db_temperaturas.max_temp_rango("01/01/2023", "03/01/2023") # Rango sin datos
    db_temperaturas.max_temp_rango("20/01/2023", "05/01/2023") # Orden inverso

    print("\n--- Temperatura mínima en un rango ---")
    db_temperaturas.min_temp_rango("05/01/2023", "20/01/2023")
    db_temperaturas.min_temp_rango("01/01/2023", "03/01/2023") # Rango sin datos
    db_temperaturas.min_temp_rango("20/01/2023", "05/01/2023") # Orden inverso

    print("\n--- Temperaturas extremas en un rango ---")
    db_temperaturas.temp_extremos_rango("10/01/2023", "25/01/2023")
    db_temperaturas.temp_extremos_rango("01/03/2023", "05/03/2023") # Rango sin datos

    print("\n--- Devolviendo temperaturas en un rango (ordenado por fecha) ---")
    db_temperaturas.devolver_temperaturas_rango("05/01/2023", "25/01/2023")
    db_temperaturas.devolver_temperaturas_rango("25/01/2023", "05/01/2023") # Orden inverso
    db_temperaturas.devolver_temperaturas_rango("01/03/2023", "05/03/2023") # Rango sin datos

    print("\n--- Borrando una temperatura ---")
    db_temperaturas.borrar_temperatura("12/01/2023")
    db_temperaturas.devolver_temperatura("12/01/2023") # Verificar si se borró
    db_temperaturas.cantidad_muestras()

    print("\n--- Borrando una temperatura que no existe ---")
    db_temperaturas.borrar_temperatura("01/01/2024")

if __name__ == "__main__":
    main()