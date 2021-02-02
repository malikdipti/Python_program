a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
print("sum:",a+b)

try:
    print("div:",a/b)
except ZeroDivisionError as zde:
    print(zde)
print("mul:",a*b)
print("sub:",a-b)

