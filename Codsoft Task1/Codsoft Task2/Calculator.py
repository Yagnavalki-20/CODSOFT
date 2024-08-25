import os
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operation_dict={
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    number1 =int(input("Enter first number:"))
    for symbol in operation_dict:
        print(symbol)
    continue_flag = True
    while continue_flag:
        op_symbol = input("pick an operator:")
        number2 = int(input("Enter next number :"))
        calculator_function = operation_dict[op_symbol]
        output = calculator_function(number1,number2)
        print(f"{number1}{op_symbol}{number2} = {output}")
        should_continue= input(f"Enter 'y' to continue calculation with {output} or 'n'to start: ")
        if should_continue =='y':
            number1=output
        elif should_continue =='n':
            continue_flag=False
            calculator()
        else:
            continue_flag = False
            print("Bye")
calculator()
