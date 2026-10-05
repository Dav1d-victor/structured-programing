x=5
while(x<=5):
    print(x)
    x+=1
    #x=x+1 is the same as x+=1

tuition=3500000
installment=1
totalpayment=0
balance= tuition-totalpayment

while (installment<=3):
    print("installment value:",installment)
    payment=int(input("how much paid?:"))
    totalpayment=totalpayment+payment
    print("so far you have paid:" ,totalpayment)
    installment+=1
    balance= tuition-totalpayment
if totalpayment>=tuition:
    print("you have completed the fees payment")
else:
    print("you have a fees balance of:" ,balance)
