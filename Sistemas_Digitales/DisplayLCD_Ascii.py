def generate_vhdl(text, fileName):
    # Función para convertir un carácter a su valor ASCII
    def char_to_ascii(char):
        return ord(char)
    
    # Divide el texto en líneas para procesar cada una individualmente
    text_lines = text.split('\n')
    
    # Comienza la generación del código VHDL con los encabezados y la definición de la entidad
    vhdl_code =f"""--LCD: System that displays a text on the liquid crystal display of the DE2 development board
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;

entity {fileName} is
    port (
        CLK50, SW: in std_logic; -- CLOCK_50 y un interruptor
        RS, RW, EN, LCD_ON, LCD_BLON: out std_logic; -- Pines del LCD
        DATA: out integer range 0 to 255 -- Pines LCD_DATA
    );
end entity;

architecture arq of {fileName} is
    signal c: integer range 0 to 50000000;
    signal clk: std_logic;
    signal edo_act, edo_sig: integer range 0 to 99;
begin
    LCD_ON <= '1'; 
    LCD_BLON <= '0';

    -- Proceso para generar un reloj dividido a partir del CLK50
    process(CLK50, SW)
    begin
        if (SW = '1') then
            clk <= '0'; 
            c <= 0;
        elsif rising_edge(CLK50) then
            c <= c + 1;
            if (c = 7000) then
                c <= 0; 
                clk <= not clk;
            end if;
        end if;
    end process;

    -- Proceso para controlar la secuencia de inicialización y escritura en el LCD
    process(edo_act)
    begin
        case edo_act is
            -- Secuencia de inicialización
            when 0 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 1;
            when 1 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 56; edo_sig <= 2;
            when 2 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 3;
            when 3 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 4;
            when 4 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 56; edo_sig <= 5;
            when 5 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 6;
            when 6 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 7;
            when 7 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 56; edo_sig <= 8;
            when 8 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 9;
            when 9 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 10;
            when 10 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 56; edo_sig <= 11;
            when 11 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 12;
            when 12 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 12; edo_sig <= 13;
            when 13 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 12; edo_sig <= 14;
            when 14 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 12; edo_sig <= 15;
            when 15 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 1; edo_sig <= 16;
            when 16 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 1; edo_sig <= 17;
            when 17 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 1; edo_sig <= 18;
            when 18 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 6; edo_sig <= 19;
            when 19 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 6; edo_sig <= 20;
            when 20 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 6; edo_sig <= 21;
"""
    state = 21  # Estado inicial para la escritura de datos
    for line in text_lines:
        for char in line:
            ascii_val = char_to_ascii(char)  # Convierte el carácter a ASCII
            vhdl_code += f"""
            when {state} => 
                RS <= '1';RW <= '0';EN <= '0';DATA <= {ascii_val};edo_sig <= {state + 1};"""
            state += 1
            vhdl_code += f"""
            when {state} => 
                RS <= '1';RW <= '0';EN <= '1';DATA <= {ascii_val};edo_sig <= {state + 1};"""
            state += 1
            vhdl_code += f"""
            when {state} => 
                RS <= '1';RW <= '0';EN <= '0';DATA <= {ascii_val};edo_sig <= {state + 1};"""
            state += 1
        
        # Avanza a la siguiente línea del LCD
        vhdl_code += f"""
        when {state} => 
            RS <= '0';RW <= '0';EN <= '0';DATA <= 192;edo_sig <= {state + 1};"""
        state += 1
        vhdl_code += f"""
        when {state} => 
            RS <= '0';RW <= '0';EN <= '1';DATA <= 192;edo_sig <= {state + 1};"""
        state += 1
        vhdl_code += f"""
        when {state} => 
            RS <= '0';RW <= '0';EN <= '0';DATA <= 192;edo_sig <= {state + 1};"""
        state += 1
    
    # Estado final para mantener la pantalla encendida
        vhdl_code += f"""
        when {state} => 
            RS <= '0';RW <= '0';EN <= '0';DATA <= 0;edo_sig <= {state}; -- Mantener el último estado
        when others => 
            RS <= '0';RW <= '0';EN <= '0';DATA <= 0;edo_sig <= {state}; -- Mantener el último estado
        end case;
    end process;

    -- Proceso para actualizar el estado actual basado en el estado siguiente
    process(clk)
    begin
        if rising_edge(clk) then 
            edo_act <= edo_sig; 
        end if;
    end process;
end architecture;
"""

    
    return vhdl_code

def salto_de_linea(frase):
    # Reemplaza la secuencia "\n" por un salto de línea real
    temp_frase = "" 

    while len(frase)>31:
        print("Frase muy larga")
        frase = input("Ingresa la frase\n==> ")

 
    frase_formateada = frase.replace("\\n", "\n")
    #print(frase_formateada)
    return frase_formateada

"""
# Ejemplo de uso:
input_phrase = input("Inserte la frase\n==>")
format_phrase = salto_de_linea(input_phrase)

fileName = input("Inserte el nombre del archivo\n==>")
vhdl_code = generate_vhdl(format_phrase, fileName)

# Escribir el código VHDL generado en un archivo
filename = fileName + ".vhd"
with open(filename, 'w') as file:
    file.write(vhdl_code)
print(f"Archivo '{filename}' generado con el código VHDL para mostrar la frase '{input_phrase}'.")
"""

# Por si acaso
"""--LCD: System that displays a text on the liquid crystal display of the DE2 development board
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;

entity {fileName} is
    port (
        CLK50, SW: in std_logic; -- CLOCK_50 y un interruptor
        RS, RW, EN, LCD_ON, LCD_BLON: out std_logic; -- Pines del LCD
        DATA: out integer range 0 to 255 -- Pines LCD_DATA
    );
end entity;

architecture arq of {fileName} is
    signal c: integer range 0 to 50000000;
    signal clk: std_logic;
    signal edo_act, edo_sig: integer range 0 to 99;
begin
    LCD_ON <= '1'; 
    LCD_BLON <= '0';

    -- Proceso para generar un reloj dividido a partir del CLK50
    process(CLK50, SW)
    begin
        if (SW = '1') then
            clk <= '0'; 
            c <= 0;
        elsif rising_edge(CLK50) then
            c <= c + 1;
            if (c = 7000) then
                c <= 0; 
                clk <= not clk;
            end if;
        end if;
    end process;

    -- Proceso para controlar la secuencia de inicialización y escritura en el LCD
    process(edo_act)
    begin
        case edo_act is
            -- Secuencia de inicialización
            when 0 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 1;
            when 1 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 56; edo_sig <= 2;
            when 2 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 3;
            when 3 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 4;
            when 4 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 56; edo_sig <= 5;
            when 5 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 6;
            when 6 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 7;
            when 7 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 56; edo_sig <= 8;
            when 8 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 9;
            when 9 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 10;
            when 10 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 56; edo_sig <= 11;
            when 11 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 56; edo_sig <= 12;
            when 12 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 12; edo_sig <= 13;
            when 13 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 12; edo_sig <= 14;
            when 14 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 12; edo_sig <= 15;
            when 15 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 1; edo_sig <= 16;
            when 16 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 1; edo_sig <= 17;
            when 17 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 1; edo_sig <= 18;
            when 18 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 6; edo_sig <= 19;
            when 19 => RS <= '0'; RW <= '0'; EN <= '1'; DATA <= 6; edo_sig <= 20;
            when 20 => RS <= '0'; RW <= '0'; EN <= '0'; DATA <= 6; edo_sig <= 21;
"""