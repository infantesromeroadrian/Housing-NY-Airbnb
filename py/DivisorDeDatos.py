from sklearn.model_selection import train_test_split
import logging

class DivisorDeDatos:
    def __init__(self, datos):
        self.datos = datos
        logging.info("Divisor de datos creado.")

    def preparar_datos(self):
        try:
            # Excluir columnas no necesarias
            columnas_a_eliminar = ['id', 'NAME', 'host id', 'host name', 'neighbourhood',
                                    'country code', 'country', 'house_rules', 'license']
            datos_preparados = self.datos.drop(columns=columnas_a_eliminar)
            logging.info("Columnas no necesarias eliminadas.")
            return datos_preparados
        except Exception as e:
            logging.error(f"Error al preparar los datos: {e}")
            return None

    def dividir_datos(self, test_size=0.2, val_size=0.2, random_state=42):
        try:
            datos_preparados = self.preparar_datos()
            X = datos_preparados.drop('price', axis=1)
            y = datos_preparados['price']

            # Primero dividimos en entrenamiento y prueba
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state)

            # Ajuste del tamaño de validación
            val_size_adjusted = val_size / (1 - test_size)

            # Dividir el conjunto de entrenamiento en entrenamiento y validación
            X_train, X_val, y_train, y_val = train_test_split(
                X_train, y_train, test_size=val_size_adjusted, random_state=random_state)

            logging.info("Datos divididos en entrenamiento, validación y prueba.")
            return X_train, X_val, X_test, y_train, y_val, y_test
        except Exception as e:
            logging.error(f"Error al dividir los datos: {e}")
            return None, None, None, None, None, None