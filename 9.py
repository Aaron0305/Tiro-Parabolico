def count_words_in_file(file_path):
    try:
        # Abre el archivo en modo lectura
        with open(file_path, 'r', encoding='utf-8') as file:
            # Lee el contenido del archivo
            content = file.read()
            # Divide el contenido en palabras
            words = content.split()
            # Cuenta el número de palabras
            word_count = len(words)
        
        print(f"The file '{file_path}' contiene {word_count} palabras.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Especifica el nombre del archivo
file_path = r'C:\Users\DELL\Documents\Bloc de notas\prueba.txt'

# Ejecuta la función para contar las palabras
count_words_in_file(file_path)
