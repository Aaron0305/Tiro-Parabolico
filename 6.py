import os
import shutil
#! cambio de nombre del archivo
def move_file_to_directory(source_file, target_directory):
    try:
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        shutil.move(source_file, os.path.join(target_directory, os.path.basename(source_file)))
        print(f"Moved {source_file} to {target_directory}")
    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Especifica el nombre del archivo y el directorio destino
source_file = r'C:\Users\DELL\Documents\Visual\archivo para mover.txt'
target_directory = r'C:\archivos movidos'

# Ejecuta la función de movimiento
move_file_to_directory(source_file, target_directory)
