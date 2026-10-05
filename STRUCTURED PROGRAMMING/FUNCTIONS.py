#s26b13/022   
#b39032
#muhanguzi david
#functions are reusable chunks of code. it lets you automate code.
#it can be referrred to elsewhere.

#types of functions.
#1. user defined functions: thee are custom functions amde by the programmer to achieve a given target.
#there are two categories; void and return function.

#void function handles the logic within its body.
#return function works out the instructions and produces the results back to the programmer.

#2. built in functions: these come with python installation. e.g orint(), input()

#syntax of a void function
#def means defining a function
"""
def calculator():
    pass#means you're leaving something empty
"""
"""
def greetings(name):
    print(f"welcome {name}")

def main():
        greetings("david")#david is the argument because it is the actual value
#ASSIGNMENT1: modify the provided code to allow the user enter their name and welcome them.
main()
"""
def calculate(parameter_one, parameter_two):
    sum = parameter_one + parameter_two
    return f"The sum is {sum}"
calculate(24,50)
print(calculate(24,50))

import random

def generate_number():
    random_number = random.randint(0,9)
    return random_number

def main():
    print("welcome to the random guess game")
    print("enter a number between 0 to 9")
    entered_number = int(input())
    computer_generated = generate_number()
    if entered_number == computer_generated:
        print("congratulations, you have won")
    else:
        print("you lose")
main()
for attempt in range(3):
    print(f"\nattempt {attempt+1}/3 enter a number between 0 to 9")
    entered_number = int(input())
    print("do you want play again? ")