def check_num_input(min_limit, max_limit, prompt =""):
    """
    Solicita al usuario un número entero dentro de un rango válido.
    
    Parámetros:
    - min_limit: Límite inferior del rango.
    - max_limit: Límite superior del rango.
    - prompt: Mensaje mostrado al usuario.

    Retorna:
    - Un número entero válido dentro de los límites.
    """
    while True:
        try:
            num = int(input(f"{prompt}\n\t==> "))
            if min_limit <= num <= max_limit:
                return num
            print(f"Enter a number between {min_limit} and {max_limit}.")
        except ValueError:
            print("Enter a valid number.")

def check_option(options):
    while True:
        data = input("\n==> ").strip()  # Elimina espacios en blanco al inicio y al final
        if data in options:
            return data
        else:
            print(f"Ingresa una opción válida: {', '.join(options)}")

        


def check_float_input(prompt=""):
    """
    Solicita al usuario un número flotante válido.
    
    Parámetro:
    - prompt: Mensaje mostrado al usuario.

    Retorna:
    - Un número flotante válido.
    """
    while True:
        try:
            return float(input(f"{prompt}\n\t==> "))
        except ValueError:
            print("Enter a valid number.")

def check_int_input(prompt=""):
    """
    Solicita al usuario un número entero válido.
    
    Parámetro:
    - prompt: Mensaje mostrado al usuario.

    Retorna:
    - Un número entero válido.
    """
    while True:
        try:
            return int(input(f"{prompt}\n\t==> "))
        except ValueError:
            print("Enter a valid number.")
