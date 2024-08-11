import csv

def separate_and_reorganize_wine_records(input_file, output_file):
    try:
        # Abrir el archivo CSV de entrada
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader)  # Leer el encabezado

            # Verificar la posición de la columna que contiene el tipo de vino
            try:
                wine_type_index = header.index('type')
            except ValueError:
                print("No se encontró la columna 'type' en el archivo CSV.")
                return
            
            white_wine_records = [header]
            red_wine_records = [header]

            # Separar los registros de vino blanco y tinto
            for row in reader:
                if len(row) > wine_type_index:
                    wine_type = row[wine_type_index].strip().lower()
                    if wine_type == 'white':
                        white_wine_records.append(row)
                    elif wine_type == 'red':
                        red_wine_records.append(row)

        # Guardar los registros reorganizados en un nuevo archivo CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(white_wine_records)
            writer.writerows(red_wine_records)
        
        print(f"Los registros se han reorganizado en '{output_file}' correctamente.")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{input_file}'.")
    except IOError as e:
        print(f"Ocurrió un error de E/S: {e}")

# Especifica los nombres de los archivos
input_file = r'C:\Users\DELL\Documents\Visual\winequality-both.csv'
output_file = r'C:\Users\DELL\Documents\Visual\winequality-separated.csv'

# Ejecuta la función para separar y reorganizar los registros
separate_and_reorganize_wine_records(input_file, output_file)