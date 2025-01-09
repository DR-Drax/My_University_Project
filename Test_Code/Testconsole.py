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


# Uso del código
encabezados = ["Col1", "Col2", "Col3", "Col4", "Col5"]
tabla_resultados = [
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],  # Col1
    [0.0, 0.0274, 0.1093, 0.2447, 0.4323, 0.6699, 0.9549, 1.2843, 1.6543, 2.0611, 2.5],  # Col2
    [0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0, 27.0, 30.0],  # Col3
    [10.0, 10.0136, 10.0539, 10.1186, 10.2043, 10.3063, 10.4187, 10.5348, 10.6468, 10.7465, 10.8253],  # Col4
    [0.0, 0.5248, 1.0567, 1.6026, 2.169, 2.7616, 3.3853, 4.0439, 4.7402, 5.4756, 6.25]  # Col5
]

# Dibujar tabla con los datos de columnas transpuestas
dibujar_tabla_ascii(encabezados, tabla_resultados)
