#Dado un DFA (= RE)

def reconoce(w):
    dic = {'0':0,'1':1}
    table = [[1,2],[0,3],[3,0],[2,1]]
    estado = 0
    for c in w:
        if c in '01$':
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