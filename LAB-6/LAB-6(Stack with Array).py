class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            print(f"Popped {self.stack.pop()} from stack")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(f"Top element is {self.stack[-1]}")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack[::-1])

    def menu(self):
        while True:
            print("\n1. Push")
            print("2. Pop")
            print("3. Peek")
            print("4. Display")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                item = input("Enter item to push: ")
                self.push(item)
            elif choice == '2':
                self.pop()
            elif choice == '3':
                self.peek()
            elif choice == '4':
                self.display()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

my_stack = Stack()
my_stack.menu()