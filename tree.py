class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value (float/int/str)
        end = value[-1]
        if end == '1':

            if check(value + '2'):
                self.left = Node(value+'2')
            else:
                self.left = '0'

            if check(value+'3'):
                self.right = Node(value+'3')
            else:
                self.left(

        elif end == '2':
            if check(value
        else:

        self.left =    # Left child
        self.right = right  # Right child
