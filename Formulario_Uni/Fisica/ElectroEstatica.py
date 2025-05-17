import math

Constante_de_proporcionalidad_K_=9*(pow(10,9))


#------------------------------------------- Ley de Cooulmb -----------------------------------------------------------#
class LEY_COULOMB:
    def __init__(self,q1,q2,distancia_entre_cargas,Energia_Potencial_Electrica):
        self.S_Energia_Potencial_Electrica = Energia_Potencial_Electrica
        self.S_Distancia_entre_cargas_r = distancia_entre_cargas
        self.S_Q1 = q1
        self.S_Q2 = q2

    def energia_potencial_E(self):
        k = Constante_de_proporcionalidad_K_

        r = self.S_Distancia_entre_cargas_r * self.S_Distancia_entre_cargas_r

        self.S_Energia_Potencial_Electrica = k * ((self.S_Q1 * self.S_Q2) / r)

        #Energia Potencial Electrica {self.S_Energia_Potencial_Electrica} J\n ó \n"
        return f"Fuerza: {self.S_Energia_Potencial_Electrica} N"

# """"""""""""""""""Pendiente de investigacion """"""""""""""""""""""""""""""""""""#
    def magnitud(self,grado1,grado2,energia_potencial1,energia_potencial2):
        fx1 = energia_potencial1 * math.sin(grado1)
        fx2 = energia_potencial2 * math.sin(grado2)
        fy1 = energia_potencial1 * math.cos(grado1)
        fy2 = energia_potencial2 * math.cos(grado2)

        fx = fx1 - fx2
        fy = fy1 + fy2

        fq = math.sqrt((fx ** 2) + (fy ** 2))
        x = pow(10,9)
        grado = math.degrees(math.atan(fq))

        return (f"Grado = {grado} \nfq {fq} fy = {fy}")
# """"""""""""""""""Pendiente de investigacion """"""""""""""""""""""""""""""""""""#
