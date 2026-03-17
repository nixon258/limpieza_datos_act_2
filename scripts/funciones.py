import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def importar_datos(url):
    df = pd.read_csv(url)
    return df

def eliminar_columna(df, columna):
    return df.drop(columna, axis=1)

def obtener_duplicados(df):
    return df[df.duplicated(keep=False)]

def eliminar_duplicados(df):
    return df.drop_duplicates()

def limpiar_simbolo_moneda(df, columna='UnitPrice', simbolo='£'):
    df[columna] = df[columna].astype(str).str.replace(simbolo, '', regex=False)
    return df

def convertir_a_numerico(df, columna):
    df[columna] = pd.to_numeric(df[columna], errors='coerce')
    return df

def obtener_valores_cero(df, columna):
    return df[df[columna] == 0]

def filtrar_mayores_a_cero(df, columna):
    return df[df[columna] > 0]
def obtener_nulos(df, columna):
    return df[df[columna].isnull()]

def contar_nulos(df, columna):
    return df[columna].isnull().sum()

def obtener_negativos(df, columna):
    return df[df[columna] < 0]

def convertir_a_absoluto(df, columna):
    df[columna] = df[columna].abs()
    return df

def eliminar_nulos(df, columna):
    return df.dropna(subset=[columna])

def convertir_a_fecha(df, columna):
    df[columna] = pd.to_datetime(df[columna], errors='coerce')
    return df

def obtener_valores_unicos(df, columna):
    return df[columna].unique()

def reemplazar_valores(df, columna, valores_viejos, valor_nuevo):
    df[columna] = df[columna].replace(valores_viejos, valor_nuevo)
    return df

def contar_valor(df, columna, valor):
    return df[df[columna] == valor].shape[0]
def crear_mapa(df_agrupado):
    fig = px.choropleth(
        df_agrupado,
        locations='Country',
        locationmode='country names',
        color='Quantity',
        hover_name='Country',
        title='Ventas Globales por País',
        color_continuous_scale=px.colors.sequential.Plasma
    )
    return fig

def mostrar_mapa(fig):
    fig.show()