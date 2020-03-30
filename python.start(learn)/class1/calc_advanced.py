# Python Calculator using functions


def add(num1, num2):
    output = num1+num2
    return output


def subtract(num1, num2):
    output = num1-num2
    return output


def multiply(num1, num2):
    output = num1*num2
    return output


def divide(num1, num2):
    output = num1/num2
    return output


num1 = int(input("Input number one: "))
num2 = int(input("Input number two: "))
operator = input("Do you want to 'add', 'subtract', 'multiply', or 'divide?': ")

if operator == "add":
    ans = add(num1, num2)
elif operator == "subtract":
    ans = subtract(num1, num2)
elif operator == "multiply":
    ans = multiply(num1, num2)
elif operator == "divide":
    ans = divide(num1, num2)
else:
    ans = "Invalid input"

print(ans)
