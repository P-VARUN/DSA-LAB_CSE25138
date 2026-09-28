class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLL:
    def __init__(self):
        self.rear = None

    def enqueue(self, data):
        curr = Node(data)
        if self.rear is None:
            self.rear = curr
            curr.next = self.rear
            print(f"{data} is added to queue")
            return
            
        curr.next = self.rear.next
        self.rear.next = curr
        self.rear = curr
        print(f"{data} is added to queue")

    def dequeue(self):
        if self.rear is None:
            print("Queue underflow")
            return
            
        front = self.rear.next
        print(f"{front.data} is deleted from queue")
        
        if self.rear == front:
            self.rear = None
        else:
            self.rear.next = front.next

    def peek(self):
        if self.rear is None:
            print("No elements in the queue")
        else:
            front = self.rear.next
            print(front.data)

    def display(self):
        if self.rear is None:
            print("Empty Queue")
            return
            
        front = self.rear.next
        temp = front
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == front:
                break
        print("(Back to Front)")

q = CircularQueueLL()
while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            e = int(input("Enter element to add: "))
            q.enqueue(e)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.peek()
        elif choice == 4:
            q.display()
        elif choice == 5:
            break
        else:
            print("Choose a valid choice")
    except ValueError:
        print("Please enter a valid number")
