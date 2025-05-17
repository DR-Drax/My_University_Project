"""
Nombre del archivo: Ondas.py
Descripción: Creacion de objetos con las propiedades de las ondas correspondientes
Autor: Samuel V. Hdz.
Fecha: 2024-05-06
"""


import math
import sys
import os


# ---------------Datos Globales-----------------------------------------#
# *************Rapidez_del_Sonido*********#
class RAPIDEZ_DEL_SONIDO:
    def __init__(self, velocidad_v,temperatura):
        self.S_Velocidad = velocidad_v # Velocidad (m/s)
        self.S_Temperatura = temperatura # Temperatura en °K

    def consulta(self):
        return (f"Velocidad : {self.S_Velocidad} m/s\n"
                f"Temperatura : {self.S_Temperatura} °K")

#+++++MATERIALES Y CARACTERISTICAS [Velocidad,Temperatura]++++++++++++++#
Aire=RAPIDEZ_DEL_SONIDO(340, 288)

Agua=RAPIDEZ_DEL_SONIDO(1435, 281)

Oxigeno=RAPIDEZ_DEL_SONIDO(317, 273)

Hierro =RAPIDEZ_DEL_SONIDO(5130, 293)

Aluminio=RAPIDEZ_DEL_SONIDO(5100, 293)

Vidrio=RAPIDEZ_DEL_SONIDO(4500, 293)


# ****************************************#

# *-------------------------------------------Caracteristicas de las Ondas-------------------------------------------- #
def FRECUENCIA(Periodo):
    # ------------------------------------------------------------------ #
    # Es el numero de veces por segundo en la que se repite un ciclo
    # (cuando las ondas cierran el circulo/obalo)
    # y se mide en ciclos/s ó Hertz (Hz)
    # ------------------------------------------------------------------ #
    Frecuencia = 1 / Periodo  # f = Frecuancia en ciclos == Hz
        
    print(f"Frecuencia : {Frecuencia} Hz")

    return Frecuencia

def PERIODO(frecuencia):
    # ------------------------------------------------------------------ #
    # Es el tiempo que tarda en realizarse un cliclo de la onda
    # el periodo es igual al inverso de la frecuencia y diceversa
    # ------------------------------------------------------------------ #
    Periodo = 1 / frecuencia  # T = Periodo en seg/ciclo
        # f = Frecuancia en ciclos = Hz

    print((f"Periodo : {Periodo} s/ciclos"))

    return Periodo
#______________________________________________________________________________________________________________________#

# ------------------------------------------Refracción y Difraccion de Ondas------------------------------------------ #
class VELOCIDAD_DE_PROPAGACION:
    # ------------------------------------------------------------------ #
    # Es la distancia que una determinada cresta o valle recorre en
    # determinado tiempo.
    # La velocicidad con la que se propaga una onda está en funcion de
    # la elasticidad y de la dencidad del medio; mientras éste es mas
    # elastico y menos denson, la rapidez de propagacion sera mayor
    # ------------------------------------------------------------------ #

    def __init__(self, Longitud_Onda_Λ, frecuencia_f,periodo_T):
        '''self es para nombrar un "atributo" o un diferenciador del objeto y sus caracteristicas
            Cuando se escribe "self.atributo=atributo" es para asignar un atributo unico para cada
            objeto -Solo es para consulta no se puede editar -'''

        self.S_Longitud_de_onda = Longitud_Onda_Λ   # Longitud de onda --- m/ciclo
        self.S_Frecuencia = frecuencia_f    # Frecuenia --- Hz
        self.S_Periodo = periodo_T  # Periodo --- seg/ciclo

        self.S_Velocidad = None

    # Velocidad de propagacion teniendo:
    # Longitud de onda y Frecuencia

    def Velocidad_con_f(self):

        self.S_Velocidad = self.S_Longitud_de_onda * self.S_Frecuencia
        return (f"Velocidad: {self.S_Velocidad} m/s")

    # Velocidad de propagacion teniendo:
    # Longitud de onda y Periodo
    def Velocidad_con_T(self):

        self.S_Velocidad = self.S_Longitud_de_onda / self.S_Periodo
        return (f"Velocidad: {self.S_Velocidad} m/s")

    # Frecuencia teniendo:
    # Velocidad de onda y Longitud de onda
    def Frecuencia(self):

        self.S_Frecuencia = self.S_Velocidad / self.S_Longitud_de_onda
        return (f"Frecuencia : {self.S_Frecuencia} Hz")

    # Periodo teniendo:
    # Velocidad de onda y Longitud de onda
    def Periodo(self):

        self.S_Periodo = self.S_Velocidad * self.S_Longitud_de_onda
        return (f"Periodo : {self.S_Periodo} m/ciclo")

    # Longitud de onda teniendo:
    # Velociadad de onda y Frecuencia
    def Longitud_de_onda_f(self):
        self.S_Longitud_de_onda = self.S_Velocidad / self.S_Frecuencia
        return (f"Longitud de onda : {self.S_Longitud_de_onda} m/ciclo")

    # Longitud de onda teniendo:
    # Velociadad de onda y Periodo
    def Longitud_de_onda_T(self):
        self.S_Longitud_de_onda = self.S_Velocidad * self.S_Periodo
        return (f"Longitud de onda : {self.S_Longitud_de_onda} m/ciclo")

