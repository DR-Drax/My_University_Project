import math

# Variables generales 
''' Notas de variables:
    lista = Lista que almacena la base de datos
    temp = es una variable temporal donde se almacena datos enteros
    Lv = Lista de varianza

    ---------------------Pendientes de Renombre----------------------------------
    nx = Variable 'pendiente de correccion' que almacena la ubicacion de la media
    sa = variable que almacena la sumatoria de todos los datos
    -----------------------------------------------------------------------------
'''
i = 1; lista = []; temp = 0; Lv = []; sa = 0; nx = 0; mo = 0 ; Bd = []

# Variables de estadistica
'''
    Medidas de Tendencia Central (MTC)
    QK = Lista que almacena los cuartiles
    cv = Coeficiente de variacion
    ca = Coeficiente de acimetria
    
'''

def false_list():
    # s = Lista de pruevas
    
    s =[] 
    for i in range (1,50):
        #r = random(1,81)
        s.append(i)

    #s = [325, 325, 334, 339, 356, 356, 359, 359, 363, 364, 364, 366, 369, 370, 373, 373, 374, 375, 389, 392, 393, 394, 397, 402, 403, 424]
    lista=s
    lista=[4599,3342,3636,2577,2897,2002,523,4459,582]
    return lista

#Medidas de Tendencia Central (MTC)
class MTC():
    def __init__(self,Bd) -> None:
        self.lista = Bd 
        #print(self.lista)
        self.lista.sort()

        self.media = 0
        self.mediana = 0
        self.moda = 0
        self.rango = 0

        self.Texto = ('-------------------------------------------------------------------------------------'
                      +'\nDatos MTC:\n')
        self.Media(); self.Mediana(); self.Moda();self.Rango()
        self.Texto += ('-------------------------------------------------------------------------------------\n')

    def Mediana(self):
        if (len(self.lista) %2 == 0):
            nx = int(len(self.lista)-1)
            x =int(nx/2)
            media = (self.lista[x]+self.lista[x+1])/2
        
        else:
            x=int((len(self.lista)+1)/2)
            media = self.lista[x]
        self.media = media
        self.Texto += (f'La Mediana es de : {round(media,4)}\n')

    def Media(self):
        temp = 0
       
        for i in self.lista:
            temp += i
        
        mediana=temp/len(self.lista)
        
        self.mediana = mediana
        self.Texto += (f'La Media es de :{round(mediana,4)}\n')

    def Moda(self):
        mo = [x for i, x in enumerate(self.lista) if i != self.lista.index(x)]
        moda = [x for i, x in enumerate(mo) if i != mo.index(x)]
       
        if (moda == [] and mo == []):
            moda = [0]
       
        elif (moda == []):
            moda = mo

        self.moda = moda
        self.Texto += (f'La Moda es: {moda}\n')
    
    def Rango(self):
        #x = variable de posicion
        x = (len(self.lista)-1)
        self.rango = (self.lista[x]-self.lista[0])
        self.Texto += (f'Rango: {self.rango}\n')

# Medidas de Dispercion
class MD():

    def __init__(self,Bd,mediana,media) -> None:

        self.lista = Bd 
        self.lista.sort()
        #print(self.lista)
        self.desviacion = 0
        self.varianza = 0
        self.ca = 0
        self.cv = 0
        self.qk = 0

        self.Texto = ('-------------------------------------------------------------------------------------'
                      +'\nDatos MD:\n')
        self.Varianza(mediana);self.Desviacion(self.varianza);self.Cv(mediana);self.Ca(mediana,media);self.Cuartil()
        self.Texto += ('-------------------------------------------------------------------------------------')

    def Varianza(self,mediana):
        temp=0
        
        for i in self.lista:
            temp += float((i-mediana)*(i-mediana))
            Lv.append(round(float((i-mediana)*(i-mediana)),4))

        varianza = temp/(int(len(self.lista)-1))

        self.varianza = varianza
        self.Texto += (f'Varianza: {round(varianza,4)}\n')

    def Desviacion(self,varianza):
        self.desviacion = math.sqrt(varianza)
        self.Texto += (f'Desviacion: {round(self.desviacion,4)}\n')
    
    def Cv(self,mediana):
        cv = (self.desviacion/mediana)*100

        self.cv = cv
        self.Texto += (f'Coeficiente de Variacion: {round(cv,4)}\n')
    
    def Ca(self,mediana,media):

        ca = ((3*(mediana-media))/self.desviacion)
        self.ca = ca
        self.Texto += (f'Coeficiente de Acimetria: {round(ca,4)}\n')
    
    def Cuartil(self):
        temp = 0; QK = []

        #No de datos = nd
        nd = len(self.lista)
        self.Texto += ('\n')
       
        for i in range(1,4):

            qk = ((i * nd)/4)

            if (qk %2==0  and i != 2):
                qk = int(qk)
                x = (self.lista[qk-1])
                self.Texto += (f'Cuartil {i}: \nQk{i}: {x}, es exacto ,Posicion {qk}\n')
           
            else:
                qk = int(qk)
                #pro = promedio
                pro = (self.lista[qk]+self.lista[qk-1])/2
                self.Texto += (f'Cuartil {i}, suma de {qk} y {qk-1}' 
                      f'\nPromedio ={pro}\n')

def Results(Bd):
    text = MTC(Bd).Texto
    text += MD(Bd,MTC(Bd).mediana,MTC(Bd).media).Texto
    return text

#funcion de pruevas          
def test():
    Bd = false_list()
    s=Bd.sort()
    
    print(Results(Bd))
    
test()