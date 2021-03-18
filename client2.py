import requests

patient = {"name": "Evan",
           "id": 1,
           "blood_type": "O+"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=patient)
print(r.status_code)
print(r.text)

tests = {"id": 1, "test_name": "HDL", "test_result": 60}
r = requests.post("http://127.0.0.1:5000/add_test", json=tests)
print(r.status_code)
print(r.text)
