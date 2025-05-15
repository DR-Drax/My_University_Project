import string
#from Num_Systen import *

def generate_binary_lists(binary_str):
    """
    Genera diccionarios con la representación binaria original y modificada.
    
    Parámetros:
    binary_str (str): Número binario en formato string.

    Retorno:
    tuple: Diccionarios con representaciones binarias originales y modificadas.
    """
    original_dict = {}
    modified_dict = {}
    letters = string.ascii_lowercase

    for i in range(len(binary_str)):
        original_value = binary_str[0:i+1]
        original_dict[letters[i]] = original_value
        
        modified_value = original_value[:-1] + ('1' if original_value[-1] == '0' else '0')
        modified_dict[letters[i]] = modified_value
    
    return original_dict, modified_dict

def create_match_list(original_dict, modified_dict):
    """
    Crea un diccionario con coincidencias entre listas binarias originales y modificadas.
    
    Parámetros:
    original_dict (dict): Diccionario de listas binarias originales.
    modified_dict (dict): Diccionario de listas binarias modificadas.

    Retorno:
    dict: Diccionario con las coincidencias.
    """
    match_dict = {}

    original_keys = list(original_dict.keys())
    original_values = list(original_dict.values())
    modified_keys = list(modified_dict.keys())
    modified_values = list(modified_dict.values())

    for mod_index, mod_value in enumerate(modified_values):
        for orig_index, orig_value in enumerate(original_values):
            if len(orig_value) == len(mod_value) and orig_value == mod_value:
                match_dict[modified_keys[mod_index]] = mod_value
            elif len(orig_value) != len(mod_value) and orig_value == mod_value[-len(orig_value):]:
                match_dict[modified_keys[mod_index]] = mod_value[-len(orig_value):]
    
    return match_dict

def create_binary_letter_map(binary_dict):
    """
    Crea un diccionario de letras correspondientes a una secuencia binaria.
    
    Parámetros:
    binary_dict (dict): Diccionario de listas binarias.

    Retorno:
    dict: Diccionario de letras con valores binarios "0" o "1".
    """
    letter_map = {}
    num_sequence = ""

    letters = list(binary_dict.keys())
    binaries = list(binary_dict.values())
    
    for i in range(len(binary_dict)):
        binNumber = binaries[i]
        if  binNumber [i:]== "0":
            num_sequence += "0"
            letter_map[letters[i]] = "0"
        elif binNumber [i:] == "1":
            num_sequence += "1"
            letter_map[letters[i]] = "1"
    
    return letter_map

def compare_binary_lists(original_dict, modified_dict):
    """
    Compara dos diccionarios con listas binarias y genera un nuevo diccionario basado en las coincidencias.

    Parámetros:
    original_dict (dict): Diccionario con listas binarias originales.
    modified_dict (dict): Diccionario con listas binarias modificadas.

    Retorno:
    dict: Diccionario resultante de la comparación.
    """
    # Diccionario para almacenar coincidencias
    matched_dict = {}
    # Diccionario para almacenar el resultado final
    result_dict = {}
    
    # Extraer claves y valores de los diccionarios
    original_keys = list(original_dict.keys())
    original_values = list(original_dict.values())
    modified_keys = list(modified_dict.keys())
    modified_values = list(modified_dict.values())

    # Comparar valores binarios y llenar el diccionario de coincidencias
    for i, modified_value in enumerate(modified_values):
        match_found = False
        for j, original_value in enumerate(original_values):
            if modified_value == original_value:
                next_key = original_keys[j + 1] if j + 1 < len(original_keys) else 'None'
                matched_dict[modified_keys[i]] = next_key
                match_found = True
                break
        if not match_found:
            matched_dict[modified_keys[i]] = 'No match'

    # Comparar y construir el diccionario de resultados finales
    for i, original_key in enumerate(original_keys):
        if original_key in matched_dict:
            next_state = matched_dict[original_key]
            result_dict[original_key] = next_state
        else:
            result_dict[original_key] = 'a'
    
    return result_dict

def display_results(original_letter_map, final_comparison, number, bin_value):
    """
    Muestra los resultados comparando el mapa original con el mapa de comparación.

    Parámetros:
    original_letter_map (dict): Diccionario de letras con valores binarios originales.
    final_comparison (dict): Diccionario de letras resultantes de la comparación.
    number (int): Número original.
    bin_value (str): Valor binario del número original.
    """
    original_keys = list(original_letter_map.keys())
    original_values = list(original_letter_map.values())
    modified_values = list(final_comparison.values())

    output = ""

    output += "╔═══════════════╦═══════════════════════════════╗\n"
    output += f"║Number: {number}\t║Bin: {bin_value}\t\t\t║\n"
    output += "╟═══════════════╬═══════╦═══════════════╦═══════╢\n"
    output += "║Current State\t║Input\t║Next State\t║Output\t║\n"
    output += "╟═══════════════║═══════║═══════════════║═══════╢\n"

    for i in range(len(original_keys)):
        if original_values[i] == "0" and (i + 1) < len(original_keys):
            output += f"║\t{original_keys[i]}\t║  0\t║\t{original_keys[i + 1].upper()}\t║   0\t║\n"
            output += f"║\t{original_keys[i]}\t║  1\t║\t{modified_values[i]}\t║   0\t║\n"
            output += "╟═══════════════║═══════║═══════════════║═══════╢\n"

        elif original_values[i] == "1" and (i + 1) < len(original_keys):
            output += f"║\t{original_keys[i]}\t║  0\t║\t{modified_values[i]}\t║   0\t║\n"
            output += f"║\t{original_keys[i]}\t║  1\t║\t{original_keys[i + 1].upper()}\t║   0\t║\n"
            output += "╟═══════════════║═══════║═══════════════║═══════╢\n"

        elif original_values[i] == "1" and (i + 1) == len(original_keys):
            output += f"║\t{original_keys[i]}\t║  0\t║\t{modified_values[i]}\t║   0\t║\n"
            output += f"║\t{original_keys[i]}\t║  1\t║\tA\t║   1\t║\n"
            output += "╚═══════════════╩═══════╩═══════════════╩═══════╝\n"

        elif original_values[i] == "0" and (i + 1) == len(original_keys):
            output += f"║\t{original_keys[i]}\t║  0\t║\tA\t║   1\t║\n"
            output += f"║\t{original_keys[i]}\t║  1\t║\t{modified_values[i]}\t║   0\t║\n"
            output += "╚═══════════════╩═══════╩═══════════════╩═══════╝\n"

    return output

def create(number,binary_number):
    
    #binary_number = decimal_to_binary(number)

    original_list, modified_list = generate_binary_lists(binary_number)

    original_letter_map = create_binary_letter_map(original_list)

    #modified_letter_map = create_binary_letter_map(modified_list)

    match_list = create_match_list(original_list, modified_list)

    final_comparison = compare_binary_lists(original_list, match_list)

    return display_results(original_letter_map,final_comparison,number,binary_number)

def get_number_list():
    """
    Solicita al usuario que ingrese una lista de números separados por comas.
    Valida que todos los elementos sean números enteros y devuelve la lista.
    """
    while True:
        user_input = input("Ingrese una lista de números separados por comas (ejemplo: 180,15,2): ")
        # Elimina espacios y divide la entrada en elementos separados por comas
        items = [item.strip() for item in user_input.split(',')]
        
        try:
            # Intenta convertir cada elemento a entero
            numbers = [int(item) for item in items]
            return numbers
        except ValueError:
            # Si ocurre un error de conversión, muestra un mensaje y vuelve a solicitar la entrada
            print("Error: Todos los valores deben ser números enteros. Intente de nuevo.")
