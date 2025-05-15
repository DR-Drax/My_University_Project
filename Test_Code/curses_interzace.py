import curses

def main(stdscr):
    """
    Función principal que gestiona la interacción con el usuario utilizando la biblioteca `curses`.
    
    stdscr: Objeto estándar de pantalla proporcionado por `curses.wrapper`.
    """

    # Oculta el cursor para que la interfaz sea más limpia
    curses.curs_set(0)

    # Datos principales del menú
    menu = ["Opción 1", "Opción 2", "Opción 3", "Salir"]  # Opciones del menú
    previews = [  # Detalles o previsualizaciones de cada opción
        "Detalle de la Opción 1: Esta opción realiza X tarea.",
        "Detalle de la Opción 2: Esta opción permite Y acción.",
        "Detalle de la Opción 3: Aquí puedes hacer Z.",
        "Salir del programa."
    ]

    selected_idx = 0  # Índice de la opción actualmente seleccionada

    def draw_menu():
        """
        Dibuja el menú principal y la previsualización en la pantalla.
        """
        stdscr.clear()  # Limpia la pantalla para evitar texto superpuesto
        height, width = stdscr.getmaxyx()  # Obtiene las dimensiones de la terminal

        # Dibuja el menú en el lado izquierdo
        for idx, option in enumerate(menu):
            x = 2  # Margen izquierdo
            y = 2 + idx  # Espaciado entre las opciones
            # Resalta la opción seleccionada
            if idx == selected_idx:
                stdscr.addstr(y, x, f"> {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, f"  {option}")

        # Dibuja la previsualización en el lado derecho
        preview_text = previews[selected_idx]  # Obtiene el texto asociado a la opción seleccionada
        preview_start_y = 2  # Coordenada Y de inicio para la previsualización
        preview_start_x = width // 2  # Coordenada X de inicio (mitad de la pantalla)
        stdscr.addstr(preview_start_y, preview_start_x, "PREVISUALIZACIÓN:")  # Título
        # Muestra el contenido línea por línea
        for i, line in enumerate(preview_text.splitlines()):
            stdscr.addstr(preview_start_y + 2 + i, preview_start_x, line)

        stdscr.refresh()  # Actualiza la pantalla con los cambios

    while True:
        draw_menu()  # Dibuja el menú en cada iteración
        key = stdscr.getch()  # Captura la tecla presionada por el usuario

        # Navegación entre opciones
        if key == curses.KEY_UP and selected_idx > 0:  # Subir en el menú
            selected_idx -= 1
        elif key == curses.KEY_DOWN and selected_idx < len(menu) - 1:  # Bajar en el menú
            selected_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter para seleccionar
            if menu[selected_idx] == "Salir":  # Salir del programa
                break
            else:
                # Acción para las otras opciones seleccionadas
                stdscr.clear()  # Limpia la pantalla para mostrar el contenido nuevo
                stdscr.addstr(0, 0, f"Seleccionaste: {menu[selected_idx]}")
                stdscr.addstr(1, 0, "Ingresa texto (Enter para continuar):")
                curses.echo()  # Muestra el texto que escribe el usuario
                user_input = stdscr.getstr(2, 0).decode("utf-8")  # Captura la entrada del usuario
                curses.noecho()  # Oculta el texto nuevamente
                stdscr.addstr(3, 0, f"Texto ingresado: {user_input}")
                stdscr.addstr(5, 0, "Presiona cualquier tecla para volver al menú.")
                stdscr.refresh()  # Actualiza la pantalla
                stdscr.getch()  # Espera a que el usuario presione una tecla para continuar

# Utiliza `curses.wrapper` para gestionar automáticamente la configuración de la terminal
curses.wrapper(main)

