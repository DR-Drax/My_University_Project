class Table_Frecuency():
    def __init__(self, Bd) -> None:
        self.lista = Bd
        self.k = 1 + (3.322 * (math.log10(len(Bd))))
        self.r = (Bd[(-1)] - Bd[0])
        self.a = round((self.r / self.k), 0)
        
        # Variables que vamos a calcular
        self.catg = []
        self.xi = []
        self.fi = []
        self.Fi = []
        self.fr = []
        self.Fr = []
        self.hi = []
        self.xifi = []
        self.media = 0
        
        # Inicializamos los cálculos
        self.XI()
        self.FI()
        self.FR()
        self.XIFI()
    
    def XI(self):
        """Calcula los intervalos de clase (categorías) y las marcas de clase (xi)."""
        c = True
        self.catg.append(self.lista[0])
        while c:
            if self.lista[-1] <= self.catg[-1]:
                c = False
            else:
                self.catg.append(self.catg[-1] + self.a)
        for i in range(len(self.catg) - 1):
            xi = (self.catg[i] + self.catg[i + 1]) / 2
            self.xi.append(xi)
    
    def FI(self):
        """Calcula la frecuencia absoluta (fi) y acumulada (Fi)."""
        for i in range(len(self.catg) - 1):
            x = sum(self.catg[i] <= j < self.catg[i + 1] for j in self.lista)
            self.fi.append(x)
        Fi = 0
        for i in self.fi:
            Fi += i
            self.Fi.append(Fi)
    
    def FR(self):
        """Calcula la frecuencia relativa (fr) y relativa acumulada (Fr)."""
        total = len(self.lista)
        Fr = 0
        for i in self.fi:
            fr = i / total
            self.fr.append(fr)
            Fr += fr
            self.Fr.append(round(Fr, 2))
            self.hi.append(fr * 100)
    
    def XIFI(self):
        """Calcula el producto de las marcas de clase (xi) por las frecuencias (fi), y la media."""
        m = 0
        for i in range(len(self.fi)):
            m += self.xi[i] * self.fi[i]
            self.xifi.append(self.xi[i] * self.fi[i])
        self.media = m / sum(self.fi)
    
    def format_table(self):
        """Genera el formato de la tabla en una cadena de texto."""

        # Definir el ancho de las columnas
        range_col_width = 16
        fi_col_width = 20
        fi_acum_col_width = 22
        fr_col_width = 15
        hi_col_width = 15
        media_col_width = 22

        # Crear la tabla para frecuencias absolutas
        table = (
            f"╔{'═' * (fi_acum_col_width + 2)}╦{'═' * (fr_col_width + 2)}╦{'═' * (hi_col_width + 2)}╗\n"
            f"║ {('Frecuencia Acumulada').center(fi_acum_col_width)} ║ {('Frecuencia Relativa').center(fr_col_width)} ║ {('Porcentaje (%)').center(hi_col_width)} ║\n"
            f"╟{'═' * (fi_acum_col_width + 2)}╬{'═' * (fr_col_width + 2)}╬{'═' * (hi_col_width + 2)}╢\n"
        )
        for i in range(len(self.fi)):
            fi_acum_str = f"{self.Fi[i]:<5}"
            fr_str = f"{self.fr[i]:<6.2f}"
            hi_str = f"{self.hi[i]:<6.2f}%"
            table += f"║ {fi_acum_str.center(fi_acum_col_width)} ║ {fr_str.center(fr_col_width)} ║ {hi_str.center(hi_col_width)} ║\n"
        
        table += (
            f"╚{'═' * (fi_acum_col_width + 2)}╩{'═' * (fr_col_width + 2)}╩{'═' * (hi_col_width + 2)}╝\n\n"
            f"╔{'═' * (media_col_width + 2)}╦{'═' * (media_col_width + 2)}╗\n"
            f"║ {('Media').center(media_col_width)} ║ {f'{self.media:.2f}'.center(media_col_width)} ║\n"
            f"╚{'═' * (media_col_width + 2)}╩{'═' * (media_col_width + 2)}╝\n"
        )
        return table





# Ejemplo de uso:
import math

datos = [140,160, 20, 23, 223, 60, 20, 95, 360, 70,
220, 400, 217, 58, 235, 380, 200, 175, 85, 65]
datos.sort()

# Crear instancia y calcular la tabla de frecuencias
tabla_frec = Table_Frecuency(datos)

# Guardar la tabla en una variable
resultado_formateado = tabla_frec.format_table()

# Imprimir la tabla desde la variable
print(resultado_formateado)
