#Create an Employee class with attributes role, department, salary, this class will have a showDetails() method

class Employee():

    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}")

    
class Engineer(Employee):

    def __init__(self, name, age):
        super().__init__("Enginner", "IT", "60,000")
        self.name = name
        self.age = age

    #overriding the parent class instance method
    def showDetails(self):
        print(f"name: {self.name}, age: {self.age}, Role: {self.role}, Department: {self.department}, Salary: {self.salary}")


emp1 = Employee("Salesman","Sales","35,000")
emp1.showDetails()

eng1 = Engineer("Jay", "23")
eng1.showDetails()


