class location :
    def __init__(self, fname,age):
        self.fname=fname
        self.age=48
        
    def first(self,age):
        return self.age - 8
    def capital(self,fname):
        return self.fname.upper()
    
    
        
      
mycity=location ("usama",48)

mycity1=location ("ahmed",49)
print("mycity1= ",mycity1.fname,mycity1.age)
print("-----------------------------------------------------------")
print(mycity1.first(49))
print("-----------------------------------------------------------")
print(mycity1.capital(""))
