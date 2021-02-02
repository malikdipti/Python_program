try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    print("Sum:",a+b)
    print("Div:",a/b)
    print("mul:",a*b)
    print("sub:",a-b)
except ZeroDivisionError as zde:
    print(zde)

except ValueError:
    print("Invalid input")