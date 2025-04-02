# README - Reporte de Transacciones

## Introducción
Este proyecto es una aplicación en Python que lee un archivo CSV con información de transacciones y genera un reporte detallado en la terminal. El propósito es procesar transacciones financieras, calcular el balance final, identificar la transacción de mayor monto y contar las transacciones de tipo Crédito y Débito.

## Instrucciones de Ejecución

### Requisitos
- Python 3.x instalado en el sistema.

### Instalación de Dependencias
Este proyecto no requiere dependencias adicionales más allá de Python.

### Ejecución
1. Coloca el archivo CSV en la misma carpeta que el script.
2. Asegúrate de que el archivo tenga el siguiente formato:
   ```csv
   id,tipo,monto
   1,Crédito,100.00
   2,Débito,50.00
   3,Crédito,200.00
   4,Débito,75.00
   5,Crédito,150.00

> python scriptInit.py

## Enfoque y Solución

El script sigue estos pasos:

1. Leer el archivo CSV y almacenar las transacciones en una lista.
2. Calcular el balance sumando créditos y restando débitos.
3. Identificar la transacción con el monto más alto.
4. Contar la cantidad de transacciones de cada tipo.
5. Imprimir el reporte en la terminal.

Las decisiones de diseño incluyeron:

- Uso del módulo csv para una lectura estructurada del archivo.
- Manejo de datos mediante listas y diccionarios para facilitar el procesamiento.
- Uso de la función max() para encontrar la transacción con el monto más alto.

## Estructura del Proyecto:

``` text
proyecto/
│── transacciones.csv   # Archivo de entrada con las transacciones
│── scriptInit.py       # Código principal para procesar el CSV y generar el reporte
│── README.md           # Documentación del proyecto


