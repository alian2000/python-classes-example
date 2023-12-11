
class student:
    def __init__(self, name , age):
        self.name= name
        self.age = age
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
        
    def get_student(self): 
        return self.name,self.age
        
        
    
    def set_student(self, name,age): 
        self.name = name
        self.age = age

student1 = student("usama",48) 

# setting the age using setter 
#student1.set_student(tamer, 15)
  

# retrieving age using getter
print(student1.get_name())
print("-----------------------------------")
print(student1.get_student())
print("************************************")


print(student1.name) 
print(student1.age) 

student1.set_student("wafa",41)
print("--------------------------------------")
print(student1.name)
print(student1.age) 