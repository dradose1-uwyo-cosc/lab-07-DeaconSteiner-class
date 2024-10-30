while True:
    equation = input("Please enter an expression to be calculated (or type exit to quit): ")
    equation = equation.replace(" ", "")

    if equation == "exit".lower():
        print("Program has been exited")
        break
    
    else:

        operators = ['+', '-', '*', '/']

        for char in equation:
            if char in operators:
                operator = char
            
        eqn_splt = equation.partition(operator)
        
        if eqn_splt[0].isdigit() and eqn_splt[-1].isdigit():
            operand_1 = float(eqn_splt[0])
            operand_2 = float(eqn_splt[-1])
            
        else:
            print("error occured, try again")
            continue

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

