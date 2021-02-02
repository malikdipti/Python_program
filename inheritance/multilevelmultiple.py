class A:
    def assign(self,id,name,salary):
        print("IDNO:",id)
        print("NAME:",name)
        print("SALARY:",salary)
class B(A):
    def assign_b(self,id,name,salary,dept,designation):
        super().assign(id,name,salary)
        print("Department",dept)
        print("Designation",designation)
class D:
    def assign_d(self,address):
        print("ADDRESS",address)
class C(B,D):
    def assign_c(self,id,name,salary,dept,designation,address,gender):

        super().assign_b(dept,designation)




        print("Gender",gender)
x=C()
x.assign_c(101,"satya",185000,"Developer","Python Developer","Hyderabad","Male")
x.assign_b("Developer","Python Developer")
x.assign_d("Hyderabad")