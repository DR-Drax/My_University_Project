import math
import numpy as np
import matplotlib.pyplot as plt

def graficar_ondas(Frec, Vefectivo, Iefectivo, fase_grados,opt,filename):
    # Calcular valores máximos a partir de los efectivos
    Vmax = Vefectivo * np.sqrt(2)  # Voltaje máximo
    Imax = Iefectivo * np.sqrt(2)  # Corriente máxima
    fase = np.deg2rad(fase_grados)  # Convertir el retraso de fase a radianes
    
    # Generar vector de tiempo para un ciclo
    t = np.linspace(0, 1/Frec, 1000)
    
    # Ondas de voltaje y corriente
    E = Vmax * np.sin(2 * np.pi * Frec * t)  # Onda de voltaje
    I = Imax * np.sin(2 * np.pi * Frec * t - fase)  # Onda de corriente con retraso de fase
    
    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(t, E, label=f'Voltaje (E) = {round(Vefectivo,4)}', color='blue')
    plt.plot(t, I, label=f'Corriente (I) = {round(Iefectivo,4)}', color='red')
    plt.title('Formas de Onda de Voltaje y Corriente')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid(True)
    
    if opt == 1:
        plt.savefig(filename)
        print(f"Gráfico guardado como {filename}")
        plt.show()
        return round(Frec,4),round(Vefectivo,4), round(Iefectivo,4),round(fase_grados,4),True
        
    else:
        plt.show()
        return round(Frec,4),round(Vefectivo,4), round(Iefectivo,4),round(fase_grados,4) ,False

def VoltajePico(Volt):
    return (Volt*math.sqrt(2))

def act2 ():
    pass

def CorrienteMax(Amper):
    return (Amper*math.sqrt(2))