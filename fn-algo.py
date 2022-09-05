from airtight import tightCheck

def possibleMoves(string, symbols):
    if len(symbols) != 2:
        print('symbols not 2 error')
        exit()
    pm = []
    for symbol in symbols:
        if tightCheck(string + symbol):
            pm.append(symbol)
    return pm

def fn_algo(string, first, symbols=['A', 'B', 'C']):
    last = string[-1]
    #print(last)
    symbols.remove(last)
    #print(symbols)
    pm = possibleMoves(string, symbols)
    p = len(pm)

    if p == 0:
        print('DEADEND')
        exit()
    elif p == 1:
        #This is an FN
        #for i in range():
#        if pm[0] == first:
#            front = string[1:-1]
#        else:
        front = string[:-1]
        symbols.remove(front[-1])
        for i in range(len(front)):
            if i == len(front) - 1:
                print('SHIT!')
            if tightCheck(string+pm[0]+front[i:]+symbols[0]):
                return string + pm[0] + front[i:] + symbols[0]
        print("FUCK")
        exit()
        return string + pm[0] + front + symbols[0]
    elif p == 2:
        return string + pm[0] 
    else:
        print('Error p greater than 2')

string = 'A'
first = 'A'
while True:
    print('curr' + string)
    string = fn_algo(string, first, ['A', 'B', 'C'])

