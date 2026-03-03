import pandas as pd
import json
from dagster import asset

@asset(group_name="staging")
def stg_clientes():
    """Carga clientes, filtra activos y genera nombre_completo."""
    df = pd.read_csv("data/raw/clientes/clientes.csv")
    # Filtramos por el campo 'estado' (True)
    df = df[df['estado'] == True].copy()
    
    # Creamos nombre_completo según el formato necesario
    df['nombre_completo'] = df['nombre'] + " " + df['apellido']
    
    # Aseguramos tipo de dato para el join
    df['id_cliente'] = df['id_cliente'].astype(int)
    
    return df[['id_cliente', 'nombre_completo']]

@asset(group_name="staging")
def stg_cablemodems():
    """Aplanado del JSON, hereda 'nodo' y filtra por 'encendido'."""
    with open("data/raw/cablemodems/cablemodems.json", "r") as f:
        data = json.load(f)
    
    # 'nodo' y 'id_cliente' están en la raíz del objeto en tu JSON
    df = pd.json_normalize(
        data,
        record_path=['cablemodems'],
        meta=['id_cliente', 'nodo']
    )
    
    # Requerimiento: Redondear power a 3 decimales
    df['power'] = df['power'].astype(float).round(3)
    
    # Filtro: Solo cablemodems encendidos
    df = df[df['encendido'] == True].copy()
    
    # Aseguramos tipo de dato para el join
    df['id_cliente'] = df['id_cliente'].astype(int)
    
    return df