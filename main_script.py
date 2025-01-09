import os

#________User System__________#
from System_User.InputUser import check_num_input as CheckIOp
from System_User.InputUser import check_float_input as CheckF
from System_User.PySisteam import *

#__________Formulario Physics_____#
from Formulario_Uni.Fisica.Ondas import *

#__________Probablidad________#
from Formulario_Uni.Probabilidad_Estadistica import *

#from Sistemas_Digitales import conversion_simplificado
from Control_Motores.tra import *

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

# Pendiente de revison
def Probabilidad(TextHistory,imageHistory):

    x = CheckIOp(1, 5,Style_Menu(["Datos agrupados","Datos no agrupados","Back"]))
    if x == 1:
        print("Hola 1") 
    elif x == 2:
        print("Hola 2")
    elif x == 3:
        flag = False  # Regresa al menú principal

    return flag,TextHistory,imageHistory

def Control_motores(TextHistory,imageHistory):
    flag = True
    TextHistory += "\nControl de Motores\n"
    """
    Función para manejar las opciones del menú de Control de Motores.
    """

    clear_screen()
    x = CheckIOp(1, 4,Style_Menu(["Voltaje pico","Corriente máxima","Gráfica de ondas","Back"]))
    
    if x == 1:
        voltage = VoltajePico(CheckF("Insert Voltage"))

        TextHistory += f'\tVoltaje pico: {round(voltage, 4)}\n'
        print(f'Voltaje pico: {round(voltage, 4)}') 

    elif x == 2:
        current = CorrienteMax(CheckF("Insert amperage"))

        TextHistory += f'\tCorriente máxima: {round(current, 4)}'
        print(f'Corriente máxima: {round(current, 4)}\n')  

    elif x == 3: 
        x = CheckIOp(1,2,"Do you hava the exact values\n"+Style_Menu(["Si","No"]))

        if x == 2:
            Frec, Vefectivo, Iefectivo, fase_grados,imga = graficar_ondas(CheckF("Frecuencia"),
                        VoltajePico(CheckF("Voltaje [Directa de la fuente]")),
                        CorrienteMax(CheckF("Corriente [Administrada]")),
                        CheckF("Grados"),
                        CheckIOp(1, 2,"Do you want save imgae\n"+Style_Menu(["Yes","No"])),
                        f"Graphic {imageHistory + 1}")
        else:
            Frec, Vefectivo, Iefectivo, fase_grados,imga = graficar_ondas(CheckF("Frecuencia"),
                        CheckF("Voltaje [Rms]"),
                        CheckF("Corriente [Administrada]"),
                        CheckF("Grados"),
                        CheckIOp(1, 2,"Do you want save imgae\n"+Style_Menu(["Yes","No"])),
                        f"Graphic {imageHistory + 1}")
        if imga:
            imageHistory += 1
            TextHistory += (f"\tData Graphic {imageHistory}\n")

        else:
            TextHistory += (f"\tNot save graphic \n")

        TextHistory += (    f"\tFrecuencia: {Frec}\n"+
                            f"\tVoltaje efectivo: {Vefectivo}\n"+
                            f"\tCorriente efectiva: {Iefectivo}\n"+
                            f"\tFase grados: {fase_grados}")

    elif x == 4:
        flag = False  # Regresa al menú principal
    return flag,TextHistory,imageHistory

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
    inputU = CheckIOp(1, 6,Style_Menu(["Sistemas Digitales","Probabilidad y estadística","Física","Control de Motores","Matematicas","Exit"]))
    
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

        elif inputU == 2:
            clear_screen()
            Delay_Writer("Probabilidad don't have UI",.04)
            Delay_Writer("....",.5)
            hOpt = False
            """print(f"Probabilidad y estadística en desarrollo.")
            hOpt,TextHistory,imageHistory = Probabilidad(TextHistory,imageHistory) """

            # Aquí puedes implementar las opciones para "Probabilidad y estadística"
        elif inputU == 3:
            clear_screen()
            Delay_Writer("Fisica don't have UI",.04)
            Delay_Writer("....",.5)
            hOpt = False
            # Aquí puedes implementar las opciones para "Física"
        elif inputU == 4:
            hOpt,TextHistory,imageHistory = Control_motores(TextHistory,imageHistory)  # Si regresa False, reactivar el menú principal
        
        elif inputU == 5:
            print(f"Matematicas")
            hOpt,TextHistory,imageHistory = Matematicas(TextHistory,imageHistory)
        
        elif inputU == 6:
            flag = False

        if hOpt and inputU != 6:
            flag = Continue()
    clear_screen()
    print(TextHistory)

if __name__ == "__main__":
    main()
