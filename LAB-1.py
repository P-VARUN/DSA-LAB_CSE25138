# a) Rocket launch countdown
def countdown(n):
    if n <= 0:
        print("Launch!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)

# b) Calculate power recursively
def calculate_power(P, n):
    if n == 0:
        return 1
    else:
        return P * calculate_power(P, n - 1)

print(calculate_power(20, 5))

# c) Search for an employee ID in a list recursively
def search_employee(emp_list, emp_id, index=0):
    if index == len(emp_list):
        return False
    if emp_list[index] == emp_id:
        return True
    return search_employee(emp_list, emp_id, index + 1)

employees = [101, 105, 108, 112]
print(search_employee(employees, 108))

# d) Calculate factorial recursively
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

print(calculate_factorial(5))

# e) Print the first n terms of Fibonacci series recursively
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(terms):
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()

print_fibonacci_series(7)