# Python code to test
import requests, json
# sample request
data = {"emp_ids":["1001","1002","1003"],"status":["active"]}
# Hitting the API with a POST request
ot = requests.post(url='http://localhost:6123/get_emp_info', json=json.dumps(data))
print(ot)