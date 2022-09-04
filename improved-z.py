import random
import time

def checkReturnIndex(string):
    n = len(string)
    last = string[-1]
    if n > 4:
        for i in range(-1, -(int(n/2)+2), -1):
            if i == -1:
                pass
            elif i == -2:
                if last != string[-2]:
                    pass
                else:
                    return False
            else:
                if last == string[i]: 
                    if string[i+1:-1] != string[i+(i+2):i]:
                        pass
                    else:
                        #print("repeat found")
                        #print(string)
                        #print(i)
                        #print(n+i)
                        #print(string[i+1:-1])
                        #print(string[i+(i+2):i])
                        return i
        return True
    else:
        return string[-1] != string[-2] and string[2:] != string[:2]

def generateRandom(symbols=['A', 'B', 'C']):
    randStr = ''
    for i in range(random.randint(1, 10)):
        randStr += random.choice(symbols)
    return randStr

#for j in range(50):
#    rand = generateRandom()
#    checkReturnIndex(rand)


symbols = ['A', 'B', 'C']
string = 'ABACBABCBACBCABACBABCBACABACBABCABACBCABCBABCABACBABCBACBCABACBABCABACBCABCBABCABACBABCBACABACBABCABACBCABCBABCABACBABCACBACABACBABCBACBCABACBABCBACABACBABCABACBCABCBABCABACBABCBACBCABACBABCABACBCABCBABCABACBABCBACABACBABCABACBCABCBABCABACBABCACBCABACBABCBACBCABACBABCABACBCABCBABCABACBABCBACBCABACBABCABACBCACBABCBACBCABACBABCBACBCACBABCBACABACBABCBACBCABACBABCBACABACBABCABACBCABCBABCABACBABCBACBCABACBABCABACBCABCBABCABACBABCBACABACBABCABACBCABCBABCABACBABCACBACABACBABCBACBCABACBABCBACABACBABCABACBCABCBABCABACBABCBACBCABACBABCABACBCABCBABCABACBABCBACABACBABCABACBCABCBABCABACBCACBABCBACBCABACBABCBACBCACBABCBACABACBABCBACBCABACBABCBACABACBABCABACBCABCBABCABACBABCBACBCABACBABCABACBCABCBABCABACBABCBACABACBABCABACBCABCBABCABACBABCACBACABACBABCBACBCABACBABCBACABACBABCABACBCABCBABCABACBABCBACBCABACBABCABACBCABCBABCABACBABCBACABACBABCABACBCACBABCBACBCABACBABCBACBCACBABCBACABACBABCBACBCABACBABCBACABACBABCABACB'
while True:
    myList = []
    print(string)
    for symbol in symbols:
        if symbol == string[-1]:
            pass
        else:
            result = checkReturnIndex(string+symbol)
            if result == True:
                string += symbol
                symbols = ['A', 'B', 'C']
                break 
            else:
                myList.append(result)
    #We hit DE 
    if result == True:
        continue
    else:
        cutIndex = max(myList)
        symbols = ['A', 'B', 'C']
        symbols.remove(string[cutIndex])
        string = string[:cutIndex]
