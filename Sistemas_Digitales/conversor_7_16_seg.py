segment_values_16dgt = {
        'A': "0000110000111111",
        'B': "0000001100111111",
        'C': "0011000011111111",
        'D': "1100000100111111",
        'E': "0011000000111111",
        'F': "0011110000111111",
        'G': "0010000010111111",
        'H': "1100110000111111",
        'I': "0011001111101101",
        'J': "1100000111111011",
        'K': "1111111111101111",
        'L': "1111000011111111",
        'M': "1100110011010111",
        'N': "1100110011011011",
        'O': "0000000011111111",
        'P': "0001110000111111",
        'Q': "0000000011111011",
        'R': "0001110000111011",
        'S': "0010001000111111",
        'T': "0011111111101101",
        'U': "1100000011111111",
        'V': "1111110011110110",
        'W': "1100110011111010",
        'X': "1111111111010010",
        'Y': "1111111111010101",
        'Z': "0011001111110110",
        '0': "0000000011110110",
        '1': "1111111111111000",
        '2': "0001000100111111",
        '3': "0000001110111111",
        '4': "1100111000111111",
        '5': "0010001000111111",
        '6': "0110000000111111",
        '7': "0000111111111111",
        '8': "0000000000111111",
        '9': "0000101000111111",
        '.': "1111111111111111"
    }

segment_values_8dgt = {
        '0': "0000001",
        '1': "1001111",
        '2': "0010010",
        '3': "0000110",
        '4': "1001100",
        '5': "0100100",
        '6': "0100000",
        '7': "0001111",
        '8': "0000000",
        '9': "0000100",
        'A': "0001000",
        'B': "1100000",
        'C': "0110001",
        'D': "1000010",
        'E': "0110000",
        'F': "0111000",
        'G': "0100001",
        'H': "1001000",
        'I': "1111111",
        'J': "1110000",
        'K': "1001000", 
        'L': "0110001",
        'M': "0010101",
        'N': "0010100",
        'O': "0000001",
        'P': "1101000",
        'Q': "1000101",
        'R': "0000100",
        'S': "0100100",
        'T': "0111100",
        'U': "0000001",
        'V': "0000110",
        'W': "0010101",
        'X': "1001000",
        'Y': "1000100",
        'Z': "0100100",
    }


def generate_vhdl_code_sw(phrase,flieName,dysplayseg):
    # Define el diccionario de letras con sus valores en segmentos hexadecimales
    values = 0

    if (dysplayseg == 1):
        segment_values = segment_values_16dgt
        values='15'
    elif (dysplayseg == 2):
        segment_values = segment_values_8dgt
        values='6'

    # Convertir la frase a mayúsculas y crear una cadena para almacenar el código VHDL
    phrase = phrase.upper()
    vhdl_code = ""
    
    # Generar el código VHDL para asignar los segmentos según cada letra en la frase
    vhdl_code +=("library IEEE;\n" 
                +"use IEEE.STD_LOGIC_1164.ALL;\n"
                + "entity "+flieName+" is\n"
                + "    Port ( binary_num : in STD_LOGIC_VECTOR(4 downto 0);\n"
                + "           segments   : out STD_LOGIC_VECTOR("+values+" downto 0));\n"
                + "end "+flieName+";\n"
                + "architecture Behavioral of "+flieName+" is\n"
                + "begin\n\n"
                + "    process(binary_num)\n"
                + "    begin\n"
                + "        case binary_num is\n")
    # Generar los casos para cada letra en la frase ingresada
    for index, letter in enumerate(phrase):
        if letter in segment_values:
            binary_num = format(index, '05b')  # Convierte el índice a binario de 5 bits
            vhdl_code += f"            when \"{binary_num}\" => segments <= \"{segment_values[letter]}\"; -- {letter} ({segment_values[letter]})\n"
    
    # Agregar el caso para letras no definidas (fuera del abecedario)
    vhdl_code += "            when others => segments <= (others => '0'); -- Default\n"
    
    vhdl_code += "        end case;\n"
    vhdl_code += "    end process;\n"
    
    vhdl_code += "end Behavioral;\n"

    return vhdl_code


def generate_vhdl_code_timer(phrase, fileName, displayseg, time):
    
    userClock = time * 50000000 
    userClock = str(userClock)
    if displayseg == 1:
        segment_values = segment_values_16dgt
        values = '15'
    elif displayseg == 2:
        segment_values = segment_values_8dgt
        values = '6'

    phrase = phrase.upper()
    vhdl_code = ""
    vhdl_code += ("library IEEE;\n"
                +  "use IEEE.STD_LOGIC_1164.ALL;\n"
                +  "use IEEE.STD_LOGIC_ARITH.ALL;\n"
                +  "use IEEE.STD_LOGIC_UNSIGNED.ALL;\n\n"
                +  "entity " + fileName + " is\n"
                +  "    Port ( CLK : in STD_LOGIC;\n"
                +  "           segments : out STD_LOGIC_VECTOR(" + values + " downto 0));\n"
                +  "end " + fileName + ";\n\n"
                +  "architecture Behavioral of " + fileName + " is\n"
                +  "    signal counter : integer range 0 to " + userClock + " := 0;\n"
                +  "    signal display_index : integer range 0 to " + str(len(phrase)-1) + " := 0;\n"
                +  "begin\n\n"
                +  "    process(CLK)\n"
                +  "    begin\n"
                +  "        if rising_edge(CLK) then\n"
                +  "            counter <= counter + 1;\n"
                +  "            if counter = " + userClock + " then\n"
                +  "                counter <= 0;\n"
                +  "                if display_index = " + str(len(phrase)-1) + " then\n"
                +  "                    display_index <= 0;\n"
                +  "                else\n"
                +  "                    display_index <= display_index + 1;\n"
                +  "                end if;\n"
                +  "            end if;\n"
                +  "        end if;\n"
                + "    end process;\n\n"
                + "    process(display_index)\n"
                +  "    begin\n"
                + "        case display_index is\n")

    for index, letter in enumerate(phrase):
        if letter in segment_values:
            vhdl_code += f"            when {index} => segments <= \"{segment_values[letter]}\"; -- {letter} ({segment_values[letter]})\n"

    vhdl_code += "            when others => segments <= (others => '0'); -- Default\n"

    vhdl_code += ("        end case;\n"
                +  "    end process;\n"
                + "end Behavioral;\n")
    
    return vhdl_code
