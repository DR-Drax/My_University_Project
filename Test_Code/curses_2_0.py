import curses
from curses import textpad

# Función para ingresar texto (con caracteres imprimibles)
def input_text(stdscr, y, x, label):
    """
    Permite al usuario ingresar texto. El texto ingresado se almacena y retorna.
    :param stdscr: Pantalla estándar de curses.
    :param y: Fila en la que se muestra el input.
    :param x: Columna en la que se muestra el input.
    :param label: Etiqueta que se muestra antes del input.
    :return: Texto ingresado por el usuario.
    """
    curses.curs_set(1)  # Mostrar cursor
    stdscr.addstr(y, x, label)
    stdscr.refresh()

    # Crear caja para ingresar texto
    height, width = 1, 30
    box = curses.newwin(height, width, y, x + len(label) + 1)
    box.border()

    # Crear el objeto textpad y editar texto
    textpad_obj = textpad.Textbox(box)
    text = textpad_obj.edit().strip()  # Retorna el texto editado sin espacios finales

    return text


# Función para ingresar números (solo enteros)
def input_number(stdscr, y, x, label):
    """
    Permite al usuario ingresar un número entero.
    :param stdscr: Pantalla estándar de curses.
    :param y: Fila en la que se muestra el input.
    :param x: Columna en la que se muestra el input.
    :param label: Etiqueta que se muestra antes del input.
    :return: Número entero ingresado por el usuario.
    """
    curses.curs_set(1)  # Mostrar cursor
    stdscr.addstr(y, x, label)
    stdscr.refresh()

    num = ""
    while True:
        key = stdscr.getch()
        if key == 10:  # Enter
            try:
                return int(num)
            except ValueError:
                stdscr.addstr(y + 1, x, "Error: Por favor ingrese un número válido.")
                stdscr.refresh()
                num = ""  # Reiniciar entrada
        elif key == 127:  # Backspace
            num = num[:-1]
        elif 48 <= key <= 57:  # Caracteres numéricos
            num += chr(key)
        
        stdscr.addstr(y + 1, x, " " * 20)  # Limpiar la línea
        stdscr.addstr(y + 1, x, num)  # Mostrar número
        stdscr.refresh()


# Función para mostrar un menú con opciones
def menu(stdscr):
    """
    Muestra un menú de opciones que el usuario puede seleccionar con las flechas.
    :param stdscr: Pantalla estándar de curses.
    :return: La opción seleccionada por el usuario.
    """
    curses.curs_set(0)  # Ocultar el cursor
    options = ["Opción 1: Ingresar texto", "Opción 2: Ingresar número", "Opción 3: Salir"]
    selected = 0  # Opción seleccionada

    while True:
        stdscr.clear()
        for i, option in enumerate(options):
            if i == selected:
                stdscr.addstr(5 + i, 10, option, curses.A_REVERSE)  # Resaltar opción
            else:
                stdscr.addstr(5 + i, 10, option)

        stdscr.refresh()
        key = stdscr.getch()

        # Navegar por las opciones
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(options) - 1:
            selected += 1
        elif key == 10:  # Enter
            return selected  # Devuelve la opción seleccionada


# Función para crear un botón de "Aceptar"
def accept_button(stdscr, y, x):
    """
    Crea un botón de 'Aceptar' que el usuario puede presionar con Enter.
    :param stdscr: Pantalla estándar de curses.
    :param y: Fila en la que se muestra el botón.
    :param x: Columna en la que se muestra el botón.
    :return: None
    """
    curses.curs_set(0)  # Ocultar cursor
    stdscr.addstr(y, x, "[ Aceptar ]", curses.A_REVERSE)  # Crear botón resaltado
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == 10:  # Enter
            break  # Salir del bucle cuando se presiona Enter


# Función principal
def main(stdscr):
    """
    Función principal que ejecuta las operaciones.
    :param stdscr: Pantalla estándar de curses.
    :return: None
    """
    # Menú principal
    stdscr.addstr(2, 5, "Seleccione una opción del menú:")
    stdscr.refresh()
    option = menu(stdscr)

    if option == 0:
        # Ingresar texto
        text = input_text(stdscr, 8, 5, "Ingrese su texto:")
        stdscr.addstr(10, 5, f"Texto ingresado: {text}")
    elif option == 1:
        # Ingresar número
        number = input_number(stdscr, 8, 5, "Ingrese un número:")
        stdscr.addstr(10, 5, f"Número ingresado: {number}")
    elif option == 2:
        # Salir
        stdscr.addstr(10, 5, "Saliendo...")
    
    # Esperar que el usuario presione Enter para cerrar
    accept_button(stdscr, 12, 5)
    stdscr.refresh()

# Ejecutar la función principal con curses
curses.wrapper(main)

