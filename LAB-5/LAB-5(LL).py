class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_start(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        for _ in range(index - 1):
            if not current:
                raise IndexError("Index out of bounds")
            current = current.next
            
        if not current:
            raise IndexError("Index out of bounds")
            
        new_node.next = current.next
        current.next = new_node

    def delete_at_start(self):
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
            
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_index(self, index):
        if not self.head:
            print("List is empty.")
            return
        if index == 0:
            self.delete_at_start()
            return
            
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                raise IndexError("Index out of bounds")
            current = current.next
            
        if not current.next:
            raise IndexError("Index out of bounds")
            
        current.next = current.next.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")


if __name__ == "__main__":
    ll = LinkedList()
    
    ll.insert_at_start(10)
    ll.insert_at_end(30)
    ll.insert_at_index(1, 20)
    ll.display() 
    
    ll.delete_at_start()
    ll.display() 
    
    ll.delete_at_end()
    ll.display() 
    
    ll.insert_at_start(10)
    ll.insert_at_end(30)
    ll.delete_at_index(1)
    ll.display()