import logging
import pandas as pd
from IngestorDeDatos import IngestorDeDatos
from ExploradorDeDatos import ExploradorDeDatos
from LimpiadorDeDatos import LimpiadorDeDatos
from IngenieroDeCaracteristicas import IngenieroDeCaracteristicas
from DivisorDeDatos import DivisorDeDatos
from ModeloDePrediccion import ModeloDePrediccion
from sklearn.linear_model import LinearRegression
import pickle

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ruta del archivo de datos
ruta_archivo_datos = "/Users/adrianinfantes/Desktop/AIR/CollegeStudies/MachineLearningPath/Portfolio/AirbnbProjects/NyAirbnb/data/Airbnb_Open_Data.csv"

# Ingestar datos
ingestor = IngestorDeDatos(ruta_archivo_datos)
datos = ingestor.cargar_datos()

# Explorar datos
explorador = ExploradorDeDatos(datos)
explorador.mostrar_info()
explorador.resumen_estadistico()
explorador.conteo_nulos()

# Limpiar datos
limpiador = LimpiadorDeDatos(datos)
datos_limpios = limpiador.limpiar_datos()

# Ingeniería de características
ingeniero = IngenieroDeCaracteristicas(datos_limpios)
datos_transformados = ingeniero.transformar_caracteristicas()

# Dividir datos
divisor = DivisorDeDatos(datos_transformados)
X_train, X_val, X_test, y_train, y_val, y_test = divisor.dividir_datos()

# Modelo de predicción
modelo = ModeloDePrediccion(X_train, y_train, X_val, y_val)

# Parámetros para el modelo (ajustar según sea necesario)
parametros_rl = {'fit_intercept': [True, False]}

# Entrenar y evaluar el modelo
mejor_modelo = modelo.entrenar_modelo(LinearRegression(), parametros_rl)
rmse, mae, r2 = modelo.evaluar_modelo(mejor_modelo)

# Guardar el modelo entrenado
ruta_modelo_guardado = "/Users/adrianinfantes/Desktop/AIR/CollegeStudies/MachineLearningPath/Portfolio/AirbnbProjects/NyAirbnb/model/mejor_modelo.pkl"
with open(ruta_modelo_guardado, 'wb') as archivo:
    pickle.dump(mejor_modelo, archivo)

logging.info("Proceso completado. El modelo ha sido guardado.")

# Función para predecir precio basado en características
# Función para predecir precio basado en características
def predecir_precio(datos_entrada):
    try:
        with open('/Users/adrianinfantes/Desktop/AIR/CollegeStudies/MachineLearningPath/Portfolio/AirbnbProjects/NyAirbnb/model/mejor_modelo.pkl', 'rb') as archivo:
            modelo_cargado = pickle.load(archivo)
        predicciones = modelo_cargado.predict(datos_entrada)
        return predicciones
    except Exception as e:
        logging.error(f"Error al predecir el precio: {e}")
        return None


# Prueba de la función (esto lo puedes eliminar o comentar)
if __name__ == "__main__":
    lat_prueba, long_prueba = 40.7128, -74.0060  # Coordenadas de ejemplo
    precio_predicho = predecir_precio(lat_prueba, long_prueba)
    print(f"Precio predicho: {precio_predicho[0] if precio_predicho is not None else 'Error en predicción'}")