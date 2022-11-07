def operation(c, V1, V2):
    operators = { '*': lambda x,y: x*y , '+' : lambda x,y: x+y, '-': lambda x,y: x-y, '/': lambda x,y: x//y}
    return operators[c](V1, V2)


def postfix_eval(chaine):
    operators = '*+-/'
    L = chaine.split(' ')
    PILE = []
    
    while len(L)!=0:
        c = L.pop(0)
        if c == '': pass
        elif c in operators:
            if len(PILE)<2: return 'error-empty-stack'
            V2, V1 = PILE.pop(),  PILE.pop()
            PILE.append(operation(c, V1, V2))
        
        else: 
            try:
                c = int(c)
                PILE.append(c)
            except: return 'error-syntax'
            
    if len(PILE) == 0 : return 'error-empty-stack'
    elif len(PILE) == 2 : return 'error-unfinished'
    return PILE.pop()
        