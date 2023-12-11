# creating a class with the name Student
class Student(object):

   # constructor of the student class
   def __init__(self):

      # initiaizing the values of attributes with None
      self.studentName = None
      self.rollNumber = None
      print('The Value of Student Name:',self.studentName)
      print('The Value of Roll Number:',self.rollNumber)

#Creating the Object for the student class
studentObject1=Student()
studentObject2=Student()