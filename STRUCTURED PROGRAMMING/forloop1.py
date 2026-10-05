#for loop is for counting a sequence where the first variable is included and the last is excluded.
w=20
k=101

for w in range (w,k):
    print(w)


##write a forloop to print the first 100 numbers
w=1
k=101
i=1
for w in range (w,k):
    print(w)

## the first 100 even numbers
w=0
k=201
for w in range (w,k):
    if w%2 ==0:
        print(w)
        count +=1
print(f"count: {count}")

##method 2
a=0
b=100
count = 0
for i in range(a,b,2):
    print(i,end="")
    count +=1


##
ages = [20,18,33,19,15,12,59,60]
for age in ages:
    print(age)


ages = [20,18,33,19,15,12,59,60]
for age in ages:
    print(age,end=" ")


print("task2")
#QN.display the first odd age value.

for age in ages:
    if age%3 ==0:
        print(age)
        break##as long as you find what you need it will stop.
##we use breaks only in loops.

print("task3")
for age in ages:
    if age%4 ==0:
        print(age)
        continue##skips a number that does not meet the criteria.

print(20)
