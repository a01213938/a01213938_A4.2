# pylint: disable=invalid-name
"""
Módulo para convertir números a binario y hexadecimal.
Nombre: Jorge Muñoz
Matrícula: a01213938
"""

import sys
import time


def to_binary(n):
    """Convierte un número entero a binario usando divisiones sucesivas."""
    if n == 0:
        return "0"
    binary = ""
    temp_n = int(n)
    while temp_n > 0:
        binary = str(temp_n % 2) + binary
        temp_n //= 2
    return binary


def to_hexadecimal(n):
    """Convierte un número entero a hexadecimal manualmente."""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hex_result = ""
    temp_n = int(n)
    while temp_n > 0:
        hex_result = hex_chars[temp_n % 16] + hex_result
        temp_n //= 16
    return hex_result


def main():
    """Función principal para procesar el archivo y mostrar resultados."""
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        return

    results = []
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    num = int(float(line.strip()))
                    results.append((num, to_binary(num), to_hexadecimal(num)))
                except ValueError:
                    print(f"Error: Dato inválido -> {line.strip()}")
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return

    # Preparar salida
    output_header = "ITEM\tNUMBER\tBINARY\tHEXADECIMAL"
    print(output_header)
    with open("ConvertionResults.txt", "w", encoding='utf-8') as out_f:
        out_f.write(output_header + "\n")
        for i, res in enumerate(results, 1):
            line = f"{i}\t{res[0]}\t{res[1]}\t{res[2]}"
            print(line)
            out_f.write(line + "\n")
        elapsed = time.time() - start_time
        time_msg = f"\nExecution Time: {elapsed:.4f} seconds"
        print(time_msg)
        out_f.write(time_msg + "\n")


if __name__ == "__main__":
    main()












    