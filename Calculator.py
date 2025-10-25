def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose a operator(+ , - , * , /): ")

if operator == "+":
    print("Addition:", add(num1,num2))
elif operator == "-":
    print("Subtraction:" ,sub(num1,num2))
elif operator == "*":
    print("Multiplication:", mul(num1,num2))
elif operator == "/":
    print("Division:", div(num1,num2))
else:
    print("Invalid Operator")