import requests


def get_branches():
    r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
    print(r)
    print(type(r))
    print(r.status_code)
    print(r.text)
    branches = r.json()
    print(branches)
    for branch in branches:
        print(branch["name"])


def countries():
    server = "http://vcm-7631.vm.duke.edu:5000"
    r = requests.get(server+"/countries")
    print(r.status_code)
    print(r.text)

    my_countries = {"one": "Austria", "two": "Argentina"}
    r = requests.post(server+"/compare", json=my_countries)
    print(r.status_code)
    print(r.text)
    data = r.json()
    print(data)


def name():
    server = "http://vcm-6764.vm.duke.edu:5000"
    my_name = {"name": "Haley Snyder", "net_id": "hes22", "e-mail": "haley.snyder@duke.edu"}
    r = requests.post(server + "/student", json=my_name)
    print(r.status_code)
    print(r.text)
    data = r.json()
    print(data)

    r = requests.get(server + "/list")
    print(r.status_code)
    print(r.text)

def blood_type():
    server = "http://vcm-7631.vm.duke.edu:5002"
    r = requests.get(server + "/get_patients/hes22")
    print(r.status_code)
    print(r.text)

    r = requests.get(server + "/get_blood_type/M4")
    print(r.status_code)
    print(r.text)
    r = requests.get(server + "/get_blood_type/M5")
    print(r.status_code)
    print(r.text)

    my_match = {"Name": "hes22", "Match": "No"}
    r = requests.post(server + "/match_check", json=my_match)
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    blood_type()
