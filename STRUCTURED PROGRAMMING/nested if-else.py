maritalstatus=input("enter married/unmarried")
gender=input("enter male/female")
age=int(input("enter your age"))

if maritalstatus=="married":
    print("eligible for insurance")
else:
    if maritalstatus=="unmarried":
        if gender=="male":
            if age>30:
                print("eligible for insurance")
            else:
                print("not eligible for insurance")
        else:
            if gender=="female":
                if age>25:
                    print("eligible for insurance")
                else:
                    print("not eligible for insurance")