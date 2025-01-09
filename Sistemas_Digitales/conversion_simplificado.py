from pyeda.inter import exprvars, truthtable, truthtable2expr

def bin_to_expr(binary_string):
    n = len(binary_string)
    vars = exprvars('x', n)
    
    # Create a truth table from the binary string
    tt = truthtable(vars, list(map(int, binary_string)))
    
    # Convert the truth table to a simplified expression
    simplified_expr = truthtable2expr(tt)
    
    return simplified_expr

binary_string = "1011"  # Ejemplo de entrada binaria
simplified_expr = bin_to_expr(binary_string)
print(f"Ecuación simplificada: {simplified_expr}")
