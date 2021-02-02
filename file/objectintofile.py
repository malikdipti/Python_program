import pickle as pi
idno=101
name="diptiranjan"
marks=[10,20,30,40]
total=sum(marks)

file=open("employee.txt","wb")
pi.dump(idno,file)
pi.dump(name,file)
pi.dump(marks,file)
pi.dump(total,file)
file.close()
print("write to file")