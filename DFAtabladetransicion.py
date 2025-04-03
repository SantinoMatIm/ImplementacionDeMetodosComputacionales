def reconoce(w):
    dic = {'a':0,'b':1}
    estado = 0
    for c in w:
        if c in 'ab$':
            if c == '$':
                if estado == 2:
                    return True
                else:
                    return False
            estado = table[estado][dic[c]]
        else:
            estado = table
table = [[0,1],[0,2],[2,2]]
w = 'ababaa$'
print("Table:",reconoce(w))
            