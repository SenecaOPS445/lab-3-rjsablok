#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: [seneca_id]

def operate(number1, number2, operator):
    # Handle different operations based on the operator
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        # Return an error message if the operator is not recognized
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    # Testing the function with various operators
    print(operate(10, 5, 'add'))       # Should return 15
    print(operate(10, 5, 'subtract'))  # Should return 5
    print(operate(10, 5, 'multiply'))  # Should return 50
    print(operate(10, 5, 'divide'))    # Should return an error message
