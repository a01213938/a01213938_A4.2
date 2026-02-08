
import sys
import time


def read_numbers(file_path):
    """Lee números de un archivo y maneja datos inválidos."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    val = float(line.strip())
                    numbers.append(val)
                except ValueError:
                    print(f"Error: Dato inválido encontrado y omitido: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no existe.")
        sys.exit(1)
    return numbers


def compute_statistics(data):
    """Calcula media, mediana, moda, varianza y desviación estándar."""
    if not data:
        return None

    count = len(data)
    # Media
    mean = sum(data) / count

    # Mediana
    sorted_data = sorted(data)
    if count % 2 == 0:
        median = (sorted_data[count // 2 - 1] + sorted_data[count // 2]) / 2
    else:
        median = sorted_data[count // 2]

    # Moda
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    max_freq = max(frequency.values())
    mode = [k for k, v in frequency.items() if v == max_freq]
    mode_val = mode[0] if len(mode) == 1 else mode

    # Varianza
    variance = sum((x - mean) ** 2 for x in data) / count

    # Desviación estándar
    std_dev = variance ** 0.5

    return mean, median, mode_val, variance, std_dev


def main():
    """Función principal para la ejecución del programa."""
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        return

    start_time = time.time()
    file_name = sys.argv[1]
    data = read_numbers(file_name)
    
    stats = compute_statistics(data)
    elapsed_time = time.time() - start_time

    if stats:
        mean, median, mode, var, std = stats
        results = (
            f"RESULTADOS ({file_name}):\n"
            f"Media: {mean}\n"
            f"Mediana: {median}\n"
            f"Moda: {mode}\n"
            f"Varianza: {var}\n"
            f"Desviación Estándar: {std}\n"
            f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n"
        )
        
        print(results)
        
        with open("StatisticsResults.txt", "a", encoding="utf-8") as f_out:
            f_out.write(results + "\n" + "-"*30 + "\n")


if __name__ == "__main__":
    main()