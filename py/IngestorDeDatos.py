
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IngestorDeDatos:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        logging.info("Ingestor de datos creado.")

    def cargar_datos(self):
        try:
            datos = pd.read_csv(self.ruta_archivo)
            logging.info("Datos cargados exitosamente desde {}".format(self.ruta_archivo))
            return datos
        except Exception as e:
            logging.error("Error al cargar los datos desde {}: {}".format(self.ruta_archivo, e))
            return None