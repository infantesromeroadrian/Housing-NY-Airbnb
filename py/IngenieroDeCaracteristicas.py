import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import logging

class IngenieroDeCaracteristicas:
    def __init__(self, datos):
        """
        Inicializa el ingeniero de características con un DataFrame de Pandas.
        :param datos: DataFrame de Pandas con los datos.
        """
        self.datos = datos
        logging.info("Ingeniero de características creado.")

    def aplicar_one_hot_encoding(self):
        """
        Aplica One-Hot Encoding a las columnas categóricas especificadas.
        """
        try:
            # Reiniciar índice del DataFrame
            self.datos.reset_index(drop=True, inplace=True)

            one_hot_columns = ['host_identity_verified', 'neighbourhood group', 'cancellation_policy', 'room type']

            # Rellenar valores nulos en columnas categóricas
            for col in one_hot_columns:
                self.datos[col] = self.datos[col].fillna('Desconocido')

            encoder = OneHotEncoder(drop='first')
            one_hot_encoded = encoder.fit_transform(self.datos[one_hot_columns]).toarray()
            columnas_encoded = encoder.get_feature_names_out(one_hot_columns)
            df_encoded = pd.DataFrame(one_hot_encoded, columns=columnas_encoded)
            self.datos = self.datos.join(df_encoded).drop(one_hot_columns, axis=1)
            logging.info("One-hot encoding aplicado.")
        except Exception as e:
            logging.error(f"Error al aplicar one-hot encoding: {e}")

    def convertir_fechas(self):
        """
        Convierte columnas de fecha a formato numérico (año, mes, día).
        """
        try:
            formato_fecha = '%m/%d/%Y'  # Modifica según el formato correcto
            for col in self.datos.select_dtypes(include=['object']):
                if 'review' in col:  # Ajusta según el nombre de tu columna
                    self.datos[col] = pd.to_datetime(self.datos[col], format=formato_fecha, errors='coerce')

                if np.issubdtype(self.datos[col].dtype, np.datetime64):
                    self.datos[col + '_year'] = self.datos[col].dt.year
                    self.datos[col + '_month'] = self.datos[col].dt.month
                    self.datos[col + '_day'] = self.datos[col].dt.day
                    self.datos.drop(col, axis=1, inplace=True)
            logging.info("Columnas de fecha transformadas a características numéricas.")
        except Exception as e:
            logging.error(f"Error al convertir columnas de fecha: {e}")

    def convertir_numeros(self):
        """
        Convierte columnas de precio y tarifa de servicio a tipo numérico.
        """
        try:
            self.datos['price'] = self.datos['price'].astype(str)
            self.datos['service fee'] = self.datos['service fee'].astype(str)

            self.datos['price'] = self.datos['price'].str.replace('[\$,]', '', regex=True).astype(float)
            self.datos['service fee'] = self.datos['service fee'].str.replace('[\$,]', '', regex=True).astype(float)
            logging.info("Columnas convertidas a tipo numérico.")
        except Exception as e:
            logging.error(f"Error al convertir columnas a tipo numérico: {e}")

    def transformar_caracteristicas(self):
        """
        Ejecuta todas las transformaciones de características definidas.
        """
        try:
            self.aplicar_one_hot_encoding()
            self.convertir_fechas()
            self.convertir_numeros()
            logging.info("Transformación de características completada.")
            return self.datos
        except Exception as e:
            logging.error(f"Error durante la transformación de características: {e}")
            return None