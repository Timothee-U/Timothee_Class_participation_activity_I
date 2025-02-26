#!/usr/bin/env python3

# This is a Python script that takes 2 user inputed numbers, adds two numbers, and displays the result

# Here we are sking the user to input two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Making sure the inputs are strictly integers
num1 = int(num1)
num2 = int(num2)

# Adding the two numbers together
result = num1 + num2

# Displaying the result
print(f"---------------\n The sum of {num1} and {num2} is {result}.")
