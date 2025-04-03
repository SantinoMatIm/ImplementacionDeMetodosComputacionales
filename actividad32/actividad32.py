def lexerAritmetico(archivo):

    dic = {
        'd': '0123456789',
        'l': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'suma': '+',
        'resta': '-',
        'mult': '*',
        'div': '/',
        'pot': '^',
        'igual': '=',
        'pa': '(',
        'pc': ')',
        'punto': '.',
        'guion': '_',
        'b': ' \t\r',
        'nl': '\n'
    }
    
    tabla = {
        0: {'d': 1, 'l': 4, 'suma': 8, 'resta': 9, 'mult': 10, 'div': 16, 
            'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14, 'punto': 18, 'b': 0, 'nl': 0},
        1: {'d': 1, 'punto': 2, 'l': 99, 'b': 0, 'nl': 0, 'suma': 8, 'resta': 9, 
            'mult': 10, 'div': 16, 'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14, 'e': 5, 'E': 5},
        2: {'d': 3, 'l': 99, 'suma': 99, 'resta': 99, 'mult': 99, 
            'div': 99, 'pot': 99, 'pa': 99, 'pc': 99, 'igual': 99, 'b': 99, 'nl': 99},
        3: {'d': 3, 'l': 99, 'b': 0, 'nl': 0, 'suma': 8, 'resta': 9, 'mult': 10, 
            'div': 16, 'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14, 'e': 5, 'E': 5},
        4: {'d': 4, 'l': 4, 'guion': 4, 'b': 0, 'nl': 0, 'suma': 8, 'resta': 9, 
            'mult': 10, 'div': 16, 'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14},
        5: {'d': 7, 'suma': 6, 'resta': 6, 'b': 99, 'nl': 99},
        6: {'d': 7, 'l': 99, 'b': 99, 'nl': 99},
        7: {'d': 7, 'l': 99, 'b': 0, 'nl': 0, 'suma': 8, 'resta': 9, 'mult': 10, 
            'div': 16, 'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14},
        8: {'b': 0, 'nl': 0, 'd': 1, 'l': 4, 'punto': 18},
        9: {'b': 0, 'nl': 0, 'd': 1, 'l': 4, 'punto': 18},
        10: {'b': 0, 'nl': 0, 'd': 1, 'l': 4, 'punto': 18},
        11: {'b': 0, 'nl': 0, 'd': 1, 'l': 4, 'punto': 18},
        12: {'b': 0, 'nl': 0, 'd': 1, 'l': 4, 'punto': 18, 'resta': 9},
        13: {'b': 0, 'nl': 0, 'suma': 8, 'resta': 9, 'mult': 10, 'div': 16, 
             'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14},
        14: {'b': 0, 'nl': 0, 'd': 1, 'l': 4, 'punto': 18, 'resta': 9},
        15: {'b': 0, 'nl': 0, 'd': 1, 'l': 4, 'punto': 18, 'resta': 9},  
        16: {'div': 17, 'b': 0, 'nl': 0, 'd': 1, 'l': 4, 'punto': 18, 'resta': 9,
            'suma': 8, 'mult': 10, 'pot': 11, 'pa': 12, 'pc': 13, 'igual': 14},
        17: {k: 17 for k in dic.keys()},  
    }
    
    # Agregar todas las letras como transiciones válidas para el estado de comentario
    for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/^()=_. \t':
        tabla[17][c] = 17
    
    # Caso especial para fin de comentario
    tabla[17]['nl'] = 0
    
    # Mapeo de estados finales a tipos de token
    tipos_token = {
        1: "Entero",
        3: "Real",
        4: "Variable",
        7: "Real",
        8: "Suma",
        9: "Resta",
        10: "Multiplicación",
        11: "Potencia",
        12: "Paréntesis que abre",
        13: "Paréntesis que cierra",
        14: "Asignación",
        15: "División",  # No usado explícitamente
        16: "División",
        17: "Comentario"
    }
    
    try:
        # Leer el archivo
        with open(archivo, 'r') as f:
            texto = f.read() + '\n'  # Añadir salto de línea al final para procesar último token
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{archivo}'")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        return []
    
    estado = 0
    lexema = ""
    tokens = []
    i = 0
    
    # Procesar el texto caracter por caracter
    while i < len(texto):
        caracter = texto[i]
        
        # Determinar tipo de entrada
        tipo_entrada = None
        for tipo, chars in dic.items():
            if caracter in chars:
                tipo_entrada = tipo
                break
        
        # Si no está en el diccionario, usar el mismo caracter
        if tipo_entrada is None:
            tipo_entrada = caracter
        
        # Verificar si la transición es válida
        if estado in tabla and tipo_entrada in tabla[estado]:
            nuevo_estado = tabla[estado][tipo_entrada]
            
            # Si cambiamos de estado y el actual es un estado final, procesar el token
            if (nuevo_estado != estado) and estado in tipos_token:
                if estado == 17:  # Comentario
                    tokens.append((lexema, tipos_token[estado]))
                    lexema = ""
                else:  # Otros tokens
                    tokens.append((lexema, tipos_token[estado]))
                    lexema = ""
                    
                    # Para operadores y símbolos, no retroceder
                    # Para otros tokens (como variables, números), retroceder
                    if nuevo_estado not in [0, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
                        i -= 1
            
            # Actualizar estado
            estado = nuevo_estado
            
            # Solo agregar al lexema si no es un espacio en blanco en estado inicial
            if not (tipo_entrada in ['b', 'nl'] and estado == 0):
                lexema += caracter
            
            # Caso especial: fin de comentario (salto de línea en estado 17)
            if estado == 0 and tipo_entrada == 'nl' and lexema.startswith('//'):
                tokens.append((lexema.rstrip(), tipos_token[17]))
                lexema = ""
            
            # Caso especial: comentario confirmado (estado 17) cuando llega salto de línea
            if estado == 17 and tipo_entrada == 'nl':
                tokens.append((lexema.rstrip(), tipos_token[17]))
                lexema = ""
                estado = 0
        else:
            # Error: transición no definida
            print(f"Error: caracter '{caracter}' inesperado en estado {estado}")
            if lexema:
                print(f"Lexema parcial: '{lexema}'")
            estado = 0
            lexema = ""
        
        i += 1
    
    # Procesar el último token si queda alguno
    if lexema and estado in tipos_token:
        tokens.append((lexema, tipos_token[estado]))
    
    # Imprimir los tokens encontrados
    print("Token\t\tTipo")
    print("-" * 40)
    for token, tipo in tokens:
        print(f"{token}\t\t{tipo}")
    
    return tokens

# Código para ejecutar el programa
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
    else:
        # Usar "expresiones.txt" como valor predeterminado
        archivo = "expresiones.txt"
        print(f"Usando archivo predeterminado: {archivo}")
    
    lexerAritmetico(archivo)