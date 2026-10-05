#lists
animals = ["lion", "elephant", "buffalo", "leopard", "rhino", "mamba", "giraffe", "crocodile", "hippo", "elephant"]
animals.remove ("elephant")
print(animals)

numbers = [100, 2, 36, 4, 9, 14, 10, 8]
print(numbers[::-1])#to reverse the list using slicing

numbers.sort()#sorts in ascending order
print(numbers)

animals_2 =["bear", "tiger", "zebra", "bat"]
animals.extend(animals_2)#Extend adds elements from one list to another list
print(animals)

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