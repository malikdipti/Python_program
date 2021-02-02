l1=[6,5,65,32,41,26]
l2=[]
for x in l1:
    if(x%2==0):
        l2.append(x)
print(l2)


print("-------------------------------------")
#comprehension list
l3=[x for x in l1 if x%2==0]
print(l3)