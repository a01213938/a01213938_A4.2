"""
Módulo para calcular estadísticas descriptivas.
Nombre: Jorge Muñoz
Matrícula: [Tu Matricula]
"""

import sys
import time


def calculate_mean(numbers):
    """Calcula la media aritmética."""
    total = 0.0
    for num in numbers:
        total += num
    return total / len(numbers) if numbers else 0


def main():
    """Función principal."""
    start_time = time.time()

    if len(sys.argv) < 2:
        print("Error: Se requiere un archivo de texto.")
        return

    file_name = sys.argv[1]
    data = []

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    data.append(float(line.strip()))
                except ValueError:
                    print(f"Dato inválido ignorado: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_name}")
        return

    if not data:
        print("No hay datos numéricos para procesar.")
        return

    # Realizar cálculos aquí (Median, Mode, etc. con algoritmos básicos)
    mean = calculate_mean(data)
    
    elapsed_time = time.time() - start_time
    
    # Formatear resultados
    results = (
        f"Media: {mean}\n"
        f"Tiempo de ejecución: {elapsed_time:.4f} segundos"
    )

    print(results)
    with open("StatisticsResults.txt", "w", encoding='utf-8') as out_file:
        out_file.write(results)


if __name__ == "__main__":
    main()