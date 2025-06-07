class student:
    college_name="hr school"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno 
    def welcome(self):
        print("hello")           
s1=student("aditya",34)
print(s1.name,s1.rollno)
s1.welcome()
print(student.college_name)
s2=student("ashima",23)
print(s2.name,s2.rollno)
