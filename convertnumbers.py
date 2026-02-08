import sys
import time


def to_binary(num):
    """Convierte un número a binario usando algoritmo de división."""
    if num == 0:
        return "0"
    is_negative = num < 0
    num = abs(int(num))
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return "-" + binary if is_negative else binary


def to_hexadecimal(num):
    """Convierte un número a hexadecimal usando algoritmo de división."""
    if num == 0:
        return "0"
    is_negative = num < 0
    num = abs(int(num))
    hex_chars = "0123456789ABCDEF"
    hex_result = ""
    while num > 0:
        hex_result = hex_chars[num % 16] + hex_result
        num //= 16
    return "-" + hex_result if is_negative else hex_result


def main():
    """Función principal."""
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        return

    start_time = time.time()
    results = []
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    val = int(float(line.strip()))
                    results.append((val, to_binary(val), to_hexadecimal(val)))
                except ValueError:
                    print(f"Error: Dato inválido omitido: {line.strip()}")
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return

    elapsed_time = time.time() - start_time
    output = f"ITEM\tDECIMAL\tBINARY\tHEX\n"
    for i, res in enumerate(results, 1):
        output += f"{i}\t{res[0]}\t{res[1]}\t{res[2]}\n"
    
    output += f"\nTiempo de ejecución: {elapsed_time:.4f} s\n"
    print(output)
    with open("ConvertionResults.txt", "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    main()