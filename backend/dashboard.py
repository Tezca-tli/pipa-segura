import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CSV = os.path.join(BASE_DIR, "..", "data", "pedidos.csv")
RUTA_GRAFICA = os.path.join(BASE_DIR, "..", "data", "reporte_visual.png")

def generar_dashboard():
    if not os.path.exists(ARCHIVO_CSV):
        print(f"❌ No se encontró el archivo: {ARCHIVO_CSV}")
        print("Asegúrate de haber corrido main.py primero para generar datos.")
        return

    # 1. Cargar datos con Pandas
    df = pd.read_csv(ARCHIVO_CSV)

    # 2. Configurar la figura (2 gráficas)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('📊 Dashboard Operativo - Pipa Segura Ensenada', fontsize=16)

    # --- GRÁFICA 1: Demanda por Colonia ---
    demanda_colonia = df['colonia'].value_counts()
    demanda_colonia.plot(kind='bar', ax=ax1, color='skyblue', edgecolor='black')
    ax1.set_title('Zonas con Mayor Demanda')
    ax1.set_ylabel('Número de Pedidos')
    ax1.set_xlabel('Colonia')

    # --- GRÁFICA 2: Distribución por Pipa ---
    uso_pipas = df['pipa_id'].value_counts()
    uso_pipas.plot(kind='pie', ax=ax2, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
    ax2.set_title('Uso de Unidades Logísticas')
    ax2.set_ylabel('')

    # 3. Guardar y Mostrar
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(RUTA_GRAFICA)
    print(f"✅ Dashboard generado exitosamente en: {RUTA_GRAFICA}")
    plt.show()

if __name__ == "__main__":
    generar_dashboard()