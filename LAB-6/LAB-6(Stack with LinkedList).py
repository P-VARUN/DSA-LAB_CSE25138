class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} is added to stack")
        
    def pop(self):
        if self.top is None:
            print("Stack underflow")
        else:
            print(f"{self.top.data} is deleted from stack")
            self.top = self.top.next
            
    def peek(self):
        if self.top is None:
            print("No elements in the stack")
        else:
            print(self.top.data)
            
    def display(self):
        if self.top is None:
            print("Empty Stack")
        else:
            current = self.top
            while current:
                print(current.data, end="->")
                current = current.next
            print(None)

s = Stack()
while (True):
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    i = int(input("Enter your choice: "))
    if (i == 1):
        e = int(input("Enter element to add: "))
        s.push(e)
    elif (i == 2):
        s.pop()
    elif (i == 3):
        s.peek()
    elif (i == 4):
        s.display()
    elif (i == 5):
        exit()
    else:
        print("Choose correct choice")