class A :
    def __init__(self):
        print(" class A")
class B :
    def __init__(self):
        print(" class B")
class c (A,B):
    def m1():
        print("m1")

x= c()
print(x)
