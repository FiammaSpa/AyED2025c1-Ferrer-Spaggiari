import unittest
from modules.temperaturas_db import Temperaturas_DB
from datetime import datetime

class TestTemperaturasDB(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada método de prueba."""
        self.db = Temperaturas_DB()

    def test_guardar_y_devolver_temperatura(self):
        """
        Prueba la insercion y recuperacion de temperaturas, incluyendo actualizaciones.
        """
        self.db.guardar_temperatura("01/01/2023", 10.0)
        self.assertEqual(self.db.devolver_temperatura("01/01/2023"), 10.0)

        # Actualizar temperatura
        self.db.guardar_temperatura("01/01/2023", 12.5)
        self.assertEqual(self.db.devolver_temperatura("01/01/2023"), 12.5)

        # Devolver temperatura de fecha no existente
        self.assertIsNone(self.db.devolver_temperatura("02/01/2023"))

    def test_cantidad_muestras(self):
        """
        Prueba la funcion de conteo de muestras.
        """
        self.assertEqual(self.db.cantidad_muestras(), 0)
        self.db.guardar_temperatura("01/01/2023", 10.0)
        self.assertEqual(self.db.cantidad_muestras(), 1)
        self.db.guardar_temperatura("02/01/2023", 15.0)
        self.assertEqual(self.db.cantidad_muestras(), 2)
        self.db.guardar_temperatura("01/01/2023", 12.0) # Actualiza, no añade nuevo
        self.assertEqual(self.db.cantidad_muestras(), 2)

    def test_borrar_temperatura(self):
        """
        Prueba la eliminacion de temperaturas.
        """
        self.db.guardar_temperatura("01/01/2023", 10.0)
        self.db.guardar_temperatura("02/01/2023", 15.0)
        self.assertEqual(self.db.cantidad_muestras(), 2)

        self.db.borrar_temperatura("01/01/2023")
        self.assertEqual(self.db.cantidad_muestras(), 1)
        self.assertIsNone(self.db.devolver_temperatura("01/01/2023"))

        # Borrar temperatura que no existe
        self.db.borrar_temperatura("03/01/2023") # No debería causar error
        self.assertEqual(self.db.cantidad_muestras(), 1)

    def test_max_temp_rango(self):
        """
        Prueba la obtencion de la temperatura maxima en un rango.
        """
        self.db.guardar_temperatura("01/01/2023", 10.0)
        self.db.guardar_temperatura("05/01/2023", 20.0)
        self.db.guardar_temperatura("10/01/2023", 15.0)
        self.db.guardar_temperatura("15/01/2023", 25.0)
        # Rango normal
        self.assertEqual(self.db.max_temp_rango("01/01/2023", "10/01/2023"), 20.0)
        # Rango con orden inverso
        self.assertEqual(self.db.max_temp_rango("10/01/2023", "01/01/2023"), 20.0)
        # Rango que incluye un solo elemento
        self.assertEqual(self.db.max_temp_rango("05/01/2023", "05/01/2023"), 20.0)
        # Rango que no tiene datos
        self.assertIsNone(self.db.max_temp_rango("02/01/2023", "04/01/2023"))
        # Rango que incluye todo
        self.assertEqual(self.db.max_temp_rango("01/01/2023", "15/01/2023"), 25.0)
    def test_min_temp_rango(self):
        """Prueba la obtencion de la temperatura minima en un rango."""
        self.db.guardar_temperatura("01/01/2023", 10.0)
        self.db.guardar_temperatura("05/01/2023", 20.0)
        self.db.guardar_temperatura("10/01/2023", 5.0)
        self.db.guardar_temperatura("15/01/2023", 12.0)

        self.assertEqual(self.db.min_temp_rango("01/01/2023", "15/01/2023"), 5.0)
        self.assertEqual(self.db.min_temp_rango("15/01/2023", "01/01/2023"), 5.0)
        self.assertEqual(self.db.min_temp_rango("05/01/2023", "12/01/2023"), 5.0)
        self.assertIsNone(self.db.min_temp_rango("02/01/2023", "04/01/2023"))

    def test_temp_extremos_rango(self):
        """
        Prueba la obtencion de temperaturas extremas en un rango.
        """
        self.db.guardar_temperatura("01/01/2023", 10.0)
        self.db.guardar_temperatura("05/01/2023", 20.0)
        self.db.guardar_temperatura("10/01/2023", 5.0)
        self.db.guardar_temperatura("15/01/2023", 25.0)

        min_val, max_val = self.db.temp_extremos_rango("01/01/2023", "15/01/2023")
        self.assertEqual(min_val, 5.0)
        self.assertEqual(max_val, 25.0)

        min_val, max_val = self.db.temp_extremos_rango("02/01/2023", "04/01/2023")
        self.assertIsNone(min_val)
        self.assertIsNone(max_val)

    def test_devolver_temperaturas_rango(self):
        """
        Prueba la obtencion de todas las temperaturas en un rango.
        """
        self.db.guardar_temperatura("01/01/2023", 10.0)
        self.db.guardar_temperatura("05/01/2023", 20.0)
        self.db.guardar_temperatura("10/01/2023", 15.0)
        self.db.guardar_temperatura("15/01/2023", 25.0)

        expected_results = [
            "01/01/2023: 10.0°C",
            "05/01/2023: 20.0°C",
            "10/01/2023: 15.0°C"
        ]
        results = self.db.devolver_temperaturas_rango("01/01/2023", "10/01/2023")
        self.assertListEqual(results, expected_results)

        # Rango inverso
        results_rev = self.db.devolver_temperaturas_rango("10/01/2023", "01/01/2023")
        self.assertListEqual(results_rev, expected_results)

        # Rango sin datos
        self.assertListEqual(self.db.devolver_temperaturas_rango("02/01/2023", "04/01/2023"), [])


    def test_formato_invalido(self):
        """
        Prueba el manejo de formatos de fecha invalidos.
        """
        with self.assertRaises(ValueError):
            self.db.guardar_temperatura("2023-01-01", 10.0)
        with self.assertRaises(ValueError):
            self.db.devolver_temperatura("01/01/23")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)