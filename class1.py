class location :
    name="Usama"
    latitude = "25.594095"
    longtitude = "85.137566"
    city="CHICAGO"
    state="IL"
    country="USA"
    zipCode=60502
    age=1
    pic="pic1.png"

customer1=location()
print (customer1.state)
print(customer1.age +8)

customer1.age=40
print(customer1.age)
print(customer1.age+5)

print (customer1.name.upper())
print (customer1.city.lower())
print (customer1.latitude,customer1.longtitude)
print("-------------------------")

customer2=location()
print (customer2.state)
print(customer2.age) #add a comment