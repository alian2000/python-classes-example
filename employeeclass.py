#from distutils.command.build_scripts import first_line_re
#from http.client import PAYMENT_REQUIRED


class Employee:
    def __init__(self , first,last,pay,gender):
        self.first = first                       # first is class variables
        self.last = last
        self.pay = pay
        self.email = first +'.'+last + '@company.com'
        self.gender = gender
    def fullname(self):
        #return '{} {} {} {} {}'.format(self.first,self.last,self.pay,self.email,self.gender)
        return (self.first,self.last,self.pay,self.email,self.gender)     

emp_1=Employee('usama','Elayyan',50000,'male')    # emp_1 is an instance of class Employee
emp_2=Employee('Tamer','alian',60000,'male')      # Tamer value is an instance emp_2 variable first value 

totalSalary =(emp_1.pay+emp_2.pay)

print ("totalSalary= ",totalSalary)
print (emp_1.first,emp_2.first)
# print(emp_2.fullname())  # we used class instance or object with the function fullname.
# print(emp_2.__dict__) #applying __dict__ method on the class instance emp_2 
print("----------------------------------")
print(emp_1.__dict__)  
print("----------------------------------")
print (Employee.fullname(emp_2))


