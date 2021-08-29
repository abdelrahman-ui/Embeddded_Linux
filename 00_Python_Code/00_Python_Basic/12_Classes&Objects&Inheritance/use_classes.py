from ClassesAndObject import Employee

employee_1 = Employee("Abdo",60,"Home",True,10,1550)
employee_2 = Employee("DINA",23,"Home",False,7.5,1000)

print("Sallery 1 : ",employee_1.sallary)
employee_1.Bonus()
print("Sallery 2 : ",employee_2.sallary)
employee_2.Bonus()
print("Name is",employee_1.name,"his Age =",employee_1.age,"iS Good -->",employee_1.Is_Exceellent())
print("Name is",employee_2.name,"his Age =",employee_2.age,"iS Good -->",employee_2.Is_Exceellent())
from ClassesAndObject import Student
Student_1=Student("Abdo",15,"Mecatronics",3.17,"ERU")
print("Student Name is --> ",Student_1.name, "his Age = ",Student_1.age," The department is -->",Student_1.department,"Stady At -->",Student_1.Collage)

from Doctors import Doctor
doctor_1 =Doctor()
doctor_1.Student_Year()
doctor_1.Works_Where()
doctor_1.Paid_by_Who()
print("========= Inheritance =========")
from Famly_Doctor import FamilyDoctor
doctor_2 =FamilyDoctor()
doctor_2.Student_Year()
doctor_2.Works_Where()
doctor_2.What_Specialization()
doctor_2.Paid_by_Who()