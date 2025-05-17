import os

# Función para solicitar al usuario la ubicación y el nombre del archivo
def guardar_archivo():
    carpeta_destino = input("Ingrese la ruta de la carpeta donde desea guardar el archivo: ")
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión, por ejemplo, mi_archivo.txt): ")
    
    ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
    
    # Crear y guardar el archivo
    try:
        with open(ruta_completa, 'w') as archivo:
            archivo.write("Este es el contenido de mi archivo.")
        
        print(f"Archivo guardado en: {ruta_completa}")
    except FileNotFoundError:
        print("La carpeta especificada no existe.")
    except PermissionError:
        print("No tiene permisos para guardar el archivo en la ubicación especificada.")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

# Llamar a la función para guardar el archivo
guardar_archivo()
