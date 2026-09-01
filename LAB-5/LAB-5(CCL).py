class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        temp.next = new_node
        new_node.next = self.head

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_start(data)
            return
        
        new_node = Node(data)
        temp = self.head
        count = 0
        
        while temp and count < index - 1:
            temp = temp.next
            count += 1
            if temp == self.head:
                print("Index out of bounds")
                return
                
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_start(self):
        if not self.head:
            print("List is empty")
            return
        
        if self.head.next == self.head:
            self.head = None
            return
            
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            
        temp.next = self.head.next
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
            
        if self.head.next == self.head:
            self.head = None
            return
            
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
            
        temp.next = self.head

    def delete_at_index(self, index):
        if not self.head:
            print("List is empty")
            return
            
        if index == 0:
            self.delete_at_start()
            return
            
        temp = self.head
        count = 0
        
        while temp and count < index - 1:
            temp = temp.next
            count += 1
            if temp.next == self.head:
                print("Index out of bounds")
                return
                
        temp.next = temp.next.next

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print(f"(back to head: {self.head.data})")

if __name__ == "__main__":
    cll = CircularLinkedList()
    
    cll.insert_at_end(10)
    cll.insert_at_end(20)
    cll.insert_at_start(5)
    cll.insert_at_index(2, 15)
    cll.display()
    
    cll.delete_at_start()
    cll.delete_at_end()
    cll.display()
    
    cll.delete_at_index(1)
    cll.display()