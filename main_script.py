import os

#________User System__________#
from PyTools.InputUser import check_num_input as CheckIOp
from PyTools.InputUser import check_float_input as CheckF
from PyTools.PySisteam import *

#__________Formulario Physics_____#
from Formulario_Uni.Fisica.Ondas import *

#_____Cinematica de mecanismos____#
from Cinematica_Mecanismos.Perfil_Levas import *

#from Maths
from Formulario_Uni.Maths.Meth_Num import *

#__Digital systems__
from Sistemas_Digitales.conversor_7_16_seg import *
from Sistemas_Digitales.MaquinaEstados import *
from Sistemas_Digitales.DisplayLCD_Ascii import *
from Sistemas_Digitales.Num_Systen import * 

def Continue():
    """
    Función que pregunta al usuario si desea continuar con otro ejercicio.
    """
    print("\nDo you want do another exercise")
    opt = CheckIOp(1, 2,Style_Menu(["Yes","No"]))
    return opt == 1 

def Sistemas_Digitales(TextHistory,imageHistory):
    flag = True
    TextHistory += "Sistemas Digitales\n"
    """
    Función para manejar las opciones del menú de Control de Motores.
    """
    clear_screen()

    x = CheckIOp(1, 5,Style_Menu(["Conversor 7 y 16 seg [switch]","Conversor 7 y 16 seg [Timer]","Maquina Estado","Display LCD","Back"]))
    if x == 1:
        seg = int(input("Number of the dysplay \n1)16seg \n2)7seg\n==>"))

        input_phrase = input("Instert frase\n==>")
        flieName = input("Instert Name of file\n==>")
        vhdl_code = generate_vhdl_code_sw(input_phrase,flieName,seg)

        # Seleccion


        # Escribir el código VHDL generado en un archivo
        filename = flieName+".vhd"
        with open(filename, 'w') as file:
            file.write(vhdl_code)

        TextHistory += f"\tSave file {filename}"
        print(f"Archivo '{filename}' generado con el código VHDL para mostrar la frase '{input_phrase}'.")
    
    elif x == 2:
        seg = CheckIOp(1,2,"Number of the dysplay \n1)16seg \n2)7seg")
        #seg = int(input("Number of the dysplay \n1)16seg \n2)7seg\n==>"))

        input_phrase = input("Instert frase\n==>")
        flieName = input("Instert Name of file\n==>")
        time = CheckF("Time")
        vhdl_code = generate_vhdl_code_timer(input_phrase,flieName,seg,time)

        # Seleccion


        # Escribir el código VHDL generado en un archivo
        filename = flieName+".vhd"
        with open(filename, 'w') as file:
            file.write(vhdl_code)

        TextHistory += f"\tSave file {filename}"
        print(f"Archivo '{filename}' generado con el código VHDL para mostrar la frase '{input_phrase}'.")

    elif x == 3:
        NumberList = get_number_list()
        for i in NumberList:
            tableE = create(i,decimal_to_binary(i))
            TextHistory += tableE
            print(tableE)
            print('\n') 

    elif x == 4:
        # Ejemplo de uso:
        input_phrase = input("Inserte la frase\n==>")
        format_phrase = salto_de_linea(input_phrase)

        fileName = input("Inserte el nombre del archivo\n==>")
        vhdl_code = generate_vhdl(format_phrase, fileName)

        # Escribir el código VHDL generado en un archivo
        filename = fileName + ".vhd"
        with open(filename, 'w') as file:
            file.write(vhdl_code)

        TextHistory += f"\tSave file {filename}"
        print(f"Archivo '{filename}' generado con el código VHDL para mostrar la frase '{input_phrase}'.")

    elif x == 5:  
        flag = False

    return flag,TextHistory,imageHistory

