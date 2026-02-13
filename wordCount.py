# pylint: disable=invalid-name
"""
Módulo para contar la frecuencia de palabras en un archivo.
Nombre: Jorge Muñoz
Matrícula: a01213938
"""

import sys
import time


def main():
    """Procesa el archivo y cuenta la frecuencia de palabras."""
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return

    word_freq = {}
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            for line in file:
                # Separar por espacios y limpiar puntuación básica si es necesario
                words = line.split()
                for word in words:
                    clean_word = word.strip().lower()
                    if clean_word:
                        word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return

    # Preparar resultados
    output = []
    header = "Word\tFrequency"
    print(header)
    output.append(header)

    for word, freq in sorted(word_freq.items()):
        line = f"{word}\t{freq}"
        print(line)
        output.append(line)

    elapsed_time = time.time() - start_time
    time_msg = f"Time elapsed: {elapsed_time:.4f} seconds"
    print(time_msg)
    output.append(time_msg)

    # Guardar en archivo
    with open("WordCountResults.txt", "w", encoding='utf-8') as out_f:
        out_f.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
