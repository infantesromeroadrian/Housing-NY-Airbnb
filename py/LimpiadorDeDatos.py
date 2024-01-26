import logging
import pandas as pd
import numpy as np


class LimpiadorDeDatos:
    def __init__(self, datos):
        self.datos = datos
        logging.info("Limpiador de datos creado.")

    def manejar_nulos(self):
        try:
            for columna in self.datos.columns:
                if self.datos[columna].dtype == 'object':
                    # Modificación aquí: Asignar el resultado de fillna directamente
                    self.datos[columna] = self.datos[columna].fillna(self.datos[columna].mode()[0])
                else:
                    # Igualmente aquí
                    self.datos[columna] = self.datos[columna].fillna(self.datos[columna].median())
            logging.info("Valores nulos manejados.")
        except Exception as e:
            logging.error(f"Error al manejar valores nulos: {e}")

    def corregir_datos_atipicos(self):
        try:
            for columna in ['minimum nights', 'availability 365']:
                q1 = self.datos[columna].quantile(0.25)
                q3 = self.datos[columna].quantile(0.75)
                iqr = q3 - q1
                limite_inferior = q1 - 1.5 * iqr
                limite_superior = q3 + 1.5 * iqr
                self.datos = self.datos[(self.datos[columna] >= limite_inferior) & (self.datos[columna] <= limite_superior)]
            logging.info("Datos atípicos corregidos.")
        except Exception as e:
            logging.error(f"Error al corregir datos atípicos: {e}")

    def limpiar_datos(self):
        try:
            self.manejar_nulos()
            self.corregir_datos_atipicos()
            logging.info("Datos limpiados exitosamente.")
            return self.datos
        except Exception as e:
            logging.error(f"Error durante la limpieza de datos: {e}")
            return None