# Pendiente de revison
def Fisica(TextHistory,imageHistory):
    flag = True
    TextHistory += "Physics Formulario"
    ObjectHustory =[]
    
    def Ondas(Eleccion):
        if Eleccion == 1:
            pass
        elif Eleccion == 2:
            pass
        elif Eleccion == 3:
            pass
        elif Eleccion == 4:
            return False

    x = CheckIOp(1, 5,Style_Menu(["Coversor","Cuerpo Base","Electro Estatica","Ondas","Back"]))

    if x == 1:
        pass
    elif x == 2:
        pass
    elif x == 3:
        pass
    elif x == 4:
        x = CheckIOp(1, 5,Style_Menu(["Velocidad de propagacion","Efecto Doppler","Refraccion","Back"]))

    elif x == 5:
        flag = False 

    return flag,TextHistory,imageHistory

def Cinematica_Mecanismos(TextHistory,imageHistory):
    def interfaz_pedir_datos():
        """
        Interfaz de usuario para ingresar parámetros de cálculo para el perfil de levas.
        Solo recopila datos y los devuelve.
        """
        def mostrar_resumen(matriz, tipos):
            clear_screen()
            print("\n--- Resumen de datos ingresados ---")
            print("{:<10}{:<15}{:<15}{:<20}".format("Etapa", "Duración (s)", "Movimiento", "Altura (mm) / Tipo"))
            print("-" * 60)
            for i, (t, m, h, tp) in enumerate(zip(matriz[0], matriz[1], matriz[2], tipos)):
                mov = ["Ascenso", "Plano", "Descenso"][m - 1]
                curva = ["Lineal", "Armónica", "Cicloidal"][tp - 1] if m != 2 else "N/A"
                print("{:<10}{:<15}{:<15}{:<20}".format(i + 1, t, mov, f"{h} / {curva}"))

        def editar_dato(matriz, tipos):
            clear_screen()
            while True:
                print("\n--- Edición de datos ---")
                print("Seleccione una etapa para editar (0 para salir):")
                etapa = CheckIOp(0, len(matriz[0]), "Número de etapa: ")
                if etapa == 0:
                    break

                etapa -= 1  # Ajustar índice
                print(f"\nEditando etapa {etapa + 1}:")
                matriz[0][etapa] = CheckF("Duración de la etapa (s): ")
                matriz[1][etapa] = CheckIOp(1, 3, "Tipo de movimiento (1: Ascenso, 2: Plano, 3: Descenso): ")
                
                if matriz[1][etapa] == 2:
                    matriz[2][etapa] = 0
                    tipos[etapa] = 1
                else:
                    matriz[2][etapa] = CheckF("Altura asociada (mm): ")
                    tipos[etapa] = CheckIOp(1, 3, "Tipo de curva (1: Lineal, 2: Armónica, 3: Cicloidal): ")

        clear_screen()
        print("\n=== Parámetros de la leva ===")
        
        # Número de etapas
        num_etapas = CheckF("Ingrese el número de etapas: ")

        matriz_datos = [[], [], []]  # [tiempos, movimientos, alturas]
        tipo_movimiento = []
        
        for i in range(int(num_etapas)):
            clear_screen()
            print("=" * 60)
            print(f"\nEtapa {i + 1}")
            
            # Tiempo de la etapa
            matriz_datos[0].append(CheckF("\tDuración de la etapa (s): "))
            
            # Tipo de movimiento (Ascenso, Plano, Descenso)
            movimiento = CheckIOp(1, 3, "\tTipo de movimiento (1: Ascenso, 2: Plano, 3: Descenso): ")
            matriz_datos[1].append(movimiento)
            
            if movimiento == 2:
                matriz_datos[2].append(0)  # Altura es 0 para "Plano"
                tipo_movimiento.append(1)  # Tipo predeterminado para plano
            else:
                # Altura asociada
                matriz_datos[2].append(CheckF("\tAltura asociada (mm): "))
                # Tipo de curva para cada etapa
                tipo_movimiento.append(CheckIOp(1, 3, "\tTipo de curva (1: Lineal, 2: Armónica, 3: Cicloidal): "))

        # Mostrar resumen de datos
        clear_screen()
        mostrar_resumen(matriz_datos, tipo_movimiento)
        
        # Opción para editar
        while True:
            #opcion = input("\n¿Desea editar algún dato? (s/n): ").strip().lower()
            opcion = ask_continue("\n¿Desea editar algún dato? (s/n): ")
            if opcion == True:
                editar_dato(matriz_datos, tipo_movimiento)
                clear_screen()
                mostrar_resumen(matriz_datos, tipo_movimiento)
            elif opcion == False:
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        
            # Retornar la matriz
        return matriz_datos, tipo_movimiento


    y = 1
    flag = True
    while flag == True:
        datos ,tipo_movimiento = interfaz_pedir_datos()
        print("\n--- Datos ingresados ---")
        print(datos)

        y = levas_table(datos,tipo_movimiento,100,y)
        y += 1
        a = CheckIOp(1,2,"Quiere hacer otra grafica? (1: Si  2: No)")

        if a == 1:
            flag = True
        else:
            flag = False
    
    return flag,TextHistory,imageHistory

