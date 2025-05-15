import matplotlib
matplotlib.use('TkAgg')  # Force interactive backend before other imports
import matplotlib.pyplot as plt
import sympy as sp
# Rest of your imports...

#import sympy as sp
#import matplotlib.pyplot as plt
import re  # Necesario para trabajar con expresiones regulares

# Definir las variables simbólicas
x, y = sp.symbols('x y')


def agregar_operadores_implicitos(equation_text):
    """
    Agrega operadores de multiplicación (*) implícitos donde sea necesario.
    Por ejemplo: '4x' -> '4*x', '(1+4x)' -> '(1+4*x)'
    """
    # Patrón: Busca un número o cierre de paréntesis seguido de una variable o paréntesis de apertura
    pattern = r'(\d)([a-zA-Z\(])'
    # Inserta un operador de multiplicación (*) donde se encuentre el patrón
    processed_text = re.sub(pattern, r'\1*\2', equation_text)
    return processed_text

def graficar_tablas_unificada(tables, nombres):
    """
    Genera un gráfico con una o varias tablas de resultados.

    Parameters:
        tables: list, una tabla (list con valores de x e y) o lista de tablas.
        nombres: list, nombres de los métodos o del método (opcional si es una sola tabla).

    Returns:
        None, muestra el gráfico.
    """
    plt.figure(figsize=(10, 6))

    # Si solo se pasa una tabla, convertirla a lista para uniformidad
    if isinstance(tables[0][0], (int, float)):
        tables = [tables]
        nombres = [nombres] if nombres else ['Resultados']

    # Graficar todas las tablas
    for table, nombre in zip(tables, nombres):
        x_values = table[0]
        y_values = table[1]
        plt.plot(x_values, y_values, label=nombre)

    plt.title('Comparación de Métodos Numéricos' if len(tables) > 1 else f'Resultados: {nombres[0]}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def excata(equation, min, max, h, xi, yi, table):
    y = sp.Function('y')(x)
    ode = sp.Eq(y.diff(x), equation)
    
    # Resolver la ecuación diferencial
    solucion = sp.dsolve(ode)
    print(f"Solución simbólica: {ode}")
    
    # Resolver la constante con la condición inicial y(xi) = yi
    constantes = sp.solve(solucion.rhs.subs(x, xi) - yi)
    solucion = solucion.subs(constantes[0])  # Sustituir la constante en la solución
    
    # Convertir la solución a función evaluable
    solucion_func = sp.lambdify(x, solucion.rhs, 'numpy')  
    valores_x = [round(xi + i * h, 2) for i in range(int((max - xi) / h) + 1)]
    valores_y = [solucion_func(val) for val in valores_x]
    
    # Agregar valores a la tabla
    table[0].extend(valores_x)
    table[1].extend(valores_y)
    return table

# Función para el método de Euler
def Numeric_euler(equation, min, max, h, xi, yi, table):
    """
    Implementa el método de Euler para aproximar la solución de una ecuación diferencial.

    Parameters:
        equation: sympy.Expr, la ecuación diferencial.
        min: int, límite inferior del rango de iteración.
        max: int, límite superior del rango de iteración.
        h: float, tamaño del paso.
        xi: float, valor inicial de x.
        yi: float, valor inicial de y.
        table: list, lista que almacena los valores calculados de x e y.

    Returns:
        None, imprime la tabla con los valores aproximados de x e y.
    """
    for _ in range(min, max):
        solucion = equation.subs({x: xi, y: yi})
        yi = yi + solucion * h
        xi += h
        table[0].append(round(xi, 2))
        table[1].append(round(yi, 4))
    print("euler")
    print("  xi\tyi")
    for row in zip(*table):
        print(row)
    return table

# Función para el método de Heun
def Numeric_Hevn(equation, min, max, h, xi, yi, table):
    """
    Implementa el método de Heun para aproximar la solución de una ecuación diferencial.
    """
    table_Hevn = [[],[],[]]

    for _ in range(min, max):
        
        solucion = equation.subs({x: xi, y: yi})
        y_pred = yi + solucion * h

        table_Hevn[0].append(round(xi, 3))
        table_Hevn[1].append(round(y_pred,4))
        table_Hevn[2].append(round(yi, 4))

        yi = yi + ((solucion + equation.subs({x: xi + h, y: y_pred})) / 2) * h
        xi += h

        table[0].append(round(xi, 2))
        table[1].append(round(yi, 4))     

    print("Hevn")
    print("  xi\ty°\tyi")
    for i in zip(*table_Hevn):
        print(i)
    return table

# Función para el método de Runge-Kutta (orden 2)
def Numeric_Runge(equation, min, max, h, xi, yi, table):
    """
    Implementa el método de Runge-Kutta de segundo orden.
    """

    ruge_table = [[],[],[],[]]    
    for _ in range(min, max):


        k1 = equation.subs({x: xi, y: yi})
        k2 = equation.subs({x: xi + h / 2, y: yi + k1 * h / 2})

        ruge_table[0].append(round(xi, 3))
        ruge_table[1].append(round(yi, 4))
        ruge_table[2].append(round(k1,4))
        ruge_table[3].append(round(k2,4))

        yi = yi + k2 * h
        xi += h

        table[0].append(round(xi, 2))
        table[1].append(round(yi, 4))
    
    print("Ruge")
    print("  xi\tk1\tk2\tyi")
    for row in zip(*ruge_table):
        print(row)
    return table

# Función para convertir superíndices a formato de potencia en Python
def convertir_superindices(expresion):
    superindices = {
        '¹': '1', '²': '2', '³': '3',
        '⁴': '4', '⁵': '5', '⁶': '6',
        '⁷': '7', '⁸': '8', '⁹': '9', '⁰': '0'
    }
    for superindice, numero in superindices.items():
        expresion = expresion.replace(superindice, f"**{numero}")
    return expresion

# Función principal que gestiona la ejecución
def menu_Numeric(equation_text, MinX, MaxX, h, xi, yi, Type):
    """
    Función para resolver ecuaciones diferenciales usando métodos numéricos.
    
    Parameters:
        equation_text: str, ecuación diferencial como texto.
        MinX: int, límite inferior del rango.
        MaxX: int, límite superior del rango.
        h: float, tamaño del paso.
        xi: float, valor inicial de x.
        yi: float, valor inicial de y.
        Type: int, método numérico (1: Euler, 2: Heun, 3: Runge-Kutta).

    Returns:
        None, imprime la tabla de resultados.
    """
    table = []
    min = int(MinX)
    max = int(MaxX / h) - min

    equation_T = agregar_operadores_implicitos(equation_text)
    
    equation_T = convertir_superindices(equation_T)

    # Después reemplazamos '^' por '**' y 'sen' por 'sin' para asegurar que la sintaxis sea correcta
    equation_T = equation_T.replace("√", "sqrt")  # Para raíz cuadrada
    equation_T = equation_T.replace("e^","exp")
    equation_T = equation_T.replace("^", "**").replace("sen", "sin")

    print(f"ecuacion {equation_T}")


    etiqueta = []
    try:
        # Intentar convertir el texto en una expresión simbólica
        equation = sp.sympify(equation_T)
    except (sp.SympifyError, SyntaxError) as e:
        print(f"Error: La ecuación no es válida. Detalles: {e}")
        return

    print(f"Range: {MinX} <= x <= {MaxX}\tPaso: {h}\ty(0)={yi}")

    # Seleccionar el método y calcular
    metodo_nombre = ""
    try:
        if Type == 1:
            metodo_nombre = "Euler"
            etiqueta = [["Xi","Yi"]]
            table = Numeric_euler(equation, min, max, h, xi, yi, [[xi], [yi]])
        elif Type == 2:
            metodo_nombre = "Heun"
            etiqueta = [["Xi","Y°","Yi"]]
            table =Numeric_Hevn(equation, min, max, h, xi, yi, [[xi], [yi]])
        elif Type == 3:
            metodo_nombre = "Runge-Kutta"
            table = Numeric_Runge(equation, min, max, h, xi, yi, [[xi], [yi]])
        elif Type == 5:
            metodo_nombre = "Exacta"
            etiqueta = [["Xi","K1","K2","Yi"]]
            table = excata(equation, min, max, h, xi, yi,[[xi],[yi]])

        elif Type == 4:
            #excata(equation, min, max, h, xi, yi)
            table_E = Numeric_euler(equation, min, max, h, xi, yi, [[xi], [yi]])
            table_H = Numeric_Hevn(equation, min, max, h, xi, yi, [[xi], [yi]])
            table_R = Numeric_Runge(equation, min, max, h, xi, yi, [[xi], [yi]])
            table = [table_E, table_H, table_R]
            metodo_nombre = ["Euler", "Heun", "Runge-Kutta"]
           

        else:
            print("Error: Tipo de método no válido. Usa 1 (Euler), 2 (Heun) o 3 (Runge-Kutta).")
            return
    except Exception as e:
        print(f"Error durante la ejecución: {e}")
        return
     # Graficar resultados
    graficar_tablas_unificada(table, metodo_nombre)


#menu_Numeric("y*x³-1.1y",0,2,.2,0,1,4)
#menu_Numeric("x-y + 1",0,1,.1,0,1,3)
#menu_Numeric("e^(-x) + x*e^(-x)",0,1,.1,0,1,1)
#menu_Numeric("-2x³+12x²-20x+8.5",0,2,.5,0,1,4)

#
"""
print("Euler\n")
#               MinX, MaxX, h, xi, yi, Type
main("y*sen(x)³",0,3,.5,0,1,2) 
print("Hevn\n")
main("(x+y)/x",1,3,.5,1,0,2)
print("Ruge\n")
main("(x+y)/x",1,3,.5,1,0,3)"""
