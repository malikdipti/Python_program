class Details:
    def assign(self,id,name,gender):
        print("IDNO:",id)
        print("NAME:",name)
        print("GENDER:",gender)
class Employee(Details):
    def assign_emp(self,id,name,gender,company,dept):
        super().assign(id,name,gender)
        print("Company:",company)
        print("Department:",dept)
class Doctor(Details):
    def assign_doc(self,id,name,gender,hospital,dept):
        super(Doctor, self).assign(id,name,gender)
        print("Hospital:",hospital)
        print("Department:",dept)

e=Employee()
e.assign_emp(101,"Diptiranjan","Male","IBM","Developer")
print("-----------------------------------")
d=Doctor()
d.assign_doc(102,"Raaz","Male","AIIMS","Cardiology")

