class Person:
    # name="name"
    # age=0
    def __init__(self):        #method to intialiaze class parameters
        self.name= "noName-initial"
        self.age = -15

    def printDetails(self):              #method to print values
        print("\n Any Person Details")
        print("Name :", self.name)
        print("Age  :", self.age)
    
    def set_student(self,name,age): #methods to set new parameter values
        self.name = name
        self.age = age

person1 = Person()  # you need a setter method to set name/age values,this way you are creating an instance with default values
person1.printDetails()

print("------------------------------------------------------")

person1.name = "Mike"
person1.age = 21
person1.printDetails()

person1.set_student("Fayez Al-Dwairi",61)  #a setter method to set new values 
person1.printDetails()         #method to print out class
print("------------------------------------------------------")
print(person1.__dict__)  # print class details using builtin dict method

person2= Person()  # you need a setter method to set name/age values,this way you are creating an instance with default values
person1.printDetails()

