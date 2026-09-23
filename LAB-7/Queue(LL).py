class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        curr = Node(data)
        temp = self.front
        while (temp!=None):
            temp = temp.next
        temp.next = curr
        self.rear = curr
    def dequeue(self):
        if (self.front>self.rear or self.rear==None):
            print("Queue underflow")
        else:
            temp = self.front
            self.front = self.front.next;
            temp=None
    def peek(self):
        if (self.front==None):
            print("No elements in queue")
        else:
            print(self.front)
    def display(self):
        if (self.front==None):
            print("No elements in queue")
        else:
            temp = self.front
            while (temp!=null):
                print(temp.data,end="->")
                temp = temp.next;
            print("None")
q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(2)
q.enqueue(9)
q.display()