# Python Calculator using functions


def add(num1, num2):
    output = num1+num2
    return output
"""
This is the function. Functions are sets of instructions which take in data, process it, and send out a result.

'def' is the statement used to create a new function.

'add' (in this instance) is the name of the function. When you call a function from a variable, you use this name as the
name of your function
e.g. var = add.()

the stuff within the two brackets in add() are the required inputs. For the program to work, you need to input two
values into the function when you call it from the variable.
e.g. var = add.(num1, num2)
num1 and num2 in this instance are the two variables inputted. Note that the name of the variables inputted and the name
of th variables in the function do not need to correlate.

'output' in this instance is the instruction the function is supposed to carry out.

'return' is what the function will output. It reassigns the variable to whatever is in return.
e.g. var = add.(1, 2) will return a value (in this instance) will return 3. 'var' will now equal to 3 as well.
"""


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

"""
This is the if/else. It basically checks is the statement is true. If it is true, it will execute the code inside of the
if module. If it is false, it will execute the code within false.
e.g.
if 1==3:
    print("One equals to three!")
else:
    print("Normal sane human being here.")
    
Since 1 != 3, it will print 'Normal sane human being here.'

elif is nothing but an else if. It replaces:

if 1==3:
    print("One equals to three!")
else:
    if 1==4:
        print("I am CRAAAZZZYY!")
        else:
            if 1==1:
                print("Am I the only sane human here?")

with
if 1==3:
    print("One equals to three!")
elif 1==4:
    print("I am CRAAAZZZYY!")
elif 1==1:
    print("Am I the only sane human here?")

The syntax to write if statements is:

if (var/number) (operator[== means equal to]) (var/number):
    do xyz
else:
    do abc
"""

print(ans)
