import pandas as pd
from datetime import datetime
import logging



class ExploradorDeDatos:
    def __init__(self, datos):
        self.datos = datos
        logging.info("Explorador de datos creado.")

    def mostrar_info(self):
        try:
            logging.info("Mostrando información general del DataFrame.")
            print(self.datos.info())
        except Exception as e:
            logging.error(f"Error al mostrar información del DataFrame: {e}")

    def resumen_estadistico(self):
        try:
            logging.info("Mostrando resumen estadístico del DataFrame.")
            print(self.datos.describe())
        except Exception as e:
            logging.error(f"Error al mostrar resumen estadístico: {e}")

    def conteo_nulos(self):
        try:
            nulos = self.datos.isnull().sum()
            logging.info("Mostrando conteo de valores nulos por columna.")
            print(nulos)
        except Exception as e:
            logging.error(f"Error al mostrar conteo de nulos: {e}")