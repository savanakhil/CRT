'''Debugging in Python:
            bug --> Errors
        Debugging --> Finding and Fixing of Errors
Types of Errors
1) Syntax Error --> Missing of colon, missing of indentation
2) Runtime Error --> Division by Zero
3) Logical Error --> Missing of Logics

Debugging Techniques:
    1)print()
    2)try-except
    3)Using pdb
        pdb-->python debugger
        purpose:
        1)Pause the execution code 
        2)Inspect the variables's value 
        3)to run the code line by line
PDB Commands:
    1)n --> To execute the output in a next line
    2)p variale --> to get the value of a variable 
    3)l --> list nearby code 
    4)c --> continue the execution 
    5)s --> to start a function
    6)r --> return from the function 
    7)h --> help 
    8)q --> Quit the execution   '''
'''try:
    a=int(input("enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("can not divisible by Zero.")
except ValueError:
    print("Invalid input")
'''
import pdb 
def add(a,b):
    pdb.set_trace()
    return a + b 
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print(add(a, b))