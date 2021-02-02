class A :
    def __init__(self,no1,no2):
        print("sum:",no1+no2)
        print("sub",no1-no2)



class B(A):
    def __init__(self,no1,no2):
        super().__init__(no1,no2)
        print("mul", no1*no2)
        print("div",no1/no2)

class C(B):
    def __init__(self,no1,no2):
        super().__init__(no1,no2)
        print("mod", no1%no2)
        print("expo",no1**no2)



x=C(10,2)




