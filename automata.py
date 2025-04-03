tabla = [[1,6,7,8,0,0], [1,4,4,2,4,0], [3,8,8,8,8,8], [3,5,5,8,5,8]]
blanco = '\n\t$'
digito = '0123456789'

s = '34+65.43  -  72.01 -405'
estado = 0
p = 0 #Posición del caracter actual en el arreglo
lexema = ''
token = ''

while (s[p] != '$' or (s[p] == '$' and estado != 0)):
    c = s[p]
    if c in digito:
        col = 0
    elif c == '+':
        col = 1
    elif c == '-':
        col = 2
    elif c == '.':
        col = 3
    elif c in blanco:
        col = 4
    else:
        col = 5

    estado = tabla[estado][col]

    if estado == 4:
        print(lexema,'INT')
        lexema = ''
        estado = 0
        p -= 1
    elif estado == 5:
        print(lexema,'REAL')
        lexema = ''
        estado = 0
        p -= 1
    elif estado == 6:
        print('+','SUMA')
        lexema = ''
        estado = 0
    elif estado == 7:
        print('-','RESTA')
        lexema = ''
        estado = 0
    elif estado == 8:
        print('Error 2')
        break

    p+=1 #Avanzar una posición del string

    if estado != 0:
        lexema += c