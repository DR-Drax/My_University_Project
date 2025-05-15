import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # Force interactive backend before other import

from math import cos,sin,pi
import os


def graficar_resultados(tabla_resultados, filename=None):
    """
    Genera un gráfico con los resultados calculados para el perfil de levas.

    Parameters:
        tabla_resultados (list): Lista con dos elementos:
                                 - tabla_resultados[0]: Lista de valores de tiempo (x).
                                 - tabla_resultados[1]: Lista de valores de desplazamiento (y).
        filename (str, optional): Nombre del archivo donde se guardará el gráfico. Si es None, se mostrará en pantalla.

    Returns:
        None: Guarda o muestra el gráfico generado.
    """
    tiempos = tabla_resultados[0]
    desplazamientos = tabla_resultados[1]

    plt.figure(figsize=(10, 6))
    plt.plot(tiempos, desplazamientos, marker='o', label='Perfil de leva')
    plt.title('Gráfica del perfil de levas')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Desplazamiento (m)')
    plt.grid(True)
    plt.legend()

    if filename:
        plt.show()
        #plt.savefig(filename)  # Guardar la gráfica en el archivo
        #print(f"Gráfico guardado en {filename}")
    else:
        plt.show()  # Mostrar la gráfica en pantalla
        input()

    plt.close()  # Cerrar la figura para liberar recursos

def dibujar_tabla_ascii(headers, data, filename=None):
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

    # Abrir el archivo para escribir
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(draw_line("╔", "╦", "╗", "═") + '\n')  # Línea superior
        f.write(print_row(headers) + '\n')  # Encabezados
        f.write(draw_line("╠", "╬", "╣", "═") + '\n')  # Línea divisoria
        for row in transposed_data:
            f.write(print_row(row) + '\n')  # Filas de datos
        f.write(draw_line("╚", "╩", "╝", "═") + '\n')  # Línea inferior

    print(f"Tabla guardada en {filename}")

def lineal(info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal):
    """
    Calcula el desplazamiento lineal durante una etapa de movimiento.

    Parameters:
        info (list): Información de tiempo, movimiento y alturas de la leva.
        etapa_actual (int): Índice de la etapa actual.
        tiempo_actual (float): Tiempo actual.
        delta_tiempo (float): Incremento del tiempo entre intervalos.
        tabla_resultados (list): Tabla que almacena tiempos y desplazamientos.
        posicion_plano (float): Desplazamiento previo (posición inicial del plano).
        tiempo_temporal (int): Contador temporal para la etapa actual.

    Returns:
        Tuple: Actualiza los valores de info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano y tiempo_temporal.
    """
    if info[1][etapa_actual] == 1:  # Movimiento ascendente
        tabla_resultados[1].append(round((tiempo_actual * info[2][etapa_actual]) / info[0][etapa_actual],4))
        tiempo_temporal = 1  # Reiniciar el tiempo temporal

    elif info[1][etapa_actual] == 3:  # Movimiento descendente
        altura_control = info[2][etapa_actual - 1] if info[2][etapa_actual] == 0 else info[2][etapa_actual]
        desplazamiento = posicion_plano - ((tiempo_temporal * delta_tiempo * altura_control) / info[0][etapa_actual])
        desplazamiento = max(desplazamiento, 0)  # Evitar valores negativos
        tabla_resultados[1].append(round(desplazamiento,4))
        tiempo_temporal += 1

    return info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal

def armónico(info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal):
    """
    Calcula el desplazamiento armónico durante una etapa de movimiento.

    Parameters:
        Parameters:
        info (list): Información de tiempo, movimiento y alturas de la leva.
        etapa_actual (int): Índice de la etapa actual.
        tiempo_actual (float): Tiempo actual.
        delta_tiempo (float): Incremento del tiempo entre intervalos.
        tabla_resultados (list): Tabla que almacena tiempos y desplazamientos.
        posicion_plano (float): Desplazamiento previo (posición inicial del plano).
        tiempo_temporal (int): Contador temporal para la etapa actual.

    Returns:
        Tuple: Actualiza los valores de info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano y tiempo_temporal.
    """
    if info[1][etapa_actual] == 1:  # Movimiento ascendente
        formula = posicion_plano + (info[2][etapa_actual] / 2) * (1 - cos((pi * tiempo_actual) / info[0][etapa_actual]))
        tabla_resultados[1].append(round(formula,4))

    elif info[1][etapa_actual] == 3:  # Movimiento descendente
        formula = info[2][etapa_actual] + ((posicion_plano - info[2][etapa_actual]) / 2) * (1 + cos((pi * tiempo_temporal * delta_tiempo) / info[0][etapa_actual]))
        formula = max(formula, 0)  # Evitar valores negativos
        tabla_resultados[1].append(round(formula,4))
        tiempo_temporal += 1

    return info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal

