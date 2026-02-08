import sys
import time


def count_words(file_path):
    """Lee el archivo y cuenta la frecuencia de cada palabra."""
    word_freq = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    # Limpieza básica de puntuación
                    clean_word = word.lower().strip('.,!?;:"()')
                    if clean_word:
                        word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no existe.")
        return None
    return word_freq


def main():
    """Función principal para conteo de palabras."""
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return

    start_time = time.time()
    freqs = count_words(sys.argv[1])
    elapsed_time = time.time() - start_time

    if freqs is not None:
        header = f"{'PALABRA':<20} | {'FRECUENCIA':<10}\n"
        separator = "-" * 35 + "\n"
        result_str = header + separator
        
        for word, count in sorted(freqs.items(), key=lambda x: x[1], reverse=True):
            result_str += f"{word:<20} | {count:<10}\n"
        
        result_str += f"\nTiempo de ejecución: {elapsed_time:.4f} segundos\n"
        
        print(result_str)
        with open("WordCountResults.txt", "w", encoding="utf-8") as f:
            f.write(result_str)


if __name__ == "__main__":
    main()