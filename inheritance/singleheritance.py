class Employee:
    def assign(self,idno,name):
        self.idno=idno
        self.name=name
class TempEmployee(Employee):
    def assign_salary(self,salary,designation):
        self.salary=salary
        self.designation=designation

    def display(self):
        print("IDNO:",self.idno)
        print("NAME",self.name)
        print("SALARY:",self.salary)
        print("DESIGNATION:",self.designation)

te=TempEmployee()
te.assign(101,"Diptiranjan")
te.assign_salary(185000,"Python Developer")
te.display()
