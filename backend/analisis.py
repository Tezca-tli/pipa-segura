import csv
import os

# Ruta al archivo que acabamos de crear
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_PEDIDOS = os.path.join(BASE_DIR, "..", "data", "pedidos.csv")

def generar_reporte():
    if not os.path.exists(ARCHIVO_PEDIDOS):
        print("No hay datos para analizar aún.")
        return

    total_litros = 0
    pedidos_por_colonia = {}
    conteo_pipas = {}

    with open(ARCHIVO_PEDIDOS, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for fila in reader:
            litros = int(fila['litros'])
            colonia = fila['colonia']
            pipa = fila['pipa_id']

            # Sumar litros totales
            total_litros += litros

            # Contar pedidos por colonia
            pedidos_por_colonia[colonia] = pedidos_por_colonia.get(colonia, 0) + 1

            # Ver qué pipa está trabajando más
            conteo_pipas[pipa] = conteo_pipas.get(pipa, 0) + 1

    print("=== 📈 REPORTE DE PIPA SEGURA ===")
    print(f"Total de agua distribuida: {total_litros} Litros")
    print("\nDemandas por Colonia:")
    for col, cant in pedidos_por_colonia.items():
        print(f"- {col}: {cant} pedido(s)")
    
    print("\nUso de Unidades:")
    for p, cant in conteo_pipas.items():
        print(f"- {p}: {cant} viajes realizados")
    print("================================")

if __name__ == "__main__":
    generar_reporte()