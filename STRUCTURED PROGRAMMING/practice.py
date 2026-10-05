#practice
name = input("what is your name? ")
print("Hello " + name)
birth_year = input("enter your birth_year ") #_(underscore seperates multiple words i.e first_name, not first name)
age = 2026 - int(birth_year)
print (age)

#how to convert the value of one variable from one variablr to another.
first_number = float(input("first_number: "))
second_number = float(input("second_number: "))
sum = first_number + second_number
print("sum is " + str(sum))
programme = 'Bachelor of Science In Information Technology'
print(programme.upper())
print(programme)
print(programme.find('o'))

'''
comparison operators
>
>=
<
<=
==
!=
'''

#logical operators
price = 25
print(price>10 and price<30)
print(price>10 or price<30)
print(not price>10)

#if statements are used to make decissions in the programme
temperature = 19
if temperature > 30:
    print("It is a hot day. Drink plenty of water.")
elif temperature >25: # means greater than 25 and less than 37
    print("It is a nice day.")
elif temperature > 10: # means greater than 10 and less than 25
    print("It is a chilly day.")
else:
    print("It is a very cold day!!")

# Design a code that converts height from metres to centimetres and viceversa.
height = float(input("Height: "))
unit = input("cm or m ")
if unit == "cm":
   converted = height / 100
   print("Height in m: " + str(converted))
else:
    converted = height * 100
    print("Height in cm: " + str(converted))


#while loops are used to print a block of code multipe times
i=2
while i<=10:
    print(i * "david ")
    i=i+1

#lists
animals = ["lion", "elephant", "buffalo", "leopard", "rhino", "mamba", "giraffe", "crocodile", "hippo", "elephant"]
animals.remove = ("elephant")

numbers = [100, 2, 36, 4, 9, 14, 10, 8]
print(numbers[::-1])#to reverse the list using slicing

numbers.sort()#sorts in ascending order
print(numbers)

numbers.extend(77)
print(numbers)

marks = [64, 65, 80,78,88]
n= int(input("How many marks? "))

for i in range (n):
    value= int(input("Enter mark: "))
    marks.append(value)
if len(marks) > 0:
    average= sum(marks)/len(marks)
    print("Average:", average)
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
else:
    print("No marks entered.")
 
numbers = [14,57,4,39,82,90,63,68,94,59,66,12]
count=0
for n in numbers:
    if n>50:
        count+=1
print("Numbers above 50 are;", count)

numbers = [1, 2, 3, 4, 5]  #insert adds an item where you place its index to be on the list.
numbers.remove(3)          #append adds an item at the end of the list.
print(numbers)             #remove eliminates an item in the list.
#pop() removes a specified index from the list
#if the item appears more than once in the list, remove eliminates the first appearance of the item.
# If you do not specify the index, the pop() method removes the last item.
# #clear eliminates all items in the list.
#The del keyword also removes the specified index.
#The del keyword can also delete the list completely.
#The clear() method empties the list.


numbers=[1,2,3,4,5] 
print(1 in numbers) #boolean expression.It checks if 1 is in the list and returns a boolan value.

numbers=[1,2,3,4,5] #len()function checks how many items are in the list.
print(len(numbers))

#for loop
for item in numbers: #for loop can be used for any object that represents a sequence of objects.
    print(item)

#while loop
i=0
while i< len(numbers):
    print(numbers[i])
    i=i+1

#range function is used to generate a sequence of numbers.
#range of 5 generates a sequence of numbers starting from 0 to the specified number.
#to skip numbers add a third nmber of how many numbers you want skipped.
numbers=range(0,21,2)
for number in numbers:
    print(number)
#or
for number in range(5):
    print(number)
    