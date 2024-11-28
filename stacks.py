from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
        
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
        
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return true if len(self.stack) == 0 else False
        
    def size_of(self):
        return len(self.stack)
        
t = Stack()
t.push("Orange")
t.push("apple")
print(t.size_of())
print(t.peek())
print(t.is_empty())
print(t.pop())
print(t.size_of())
