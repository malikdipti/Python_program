pin=int(input("Enter Your Pin:"))
balance=15000
if pin==1234:
    print("Welcome Diptiranjan")
    with_amount=int(input("Enter Amount:"))
    if with_amount<= balance :

        if with_amount%100==0 :

            if with_amount<=10000:
                print("collect Your Cash")
            else:
                print(" Maximum Withdraw amount shoule be 10000 ")
        else:
            print("Amount Should be Multiple Hundred " )
    else:
        print("Balance not Available")
else:
    print("Invalid Pin Number")
