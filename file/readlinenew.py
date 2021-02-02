import re
f=open("sample.txt")
data=f.read()
res=re.findall(r'\ba\w+',data)
res1=re.findall(r'\bb\w+',data)
res2=re.findall(r'\bc\w+',data)
res3=re.findall(r'\bd\w+',data)
res4=re.findall(r'\be\w+',data)
res5=re.findall(r'\bf\w+',data)
dict={"A":res,"B":res1,"C":res2,"D":res3,"E":res4,"F":res5}

print(dict)