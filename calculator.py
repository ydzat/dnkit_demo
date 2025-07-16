print("Calculator is here!")

# Basic calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Main program
if __name__ == "__main__":
    print("Enter an operation (e.g., 1+2):")
    operation = input().strip()
    
    # Parse the operation
    if '+' in operation:
        a, b = map(float, operation.split('+'))
        print(add(a, b))
    elif '-' in operation:
        a, b = map(float, operation.split('-'))
        print(subtract(a, b))
    elif '*' in operation:
        a, b = map(float, operation.split('*'))
        print(multiply(a, b))
    elif '/' in operation:
        a, b = map(float, operation.split('/'))
        print(divide(a, b))
    else:
        print("Invalid operation. Please use +, -, *, or /.")