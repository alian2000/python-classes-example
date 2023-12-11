STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}
class studentlist:
    def create_dictionary():
        return STUDENTS

    def set_student(self,key, name, age,spec):
        self.key = key
        self.name = name
        self.age = age
        self.spec= spec

print (studentlist.create_dictionary())
print(studentlist.set_student("self",5,"wafa",41,"world"))