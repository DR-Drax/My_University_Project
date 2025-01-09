def generate_table_with_dynamic_width(content):
    """
    Genera una tabla ASCII con anchos dinámicos basados en el contenido más largo en cada columna.
    
    Parámetros:
    - content: Lista de listas donde cada sublista representa una fila de la tabla.
    
    Retorna:
    - La tabla formateada como una cadena de texto.
    """
    # Calcular el ancho máximo de cada columna basado en el contenido
    cols = len(content[0])  # Número de columnas
    col_widths = [max(len(str(row[i])) for row in content) + 2 for i in range(cols)]  # Ancho de cada columna

    # Generar la parte superior de la tabla
    top = "╔" + "╦".join(["═" * width for width in col_widths]) + "╗\n"
    
    # Generar la parte del medio de la tabla
    mid = "╟" + "╬".join(["═" * width for width in col_widths]) + "╢\n"
    
    # Generar la parte inferior de la tabla
    bottom = "╚" + "╩".join(["═" * width for width in col_widths]) + "╝\n"
    
    # Generar las filas con contenido
    rows_content = ""
    for i, row in enumerate(content):
        row_str = "║"
        for j, cell_content in enumerate(row):
            cell_content = str(cell_content).ljust(col_widths[j] - 1)  # Ajustar el contenido al ancho de la columna
            row_str += f" {cell_content}║"
        rows_content += row_str + "\n"
        if i == 0:  # Colocar la línea divisoria después de la primera fila (encabezado)
            rows_content += mid

    # Armar la tabla completa
    table = top + rows_content + bottom
    
    return table


def generate_centered_table(content):
    """
    Genera una tabla ASCII con anchos dinámicos basados en el contenido más largo en cada columna,
    y centra el contenido dentro de las celdas. El borde superior e inferior se ajusta para tener
    un ancho de columna de n+1.

    Parámetros:
    - content: Lista de listas donde cada sublista representa una fila de la tabla.

    Retorna:
    - La tabla formateada como una cadena de texto.
    """
    # Calcular el ancho máximo de cada columna basado en el contenido
    cols = len(content[0])  # Número de columnas
    col_widths = [max(len(str(row[i])) for row in content) + 1 for i in range(cols)]  # Ancho de cada columna
    
    # Ajustar el ancho de las líneas de borde superior e inferior
    adjusted_col_widths = [width + 1 for width in col_widths]
    
    # Generar la parte superior de la tabla
    top = "╔" + "╦".join(["═" * width for width in adjusted_col_widths]) + "╗\n"

    # Generar la parte del medio de la tabla
    mid = "╟" + "╬".join(["═" * width for width in col_widths]) + "╢\n"
    
    # Generar la parte inferior de la tabla
    bottom = "╚" + "╩".join(["═" * width for width in adjusted_col_widths]) + "╝\n"
    
    # Generar las filas con contenido centrado
    rows_content = ""
    for i, row in enumerate(content):
        row_str = "║"
        for j, cell_content in enumerate(row):
            cell_content = str(cell_content).center(col_widths[j])  # Centrar el contenido
            row_str += f" {cell_content} ║"
        rows_content += row_str + "\n"
        if i == 0:  # Colocar la línea divisoria después de la primera fila (encabezado)
            rows_content += mid

    # Armar la tabla completa
    table = top + rows_content + bottom
    
    return table

# Ejemplo de uso
content = [
    ["Estado", "Entrada", "Salida"],
    ["A", "0", "B"],
    ["B", "1", "C"],
    ["C", "0", "D"]
]

print(generate_centered_table(content))



