import csv

# Metodo encargado de realizar el analisis de transacciones
def procesar_transacciones(nombre_archivo):
    balance = 0.0
    transacciones = []
    conteo = {"Crédito": 0, "Débito": 0}
    
    # Se encarga de leer el archivo csv
    with open(nombre_archivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tipo = row['tipo']
            monto = float(row['monto'])
            transacciones.append((int(row['id']), tipo, monto))
            
            if tipo == "Crédito":
                balance += monto
                conteo["Crédito"] += 1
            elif tipo == "Débito":
                balance -= monto
                conteo["Débito"] += 1
    # Busca el numero mayor
    transaccion_mayor = max(transacciones, key=lambda x: x[2])
    
    print("Reporte de Transacciones")
    print("-" * 45)
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {transaccion_mayor[0]} - {transaccion_mayor[2]:.2f}")
    print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")

# Metodo principal
def main():
    archivo_csv = "transacciones.csv"  # Nombre del archivo CSV
    procesar_transacciones(archivo_csv) # Llamar a la función con el nombre del archivo CSV

# Punto de ejecucion
if __name__ == "__main__":
    main()