from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import numpy as np
import logging

class ModeloDePrediccion:
    def __init__(self, X_train, y_train, X_val, y_val):
        self.X_train = X_train
        self.y_train = y_train
        self.X_val = X_val
        self.y_val = y_val
        logging.info("Modelo de predicción inicializado.")

    def entrenar_modelo(self, modelo, parametros):
        try:
            grid_search = GridSearchCV(modelo, parametros, cv=5, scoring='neg_mean_squared_error', return_train_score=True)
            grid_search.fit(self.X_train, self.y_train)
            mejor_modelo = grid_search.best_estimator_
            logging.info("Mejor modelo encontrado: {}".format(mejor_modelo))
            return mejor_modelo
        except Exception as e:
            logging.error(f"Error durante el entrenamiento del modelo: {e}")
            return None

    def evaluar_modelo(self, modelo):
        try:
            predicciones = modelo.predict(self.X_val)
            rmse = np.sqrt(mean_squared_error(self.y_val, predicciones))
            mae = mean_absolute_error(self.y_val, predicciones)
            r2 = r2_score(self.y_val, predicciones)
            logging.info(f"Evaluación del modelo - RMSE: {rmse}, MAE: {mae}, R²: {r2}")
            return rmse, mae, r2
        except Exception as e:
            logging.error(f"Error durante la evaluación del modelo: {e}")
            return None, None, None