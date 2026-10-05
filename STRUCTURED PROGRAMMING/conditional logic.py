math = int(input("enter scores for math:"))
phy = int(input("enter scores for phy:"))
bio = int(input("enter scores for bio:"))
chem = int(input("enter scores for chem:"))

total = math + phy + bio + chem
average = total/4

print(total)
print(average)

if average >= 80 and average <=100:
    print("outstanding")

if average >=70 and average <80:
    print("good")

if average >=60 and average <70:
    print("fair")

if average <=59 and average <=29:
    print("poor")
    