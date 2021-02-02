f_name=input("Enter file name or path:")

try:
    f=open(f_name)
    data=f.read()
except FileNotFoundError as fnfe:
    print(fnfe)

else:
    print(data)
    f.close()
