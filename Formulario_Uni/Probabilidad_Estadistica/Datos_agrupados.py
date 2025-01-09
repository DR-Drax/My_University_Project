import math

class Table_Frecuency():
    def __init__(self,Bd) -> None:
        self.lista = Bd
        self.k = 1 + (3.322* (math.log10(len(Bd))))
        self.r = (Bd[(-1)]-Bd[0])
        self.a = round((self.r/self.k),0)
      
        self.text = '\n' 
        self.catg = []
        self.xi = []
        self.fi = []
        self.Fi = []
        self.fr = []
        self.Fr = []
        self.hi = []
        self.xifi = []
        self.s2 = []
        self.media = 0
        self.XI();self.FI();self.FR();self.XIFI()


        self.text += (f'dato mas chico {Bd[0]}')
        self.text += (f'K:{self.k}\nR: {self.r} \nAmplitud {self.a}')
    
    def XI(self):

        #c es la condciocion para seguir
        c = True
        catg =[]
        catg.append(self.lista[0])
        while(c == True):
            if (self.lista[-1] <= catg[-1]):
                c = False
            else:
                catg.append(((catg[-1]+self.a)))
        self.catg = catg
        for i in range(len(catg)):
            if (i != len(catg)-1):
                xi = (catg[i]+catg[i+1])/2
                self.xi.append(xi)
            else:
                break
   
    def FI(self):
        c = self.catg
        l = self.lista
        Fi = 0
        for i in range(0,len(c)):
            x = 0 
            for j in l:
                if (j >= c[i] and j< c[i+1]):
                    #print(f'{i} - {j}')
                    x += 1
                else:
                    pass
            if (x > 0):
                self.fi.append(x)
            else:
                pass
        
        for i in self.fi:
            Fi += i
            self.Fi.append(Fi)

        self.text += str(self.fi,self.Fi)
    
    def FR(self):
        for i in self.fi:
            n = len(self.lista)
            self.fr.append((i/n))
        Fr = 0
        for i in self.fr:
            Fr += i
            self.hi.append(i*100)
            self.Fr.append(round(Fr,2))
        self.text += (f'\n{self.fr}\n{self.Fr}\n{self.hi}')
    
    def XIFI(self):
        x = self.xi
        f = self.fi
        m = 0
        for i in range(0,len(x)-1):
            m += (x[i]*f[i]) 
            self.text += (x[i])
            self.xifi.append((x[i]*f[i]))
        me = (m/len(x))
        self.text += (f'{me}')

    def S2(self):
        pass
    

s = [140,160, 20, 23, 223, 60, 20, 95, 360, 70,
220, 400, 217, 58, 235, 380, 200, 175, 85, 65]
s.sort()

print(Table_Frecuency(s).text)