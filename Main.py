import os
class Stack:
    """this class contains the stack and its size
    attributes:
    items: it is the stack
    size: it holds the size of the stack"""
    
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        """the is_empty() function returns if the stack is empty"""
        return len(self.items)==0
            
    def is_full(self):
        """the is_full() function returns if the stack is full"""
        return len(self.items)==self.size
            
    def push(self, data):
        """the push function pushes or adds the data to the stack
        arguments:
        data: it holds the value to be added to the stack"""
        if not self.is_full():
            self.items.append(data)

    def pop(self):
        """the pop function pops or delets the top most data from the stack"""
        if not self.is_empty():
           self.items.pop(-1)

    def status(self):
    """the status function pops or deletes the top most data from the stack"""
       for element in self.items:
        print(element)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
