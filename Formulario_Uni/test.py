# Importar la clase DopplerEffect
from Fisica.Ondas import DopplerEffect

# Crear una instancia de la clase DopplerEffect
doppler1 = DopplerEffect(400, 0, 340, 0, 20)

# Llamar al método observer_frequency para calcular la frecuencia del observador
observer_freq = doppler1.observer_frequency()

# Imprimir el resultado
print(f"\nFo = {observer_freq}")

# Crear otra instancia de la clase DopplerEffect
doppler2 = DopplerEffect(0, 377.77, 340, 0, 20)

# Llamar al método source_frequency para calcular la frecuencia de la fuente
source_freq = doppler2.source_frequency()

# Imprimir el resultado
print(f"\nFs = {source_freq}")

# Crear otra instancia de la clase DopplerEffect
#DopplerEffect(frecuencia_real_f=400, frecuencia_real_o=377.77, vel_Real=0, vel_observador_v0=0, vel_fuente_vf=20)
doppler3 = DopplerEffect(400, 377.77, 340, 0, 0)

# Llamar al método source_velocity para calcular la velocidad de la fuente
source_vel = doppler3.source_velocity()

# Imprimir el resultado
print(f"\nVs = {source_vel}")

# Crear otra instancia de la clase DopplerEffect
doppler4 = DopplerEffect(400, 377.77, 0, 0, 20)

# Llamar al método real_velocity para calcular la velocidad real
real_vel = doppler4.real_velocity()

# Imprimir el resultado
print(f"\nV = {real_vel}")
