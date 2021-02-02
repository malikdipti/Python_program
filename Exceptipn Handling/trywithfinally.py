f_name=input("enter file name or path:")
try:
    f = open(f_name)
    data= f.read()
except FileNotFoundError as fnfe:
    print(fnfe)
else:
    print(data)


finally:
    f.close()

print("Thanks")
