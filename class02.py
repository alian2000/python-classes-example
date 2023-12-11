class location :
    def __init__(self, fname, lname,latitude,longtitude,city,state,country,zipcode=0,age=0):
        self.fname=fname
        self.lname=lname
        self.latitude = latitude
        self.longtitude = longtitude
        self.city=city
        self.state=state
        self.country=country
        self.zipCode=zipcode
        self.age=age
    def first(self,fname):
        self.fname=fname
        return fname
        
      
mycity=location ("usama","alian",33,34,"chicago","IL","USA",60525,21)

mycity1=location ("ahmed","khaleel",33,34,"chicago","IL","USA",60525,21)
print("mycity1= ",mycity1.city)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(mycity.first("newName"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
average=(mycity.age+mycity1.age)/2
print(average)
print(mycity.age+9)
print(mycity.city.upper())
print(mycity.city.upper().split("A")[0])

print (mycity.__dict__)

print("reversed= ",mycity.city[::-1])
    
#mycity1.fisrt1("sama")