def cicloidal(info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal):
    """
    Calcula el desplazamiento cicloidal durante una etapa de movimiento.

    Parameters:
        Parameters:
        info (list): Información de tiempo, movimiento y alturas de la leva.
        etapa_actual (int): Índice de la etapa actual.
        tiempo_actual (float): Tiempo actual.
        delta_tiempo (float): Incremento del tiempo entre intervalos.
        tabla_resultados (list): Tabla que almacena tiempos y desplazamientos.
        posicion_plano (float): Desplazamiento previo (posición inicial del plano).
        tiempo_temporal (int): Contador temporal para la etapa actual.

    Returns:
        Tuple: Actualiza los valores de info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano y tiempo_temporal.
    """

    if info[1][etapa_actual] == 1:  # Movimiento ascendente
        formula = posicion_plano + info[2][etapa_actual] * ((tiempo_actual / info[0][etapa_actual]) - (1 / (2 * pi)) * sin((2 * pi * tiempo_actual) / info[0][etapa_actual]))
        tabla_resultados[1].append(round(formula,4))

    elif info[1][etapa_actual] == 3:  # Movimiento descendente
        formula = info[2][etapa_actual] + (posicion_plano - info[2][etapa_actual]) * (
            1 - ((tiempo_temporal * delta_tiempo) / info[0][etapa_actual]) + (1 / (2 * pi)) * sin((2 * pi * tiempo_temporal * delta_tiempo) / info[0][etapa_actual])
        )
        formula = max(formula, 0)  # Evitar valores negativos
        tabla_resultados[1].append(round(formula,4))
        tiempo_temporal += 1

    return info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal

def levas_table(info, tipo_movimiento, num_intervalos,contador):
    """
    Genera una tabla con los desplazamientos calculados para un perfil de levas.

    Parameters:
        info (list): Información de tiempo, movimiento y alturas de la leva.
        tipo_movimiento (list): Lista de tipos de movimiento (1: lineal, 2: armónico, 3: cicloidal).
        num_intervalos (int): Cantidad de intervalos para el cálculo.

    Returns:
        None: Genera la tabla y muestra el gráfico.
    """
    suma_tiempos = sum(info[0])  # Suma total de tiempos
    tiempos_acumulados = [round(sum(info[0][:i + 1]), 2) for i in range(len(info[0]))]  # Tiempos acumulados
    tabla_resultados = [[],[],[],[],[]]  # Tabla de tiempos y desplazamientos

    delta_tiempo = suma_tiempos / num_intervalos
    velocidad_leva = 1/suma_tiempos
    etapa_actual = 0
    tiempo_temporal = 0
    posicion_plano = 0

    
    delta_tiempo = 0.001
    print(f"Tiempos acumulados {tiempos_acumulados}")
    print(f"tiempo - {suma_tiempos}")
    print(f"altura: {info[2][0]}")
    print(f"W leva {round(velocidad_leva,5)}")
    i = 0
    # rango = suma_tiempos/delta_tiempo

    while True:  # Bucle indefinido
        #print(f"contador {i}")
        # imprimir tiempo por consola
        # print(f"tiempo --{tiempo_actual}")

        tiempo_actual = round(i * delta_tiempo, 3)
        tabla_resultados[0].append(tiempo_actual)
        

        if info[1][etapa_actual] == 2:  # Mantener plano
            tabla_resultados[1].append(round(posicion_plano,5))
            tiempo_temporal = 1

        elif tipo_movimiento[etapa_actual] == 1:  # Movimiento lineal
            info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal = lineal(
                info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal)
            
        elif tipo_movimiento[etapa_actual] == 2:  # Movimiento armónico
            info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal = armónico(
                info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal)        

        elif tipo_movimiento[etapa_actual] == 3:  # Movimiento cicloidal
            info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal = cicloidal(
                info, etapa_actual, tiempo_actual, delta_tiempo, tabla_resultados, posicion_plano, tiempo_temporal)

        # Calcular los Deg
        tabla_resultados[2].append(round((tiempo_actual*velocidad_leva*360),6))

        # Calcular Rx
        rx = (info[2][0]+tabla_resultados[1][i])*cos(tabla_resultados[2][i]*(pi)/180)
        tabla_resultados[3].append(round(rx,4))

        # Calcular Ry
        ry = (info[2][0]+tabla_resultados[1][i])*sin(tabla_resultados[2][i]*(pi)/180)
        tabla_resultados[4].append(round(ry,4))


        if tiempo_actual == tiempos_acumulados[etapa_actual] and etapa_actual < len(tiempos_acumulados) - 1:
            etapa_actual += 1
            posicion_plano = tabla_resultados[1][-1]

        if tiempo_actual >= suma_tiempos:  # Condición para romper el bucle
            break

        i += 1  # Incrementar manualmente """  
    
    graficar_resultados([tabla_resultados[0],tabla_resultados[1]],f"Grafica_Resultados_{contador}")
    graficar_resultados([tabla_resultados[3],tabla_resultados[4]],f"Forma_Leva_{contador}")

    # Datos de ejemplo para probar la función
    encabezados = ["Tiempo", "Desplazamiento[mm]","Deg °", "Rx", "Ry"]
    # Llamar a la función para dibujar la tabla
    filename=(f"tabla_resultados_{contador}.txt")


    dibujar_tabla_ascii(encabezados,tabla_resultados,filename)


    contador += 1
    return contador


#Eje 1          time        tipo    altura
#y = levas_table([[3,1,6,2],[1,2,3,2],[10,10,0,0]],[2,1,3,1],100,1)