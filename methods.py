# Create a simple Student class that will take in name and marks of Three subjects and get their avg marks

class Student():

    college = "GEC-Rajkot"


    @staticmethod       #utility method does not change class or object attributes
    def helloWorld():
        print("Hello World")    

    
    @classmethod            #used when we require to change class attributes
    def updateCollege(cls, new_clg_name):
        cls.college = new_clg_name
    

    def __init__(self, name, phy, chem, math):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math

    #instance method
    def get_avg_marks(self):
        return (self.phy+self.chem+self.math)//3
    

s1 = Student('Jay',91, 87, 96)
print(s1.get_avg_marks())

Student.helloWorld()

print(Student.college)
Student.updateCollege("Other College")
print(Student.college)

