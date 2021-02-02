import pickle as pi
file=open("employee.txt","rb")
idno = pi.load(file)
print(idno)
name = pi.load(file)
print(name)
marks = pi.load(file)
print(marks)
