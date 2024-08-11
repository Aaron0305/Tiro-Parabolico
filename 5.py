import os

def copy_file_content(source_file, destination_file):
    try:
        # Verifica si el archivo fuente existe
        if not os.path.exists(source_file):
            print(f"El archivo fuente {source_file} no existe.")
            return
        
        # Lee el contenido del archivo fuente
        with open(source_file, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"Contenido leído de {source_file}: {content}")  # Mensaje de depuración
        
        # Escribe el contenido en el archivo de destino
        with open(destination_file, 'w', encoding='utf-8') as file:
            file.write(content)
            print(f"Contenido escrito en {destination_file}")  # Mensaje de depuración
        
        print(f"Copiado el contenido de {source_file} a {destination_file}")
    except FileNotFoundError:
        print(f"El archivo {source_file} no existe.")
    except IOError as e:
        print(f"Ha ocurrido un error de E/S: {e}")

# Especifica el nombre del archivo origen y el archivo destino
source_file = r'C:\Users\DELL\Documents\Bloc de notas\prueba.txt'
destination_file = r'C:\Users\DELL\Documents\Bloc de notas\prueba_2.txt'

# Ejecuta la función de copiado
copy_file_content(source_file, destination_file)