#--------------------------------------------Efecto Doppler------------------------------------------------------------#
class EFECTO_DOPPLER:
    

    def __init__(self, frecuencia_real_f,frecuencia_real_o, vel_Real, vel_observador_v0, vel_fuente_vf):
        self.S_Frecuencia_Observador = frecuencia_real_o
        self.S_Frecuencia_Fuente = frecuencia_real_f

        self.S_Vel_Fuente_sonora = vel_fuente_vf  
        self.S_Vel_Observador = vel_observador_v0  
        self.S_Vel_Real = vel_Real  

    def Frecuencia_Observador(self):
        
        
        self.S_Frecuencia_Observador = ((self.S_Frecuencia_Fuente(self.S_Vel_Real + self.S_Vel_Observador))
                                            /(self.S_Vel_Real-self.S_Vel_Fuente_sonora))
        print (self.S_Frecuencia_Observador)
   
    def Frecuenia_Fuente(self):
        

        self.S_Frecuencia_Fuente = ((self.S_Frecuencia_Observador(self.S_Vel_Real - self.S_Vel_Fuente_sonora)
                                        /(self.S_Vel_Real + self.S_Vel_Observador)))

    def Velocidad_Fuente(self):
        self.S_Vel_Fuente_sonora = -((self.Frecuenia_Fuente(self.S_Vel_Real+self.S_Vel_Observador))
                                        (self.Frecuencia_Observador)) - self.S_Vel_Real

    def Velocidad_Real(self):
        self.S_Vel_Real = (self.Frecuencia_Fuente/self.Frecuencia_Observador) + self.S_Vel_Fuente_sonora - self.S_Vel_Observador

    def DopplerData(self):
        return (f"La Frecuencia aparente Cerca es: {self.Frecuencia_Apernte_Cerca} Hz\n"
                f"La Frecuencia aparente Lejana es: {self.Frecuencia_Apernte_Lejana} Hz")

class DopplerEffect:
    # El Efexto Doppler consiste en un cambio aparente en la frecuencia de un sonido
    # durante el movimiento relativo de entre el OBSERVADOR y la FUENTE SONORA
    
    def __init__(self, real_frequency_f, real_frequency_o, real_velocity_a, observer_velocity_v0, source_velocity_vf):
        self.real_frequency_observer = real_frequency_o
        self.real_frequency_source = real_frequency_f

        self.source_velocity_s = source_velocity_vf # Velocidad de la fuete sonora (m/s)
        self.observer_velocity_o = observer_velocity_v0 # Velocidad del observador (m/s)
        self.real_velocity_A = real_velocity_a # Velocidad Real (m/s)

    def observer_frequency(self):
        # fo = [fs(v+vo)]/(v-vs)

        self.real_frequency_observer = (self.real_frequency_source * (self.real_velocity_A + self.observer_velocity_o)) / (
                self.real_velocity_A - self.source_velocity_s)
        
        return self.real_frequency_observer

    def source_frequency(self):
        # fs = [fo(v-vs)]/(v-vo)

        self.real_frequency_source = (self.real_frequency_observer * (self.real_velocity_A - self.source_velocity_s)) / (
                self.real_velocity_A + self.observer_velocity_o)
        
        return self.real_frequency_source

    def source_velocity(self):
        self.source_velocity_s = -((self.real_frequency_source * (self.real_velocity_A + self.observer_velocity_o)) / (
                self.observer_frequency())) - self.real_velocity_A
        return self.source_velocity_s

    def real_velocity(self):
        self.real_velocity_A = (self.source_velocity_s - self.observer_velocity_o) / (self.real_frequency_source / self.real_frequency_observer)  
        return self.real_velocity_A

#----------------------------------------------- Refreccion -----------------------------------------------------------#
class REFRACCION:

    def __init__(self, v, f, λ):
        self.S_Longitud_Onda = λ  # ***+ Se mide en m/ciclo
        self.S_Frecuencia = f  # ***+ Se mide en m/ciclo o hz
        self.S_Velocidad_Propagacion = v  # ***+ Se mide en m/s

        if v == 0:
            self.VELOCIDAD()
        elif f == 0:
            self.FRECUENCIA()
        elif λ == 0:
            self.LONGITUD_ONDA()

    def FRECUENCIA(self):
        # f = v / λ

        self.S_Frecuencia = self.S_Velocidad_Propagacion / self.S_Longitud_Onda
        return f"{self.S_Frecuencia} hz"

    def VELOCIDAD(self):
        # v = λ * f

        self.S_Velocidad_Propagacion = self.S_Longitud_Onda * self.S_Frecuencia
        return f"{self.S_Velocidad_Propagacion} m/s"

    def LONGITUD_ONDA(self):
        # λ = v/f

        self.S_Longitud_Onda = self.S_Velocidad_Propagacion/self.S_Frecuencia
        return f"{self.S_Longitud_Onda} m/ciclo"

"""
def main():
    print("Que Calculo que quiere realizar:\n1) Frecuencia\n2) Periodo"+
        "\n3) Velocidad de Propagacion\n4) Efecto_Doppler\n5) Refraccion")
    opc = check_input(1,6)
    print("Este programa por defecto guarda los calculos como 'Frecuencia 1'"+
        "Si quiere cambiar su nombre precione 2 de lo contrario 1 ")
    form = check_input(1,2)
    Opciones(opc,form)

if __name__ == "__main__":
    os.system("clear")
    main()


"""
