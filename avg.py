# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hii",self.name,"your average score is",sum/3)    
# s1=Student("ankit",[56,78,90])
# print(s1.name,s1.marks) 
# s1.get_avg()
# s2=Student("anshu",[80,90,89])
# print(s2.name,s2.marks)
# s3=Student("ABC",[67,98,90])
# print(s3.name,s3.marks)       


class Student:
    college_name="pd pandya"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hii",self.name,"your avarage marks is ",sum/3) 
    @staticmethod    
    def welcome():
        print("welcome")           
s1=Student("ankit",[56,89,90,99,90])
s1.name="anushka"#if i want to change the name so here and in this way i can change the name
print(s1.name,s1.marks)
s1.get_avg()
s2=Student("akay",[38,9,88,78,56])
print(s2.name,s2.marks)
s2.get_avg()
s3=Student("essa",[45,78,89,89,59,45,6,789])
print(s3.name,s3.marks)
s3.get_avg()
s3.welcome()


