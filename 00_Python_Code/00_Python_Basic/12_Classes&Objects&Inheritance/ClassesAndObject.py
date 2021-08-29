class Employee:
    def __init__(self,name ,age , department,is_manager,rating,sallary):
        self.name=name
        self.age=age
        self.department=department
        self.is_manager =is_manager
        self.rating=rating  # Range From 0 : 10
        self.sallary=sallary

    def Is_Exceellent(self):
        if self.rating >=7 :
            return True
        else:
            return False

    def Bonus(self):
        if self.age==60:
            self.sallary +=50
            print("After Bonus Sallery = ",self.sallary)
        else:
            print("No Bonus")

class Student:
    def __init__(self, name, age, department, GPA , Collage):
        self.name=name
        self.age = age
        self.department = department
        self.GPA=GPA
        self.Collage=Collage


