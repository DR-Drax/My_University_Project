import os
import time
import sys

def Delay_Writer(texto, retraso=0.03):
    """
    Muestra texto como si se estuviera escribiendo letra por letra con un retraso.
    
    :param texto: El texto a mostrar.
    :param retraso: Tiempo en segundos entre cada carácter (por defecto 0.1s).
    """
    texto +="\n"
    for letra in texto:
        sys.stdout.write(letra)  # Escribe un carácter sin salto de línea
        sys.stdout.flush()       # Asegura que se imprime inmediatamente
        time.sleep(retraso)      # Pausa por el tiempo especificado
    #print()  # Añade un salto de línea al final

def clear_screen():
    """
    Limpia la pantalla según el sistema operativo.
    """
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para sistemas basados en Unix (Linux, macOS, etc.)
        os.system('clear')

def Style_Menu(listMenu):
    """
    Genera un menú en estilo ASCII con un marco que se ajusta a un ancho de 34 caracteres.
    
    Parámetros:
    - listMenu: Lista de opciones del menú.

    Retorna:
    - El menú formateado como una cadena de texto.
    """
    # Encabezado del menú
    menu = "╔══════════════════════════════════╗\n"
    
    # Recorrer cada opción del menú
    for i in range(len(listMenu)):
        option = listMenu[i]
        # Ajustar el texto de cada opción para que no exceda el límite de 34 caracteres
        spaces = 34 - (len(option) + len(str(i)) + 3)  # 3 por 'i)', espacios y bordes
        menu += f"║ {i + 1}) {option}{' ' * spaces}║\n"
    
    # Pie del menú
    menu += "╚══════════════════════════════════╝"
    
    return menu

def Ascii_table(headers, data):
    """
    Dibuja una tabla ASCII con formato usando bordes decorativos y la guarda en un archivo de texto.

    Parameters:
        headers (list): Lista de encabezados para las columnas.
        data (list): Lista de listas, donde cada sublista representa una columna de datos.
        filename (str): Nombre del archivo donde se guardará la tabla. (por defecto 'tabla_resultados.txt')

    Returns:
        None
    """
    # Validar si la tabla está completamente vacía
    if not any(data):
        print("La tabla está vacía. No hay datos para mostrar.")
        return

    # Asegurar que las columnas de datos tengan la misma cantidad de elementos
    num_rows = len(data[0])
    for col in data:
        if len(col) != num_rows:
            print("Error: Las columnas no tienen el mismo número de filas.")
            return

    # Anchos de columna calculados dinámicamente
    col_widths = [
        max(len(str(headers[i])), max(len(str(col[i])) for col in data)) + 2
        for i in range(len(headers))
    ]

    # Función para dibujar una línea
    def draw_line(left, middle, right, fill):
        return left + middle.join([fill * width for width in col_widths]) + right

    # Función para imprimir una fila
    def print_row(row, border="║"):
        formatted_row = border + border.join(
            [f"{str(cell):^{col_widths[i]}}" for i, cell in enumerate((row))]
        ) + border
        return formatted_row

    # Transponer los datos para que las columnas se conviertan en filas
    transposed_data = list(zip(*data))

    # Imprimir el contenido en la consola
    print(draw_line("╔", "╦", "╗", "═"))  # Línea superior
    print(print_row(headers))  # Encabezados
    print(draw_line("╠", "╬", "╣", "═"))  # Línea divisoria
    for row in transposed_data:
        print(print_row(row))  # Filas de datos
    print(draw_line("╚", "╩", "╝", "═"))  # Línea inferior

def ask_continue(text = "¿Deseas continuar? (a) sí \n (b) no: "):
    """
    Pregunta al usuario si desea continuar, aceptando múltiples variantes de 'sí' y 'no'.

    La entrada es interpretada de forma flexible para mejorar la experiencia del usuario.
    Acepta opciones como:
    - Para "sí": 'a', '1', 'si', 'sí', 's', 'y', 'yes'
    - Para "no":  'b', '2', 'no', 'n'

    Returns:
        bool: True si el usuario desea continuar, False en caso contrario.
    """
    opciones_si = {"a", "1", "si", "sí", "s", "y", "yes"}
    opciones_no = {"b", "2", "no", "n"}

    while True:
        respuesta = input(text).strip().lower()
        if respuesta in opciones_si:
            return True
        elif respuesta in opciones_no:
            return False
        else:
            print("Opción no válida. Intenta de nuevo.")
            
# Pendiente
def dibujar_tabla_ascii(headers, data):
    """
    Dibuja una tabla ASCII con formato usando bordes decorativos.

    Parameters:
        headers (list): Lista de encabezados para las columnas.
        data (list): Lista de listas, donde cada sublista representa una columna de datos.

    Returns:
        None
    """
    # Validar si la tabla está completamente vacía
    if not any(data):
        print("La tabla está vacía. No hay datos para mostrar.")
        return

    # Asegurar que las columnas de datos tengan la misma cantidad de elementos
    num_rows = len(data[0])
    for col in data:
        if len(col) != num_rows:
            print("Error: Las columnas no tienen el mismo número de filas.")
            return

    # Anchos de columna calculados dinámicamente
    col_widths = [
        max(len(str(headers[i])), max(len(str(col[i])) for col in data)) + 2
        for i in range(len(headers))
    ]

    # Función para dibujar una línea
    def draw_line(left, middle, right, fill):
        return left + middle.join([fill * width for width in col_widths]) + right

    # Función para imprimir una fila
    def print_row(row, border="║"):
        formatted_row = border + border.join(
            [f"{str(cell):^{col_widths[i]}}" for i, cell in enumerate(row)]
        ) + border
        print(formatted_row)

    # Transponer los datos para que las columnas se conviertan en filas
    transposed_data = list(zip(*data))

    # Dibujar tabla
    print(draw_line("╔", "╦", "╗", "═"))  # Línea superior
    print_row(headers)  # Encabezados
    print(draw_line("╠", "╬", "╣", "═"))  # Línea divisoria
    for row in transposed_data:
        print_row(row)  # Filas de datos
    print(draw_line("╚", "╩", "╝", "═"))  # Línea inferior

#Ascii_table(["hola","como","funcionas"],[[1,2,3],[4,5,6],[7,5,8]])
