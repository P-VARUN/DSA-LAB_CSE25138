class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        curr = Node(data)
        if self.rear is None:
            self.front = self.rear = curr
            return
        self.rear.next = curr
        self.rear = curr
    def dequeue(self):
        if self.front is None:
            print("Queue underflow")
            return
        
        self.front = self.front.next
        if self.front is None:
            self.rear = None
    def peek(self):
        if self.front is None:
            print("No elements in queue")
        else:
            print(self.front.data)
    def display(self):
        if self.front is None:
            print("No elements in queue")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data, end="->")
                temp = temp.next
            print("None")

q = Queue()
while (True):
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.peek")
    print("4.Display")
    print("5.Exit")
    i = int(input("Enter your chocice: "))
    if (i==1):
        e = int(input("Enter element to add"))
        q.enqueue(e)
    elif(i==2):
        q.dequeue()
    elif(i==3):
        q.peek()
    elif(i==4):
        q.display()
    elif(i==5):
        exit()
    else:
        print("Choose correct choice")
