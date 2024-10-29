equation = input("Please enter an expression to be calculated: ")
equation = equation.replace(" ", "")

operators = ['+', '-', '*', '/']

for char in equation:
    if char in operators:
        operator = char
        
eqn_splt = equation.partition(operator)

operand_1 = float(eqn_splt[0])
operand_2 = float(eqn_splt[-1])
        

class calculator:

    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / b
    
answer = ''
if operator == '+':
    answer = calculator.add(operand_1, operand_2)
    
elif operator == '-':
    answer = calculator.subtract(operand_1, operand_2)
    
elif operator == '*':
    answer = calculator.multiply(operand_1, operand_2)
    
elif operator == '/':
    answer = calculator.divide(operand_1, operand_2)

print(answer)

