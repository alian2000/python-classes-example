from flask import Flask,render_template, flash, redirect
from flask_restful import Resource, Api, reqparse
#https://www.blog.duomly.com/python-api-tutorial/

app = Flask(__name__) # usama app variable is equal to instance of flask flask,__name__ is a special variable in python, just a name of the module
api = Api(app)

STUDENTS = {
  '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
  '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
  '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
  '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}
parser = reqparse.RequestParser()

class StudentsList(Resource):
    def get(self):
        return STUDENTS




    def post(self):
        parser.add_argument("name", location="args")
        parser.add_argument("age", location="args")
        parser.add_argument("spec", location="args")
        args = parser.parse_args()
        student_id = int(max(STUDENTS.keys())) + 1      # find the max number in the current student key and add one for the new post
        student_id = '%i' % student_id
        STUDENTS[student_id] = {                  #start building a new entry in the dictionary variable
            "name": args["name"],                 # first key/value "name":args["name"] , you can print it as well as shown below
            "age": args["age"],                   # 2nd key/value , you can print it as well as shown below
            "spec": args["spec"],                 # 3rd key/value , you can print it as well as shown below

        }
        print("--------")
        print(args.name)
        print(args.age)
        print(args.spec)

        return STUDENTS[student_id], 201
class Student(Resource):
    def get(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            return STUDENTS[student_id]


    def put(self, student_id):
        parser.add_argument("name", location="args")
        parser.add_argument("age", location="args")
        parser.add_argument("spec", location="args")
        args = parser.parse_args()
        if student_id not in STUDENTS:
            return "Record not found", 404
        else:
            student = STUDENTS[student_id]
            student["name"] = args["name"] if args["name"] is not None else student["name"]
            student["age"] = args["age"] if args["age"] is not None else student["age"]
            student["spec"] = args["spec"] if args["spec"] is not None else student["spec"]
            return student, 200

    def delete(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            del STUDENTS[student_id]
            return '', 204

api.add_resource(Student, '/students/<student_id>')

api.add_resource(StudentsList, '/students/')
@app.route('/sts')
def say_hannah():
    return "Greet from Hannah from Server"
@app.route("/")
def hello_world():
    print("Alive")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8080)
    #app.run()


#You can't store the object itself in the DB.
# What you do is to store the data from the object and reconstruct it later.
#https://stackoverflow.com/questions/2047814/is-it-possible-to-store-python-class-objects-in-sqlite



