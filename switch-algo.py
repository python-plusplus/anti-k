from airtight import tightCheck

def nextNode(left, leftChild, rightChild, string):
    if left:
        if tightCheck(string+leftChild):
            return (left, leftChild, string+leftChild)
        elif tightCheck(string+rightChild):
            left = False
            return (left, rightChild, string+rightChild)
        else:
            print('DEADEND')
            return False
    else:
        if tightCheck(string+rightChild):
            return (left, rightChild, string+rightChild)
        elif tightCheck(string+leftChild):
            left = True
            return (left, leftChild, string+leftChild)
        else:
            print('DEADEND')
            return False

left = True
string = 'ABACBCAB'
last = 'B'
    else:

while True:
    print(string)
    if last == 'A':
        left, last, string = nextNode(left, 'B', 'C', string)
    elif last == 'B':
        left, last, string = nextNode(left, 'A', 'C', string)
    else:
        left, last, string = nextNode(left, 'A', 'B', string)
