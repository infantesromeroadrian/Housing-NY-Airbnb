import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from main import predecir_precio

# Título de la aplicación
st.title('Predicción de Precios de Airbnb en Nueva York')

# Sidebar para la entrada de datos
st.sidebar.header('Ingrese los detalles de la ubicación')
lat = st.sidebar.number_input('Latitud', value=40.730610)  # Valor por defecto de ejemplo
long = st.sidebar.number_input('Longitud', value=-73.935242)  # Valor por defecto de ejemplo

# Botón para realizar la predicción
if st.sidebar.button('Predecir Precio'):
    # Preparar datos para la predicción
    datos_entrada = pd.DataFrame({
        'lat': [lat],
        'long': [long],
        'instant_bookable': [True],
        'Construction year': [2022.0],
        'service fee': [45.0],
        'minimum nights': [3.0],
        'number of reviews': [289.0],
        'reviews per month': [3.3],
        'review rate number': [2.0],
        'calculated host listings count': [1.0],
        'availability 365': [365.0],
        'host_identity_verified_verified': [1.0],
        'neighbourhood group_Brooklyn': [0.0],
        'neighbourhood group_Manhattan': [0.0],
        'neighbourhood group_Queens': [0.0],
        'neighbourhood group_Staten Island': [0.0],
        'neighbourhood group_brookln': [0.0],
        'neighbourhood group_manhatan': [0.0],
        'cancellation_policy_moderate': [0.0],
        'cancellation_policy_strict': [0.0],
        'room type_Hotel room': [0.0],
        'room type_Private room': [0.0],
        'room type_Shared room': [0.0],
        'last review_year': [2019],
        'last review_month': [6],
        'last review_day': [24],
    })

    precio_predicho = predecir_precio(datos_entrada)

    if precio_predicho is not None:
        # Mostrar precio predicho
        st.sidebar.write(f"El precio predicho para la ubicación dada es: ${precio_predicho[0]:.2f}")

        # Mostrar el mapa
        mapa = folium.Map(location=[lat, long], zoom_start=12)
        folium.Marker([lat, long], popup=f'Precio Predicho: ${precio_predicho[0]:.2f}').add_to(mapa)
        folium_static(mapa)
    else:
        st.sidebar.write("Error en la predicción del precio.")