#Dado un DFA (= RE)

def reconoce(w):
    dic = {'d':0,'+':1,'-':2,'.':3,'b':4,'otro':5}
    table = [[1,6,7,8,0,8],[1,4,4,2,4,8],[3,8,8,8,8,8],[3,5,5,8,5,8]]
    estado = 0
    for c in w:
        if c in '0123456789$':
            if c == '$':
                if estado == 0:
                    return True
                else:
                    return False
            estado = table[estado][dic[c]]
        else:
            estado = table

w = '0011$'
print("Table:",reconoce(w))