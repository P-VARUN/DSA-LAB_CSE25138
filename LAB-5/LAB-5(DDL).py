class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
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
        new_node.prev = last

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
        new_node.prev = current
        
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete_at_start(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
            
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    def delete_at_index(self, index):
        if not self.head:
            print("List is empty.")
            return
        if index == 0:
            self.delete_at_start()
            return
            
        current = self.head
        for _ in range(index):
            if not current:
                raise IndexError("Index out of bounds")
            current = current.next
            
        if not current:
            raise IndexError("Index out of bounds")
            
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements) if elements else "Empty List")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    dll.insert_at_start(10)
    dll.insert_at_end(30)
    dll.insert_at_index(1, 20)
    dll.display() 
    
    dll.delete_at_start()
    dll.display() 
    
    dll.delete_at_end()
    dll.display() 
    
    dll.insert_at_start(10)
    dll.insert_at_end(30)
    dll.delete_at_index(1)
    dll.display()