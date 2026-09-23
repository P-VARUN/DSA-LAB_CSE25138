class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
    def enqueue(self,data):
        if (self.rear>=self.size-1):
            print("Queue overflow")
        else:
            if (self.front == -1):
                self.front = 0
            self.rear+=1
            self.queue[self.rear]=data
            print(f"{data} is added to queue")
    def dequeue(self):
        if (self.front>self.rear or self.front==-1):
            print("Queue underflow")
        else :
            print(f"{self.queue[self.front]} is deleted from queue")
            self.queue[self.front] = None
            self.front+=1
    def peek(self):
        if (self.front==-1):
            print("No elements in the queue")
        else:
            print(self.queue[self.front])
    def display(self):
        if (self.front==-1):
            print("Empty Queue")
        else:
            for i in range (0,self.rear+1):
                print(self.queue[i],end="->")
            print(None)
q=Queue(5)
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