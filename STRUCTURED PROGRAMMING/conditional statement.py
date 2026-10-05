# if condition:
## MUHANGUZI DAVID
##CONDITIONAL STATEMENTS
age = int(input("Enter your age: "))
if age >= 13:
    print("you are welcome")
    ## the person can access this site because he/she is of or above the required age.
else:
    print("get lost kid!")
## if the person is below the age of 13, he/she cannot access this site.

print("welcome to basic calc")
print("please chosse an operator: \n1. addition (+) \n2. subtraction \n3. multiplication \n4. division")
operator = int(input())
number1= int(input("enter first number"))
number2= float(input("enter the second number"))
#number1 and number2 are the variables

if operator == 1:
    total = number1 + number2
    print(f"The summation of {number1} and {number2} is {total}.")
## sum is what we get after adding number1 and number2
elif operator == 2:
    difference = number1 - number2
    print(f"The difference between {number1} and {number2} is {difference}.")
##difference is what we get after subtracting number2 from number1
elif operator == 3:
    product = number1 * number2
    print(f"The product of {number1} and {number2} is {product}.")
##25product ia the answer obtained after multiplying number1 by number2
elif operator == 4:
    quotient = number1 / number2
    print(f"The quotient between {number1} and {number2} is {quotient}.")
##quotient is the value obtained after dividing number1 by number2
else:
    print("choose the right operator.")