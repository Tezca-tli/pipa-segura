import csv
import math
import os
import re
from datetime import datetime

# 1. Configuración de Rutas (Fuera de la función para que sea global)
# Esto detecta la ubicación real de main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Sube un nivel y entra a /data/
RUTA_DATA = os.path.join(BASE_DIR, "..", "data")
ARCHIVO_PEDIDOS = os.path.join(RUTA_DATA, "pedidos.csv")

# Aseguramos que la carpeta /data exista, si no, la crea
if not os.path.exists(RUTA_DATA):
    os.makedirs(RUTA_DATA)

# 2. Base de datos de prueba
PIPAS_DISPONIBLES = [
    {"id": "PIPA-CENTRO", "lat": 31.8667, "lon": -116.6000, "capacidad": 5000},
    {"id": "PIPA-VALLE-DORADO", "lat": 31.8100, "lon": -116.5800, "capacidad": 10000},
    {"id": "PIPA-SAUZAL", "lat": 31.8900, "lon": -116.6800, "capacidad": 2500}
]

def validar_telefono(telefono):
    return bool(re.match(r"^\d{10}$", telefono))

def calcular_distancia(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def procesar_pedido(nombre, telefono, colonia, lat_cliente, lon_cliente, litros):
    if not validar_telefono(telefono):
        print(f"❌ Error: Teléfono '{telefono}' inválido (deben ser 10 dígitos).")
        return

    print(f"\n--- Procesando pedido: {nombre} en {colonia} ---")
    
    # Lógica de asignación
    mejor_distancia = float('inf')
    pipa_asignada = None

    for pipa in PIPAS_DISPONIBLES:
        dist = calcular_distancia(lat_cliente, lon_cliente, pipa['lat'], pipa['lon'])
        if dist < mejor_distancia:
            mejor_distancia = dist
            pipa_asignada = pipa['id']

    # Datos para el CSV
    nuevo_pedido = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cliente": nombre,
        "telefono": telefono,
        "colonia": colonia,
        "litros": litros,
        "pipa_id": pipa_asignada,
        "estatus": "Pendiente"
    }

    # Guardado seguro usando la ruta absoluta
    archivo_existe = os.path.isfile(ARCHIVO_PEDIDOS)

    with open(ARCHIVO_PEDIDOS, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=nuevo_pedido.keys())
        if not archivo_existe:
            writer.writeheader()
        writer.writerow(nuevo_pedido)

    print(f"✅ Pedido guardado. Asignado a: {pipa_asignada}")

# --- PRUEBAS ---
if __name__ == "__main__":
    # Prueba en Maneadero
    procesar_pedido("Juan Carlos", "6461234567", "Maneadero", 31.7500, -116.5000, 5000)
    # Prueba fallida de teléfono
    procesar_pedido("Bárbara", "123", "Centro", 31.8667, -116.6000, 2500)