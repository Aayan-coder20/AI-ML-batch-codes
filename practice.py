class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa


stu1 = Student("Aayan",8)
stu2 = Student("Huzaifa",9)
stu3 = Student("Gasif",7)

print(f"{stu1.name} has a cgpa of {stu1.cgpa}")
