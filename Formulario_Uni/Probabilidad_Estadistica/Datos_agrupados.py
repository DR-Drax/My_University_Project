import math

class TableFrequency:
    def __init__(self, Bd) -> None:
        # Lista de datos ordenada
        self.lista = sorted(Bd)

        # Número de clases (fórmula de Sturges): K ≈ 1 + 3.322 * log10(n)
        self.k = round(1 + (3.322 * math.log10(len(Bd))))

        # Rango: valor máximo - mínimo
        self.r = self.lista[-1] - self.lista[0]

        # Amplitud: Rango dividido entre el número de clases
        self.a = round(self.r / self.k, 0)

        # Atributo para mostrar resultados como texto
        self.text = '\n'

        # Variables que almacenarán los resultados
        self.catg = []   # Límites de clases
        self.xi = []     # Puntos medios
        self.fi = []     # Frecuencia absoluta
        self.Fi = []     # Frecuencia acumulada
        self.fr = []     # Frecuencia relativa
        self.Fr = []     # Frecuencia relativa acumulada
        self.hi = []     # Porcentaje (fr * 100)
        self.xifi = []   # Producto xi * fi
        self.s2 = []     # Varianza (a implementar)
        self.media = 0   # Media (promedio)

        # Llamada a los métodos principales
        self.XI()
        self.FI()
        self.FR()
        self.XIFI()

        # Agregamos información básica al texto
        self.text += f'Dato más chico: {self.lista[0]}\n'
        self.text += f'K: {self.k}\nR: {self.r}\nAmplitud: {self.a}\n'

    def XI(self):
        """
        Construye los intervalos (límites de clase) y calcula los puntos medios (xi)
        """
        catg = [self.lista[0]]
        while catg[-1] < self.lista[-1]:
            catg.append(catg[-1] + self.a)
        self.catg = catg

        # Calculamos xi: punto medio de cada clase
        for i in range(len(catg) - 1):
            xi = (catg[i] + catg[i + 1]) / 2
            self.xi.append(xi)

    def FI(self):
        """
        Calcula la frecuencia absoluta (fi) y acumulada (Fi)
        """
        c = self.catg
        l = self.lista
        Fi = 0

        # Para cada clase, contamos cuántos datos caen en ella
        for i in range(len(c) - 1):
            x = sum(1 for j in l if c[i] <= j < c[i + 1])
            self.fi.append(x)

        # Frecuencia acumulada Fi
        for i in self.fi:
            Fi += i
            self.Fi.append(Fi)

        self.text += f'fi: {self.fi}\nFi: {self.Fi}\n'

    def FR(self):
        """
        Calcula las frecuencias relativas (fr), porcentajes (hi) y acumuladas (Fr)
        """
        n = len(self.lista)
        Fr = 0
        for i in self.fi:
            fr_i = i / n
            Fr += fr_i
            self.fr.append(fr_i)
            self.hi.append(fr_i * 100)
            self.Fr.append(round(Fr, 2))

        self.text += f'fr: {self.fr}\nFr: {self.Fr}\nhi: {self.hi}\n'

    def XIFI(self):
        """
        Calcula xi * fi y obtiene la media
        """
        m = 0
        for i in range(len(self.xi)):
            prod = self.xi[i] * self.fi[i]
            m += prod
            self.xifi.append(prod)
            self.text += f'xi[{i}]: {self.xi[i]}, fi[{i}]: {self.fi[i]}, xi*fi: {prod}\n'

        self.media = m / sum(self.fi)
        self.text += f'Media: {self.media}\n'

    def S2(self):
        """
        Aquí podrías calcular la varianza o desviación estándar, si se desea.
        """
        pass


# Ejemplo de uso:
s = [140, 160, 20, 23, 223, 60, 20, 95, 360, 70,
     220, 400, 217, 58, 235, 380, 200, 175, 85, 65]

tabla = TableFrequency(s)
print(tabla.text)
