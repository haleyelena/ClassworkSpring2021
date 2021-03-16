import requests

server = "http://127.0.0.1:5000"
r = requests.get(server+"/")
print(r.status_code)
print(r.text)

blood_data = {"HDL": 5}
r = requests.post(server+"/HDL", json=blood_data)
# answer = r.json() # this makes is a json file, so will last print statment will
# return actual data type
print(r.status_code)
print(r.text)
print("Type of r.text is {}".format(type(r.text)))