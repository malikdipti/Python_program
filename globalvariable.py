a=100      #Global Variable
def show():
    print("hello world")
    b=30 #Local variable
    print(a+b)

c=70    #Global Variable
print(a+c)
show()
print(a+c)
#print(c+b)
    
