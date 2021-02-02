l1=[10,20,35,65,35,48,98,68,64]
sum=0
for x in l1:
    sum=sum+x
print("sum:",sum)
print("-----------------------------")

for x in l1:
    if x%2==0:
     print(x,end=" ")