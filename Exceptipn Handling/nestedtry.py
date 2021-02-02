try:
    a=int(input("Enter First Number"))
    b=int(input("Enter Second Number"))
    print("sum:",a+b)


    try:
        print("Div:", a/b)

    except ZeroDivisionError as zde:
        print(zde)
        print("mul:", a * b)
        print("sub", a - b)

except ValueError:
    print("invalid Input")