def Matematicas(TextHistory,imageHistory):
    clear_screen()
    flag = True
    TextHistory += "Matematicas para ingenieria"
    x = CheckIOp(1, 2,Style_Menu(["Metodos numericos","Exit"]))
    if x == 1:
        clear_screen()
        y = CheckIOp(1, 5,Style_Menu(["Euler","Hevn","Runge-Kutta punto medio","Todos","Exit"]))
        clear_screen()
        if y != 5:
            values =[]
            equation = input("Insert the equation example (y*sen(x)³)\n==> ")
            xi = CheckF("Insert minimun value of x") 
            xf = CheckF("Insert maximo value of x") 
            yi = CheckF("Insert start value of y")
            h = CheckF("Insert hintervalo")
            menu_Numeric(equation,xi,xf,h,xi,yi,y)
            input()
        else:
            flag = False
            
    elif x == 2:
        flag = False

    return flag,TextHistory,imageHistory

def main_menu():
    """
    Función principal que muestra el menú y maneja las selecciones del usuario.
    """

    clear_screen()
    subject = ["Sistemas Digitales","Fisica","Cinematica de Mecanismos","Matematicas","Exit"]
    inputU = CheckIOp(1, len(subject),Style_Menu(subject))
    
    return inputU

def main():
    """
    Función principal que maneja el flujo del programa.
    """
    flag = True
    hOpt = False
    # Historial
    TextHistory = "Resumen\n"
    imageHistory = 0

    while flag:
        if not hOpt:
            inputU = main_menu()
            hOpt = True

        if inputU == 1:
            print(f"Sistemas Digitales")
            # Aquí puedes implementar las opciones para "Sistemas Digitales"
            hOpt,TextHistory,imageHistory = Sistemas_Digitales(TextHistory,imageHistory) 

            # Aquí puedes implementar las opciones para "Probabilidad y estadística"
        elif inputU == 2:
            clear_screen()
            Delay_Writer("Fisica don't have UI",.04)
            Delay_Writer("....",.5)
            hOpt = False
            # Aquí puedes implementar las opciones para "Física" 

        elif inputU == 3:
            print(f"Cinematica de Mecanismos")
            hOpt,TextHistory,imageHistory = Cinematica_Mecanismos(TextHistory,imageHistory)

        elif inputU == 4:
            print(f"Matematicas")
            hOpt,TextHistory,imageHistory = Matematicas(TextHistory,imageHistory)
                
        # Funcion de Salida
        elif inputU == 5:
            flag = False
        
        # Continuar con el programa
        if hOpt and inputU != 5:
            flag = Continue()
    clear_screen()
    print(TextHistory)

if __name__ == "__main__":
    main()
