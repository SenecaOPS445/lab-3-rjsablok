#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: [seneca_id]

def sum_numbers(number1, number2):
    # This function adds number1 and number2 and returns the result
    return number1 + number2

def subtract_numbers(number1, number2):
    # This function subtracts number2 from number1 and returns the result
    return number1 - number2

def multiply_numbers(number1, number2):
    # This function multiplies number1 and number2 and returns the result
    return number1 * number2

if __name__ == '__main__':
    # Testing the functions with sample values
    print(sum_numbers(10, 5))  # Should print 15
    print(subtract_numbers(10, 5))  # Should print 5
    print(multiply_numbers(10, 5))  # Should print 50
