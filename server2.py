from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

db = list()
test = list()

def init_server():
    add_patient_to_db("Ann Ables", 101, "A+")
    add_patient_to_db("Bob Boyles", 102, "B-")


def add_patient_to_db(name, id, blood_type):
    new_patient = {"name": name,
                   "id": id,
                   "blood_type": blood_type,
                   "test": list()}
    db.append(new_patient)
    # print(db)
    logging.info(new_patient)
    return True


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # get input data from requests
    in_data = request.get_json()
    # validate data
    answer, server_status = process_new_patient(in_data)
    return answer, server_status
    # # define new pateint dictionary
    # add_patient_to_db(in_data["name"]), in_data["id"], in_data["blood_type"]
    # # return display results
    # return "Patient added", 200


def validate_blood_type(in_data):
    blood_types = ["O+", "O-", "A+", "A-", "B+", "B-"]
    if in_data["blood_type"] not in blood_types:
        return "{} is not a valid blood type".format(in_data["blood_type"])
    return True, 200


def validate_new_patient_info(in_dict):
    expected_keys = ("name",  "id", "blood_type")
    expected_type = (str, int, str)
    for key, ty in zip(expected_keys, expected_type):
        if key not in in_dict.keys():
            return "{} key not found".format(key), 400
        if type(in_dict[key]) != ty:
            return "{} key has the wrong value type".format(key), 400

    return True, 200


def process_new_patient(in_data):
    validate_input, server_status = validate_new_patient_info(in_data)
    if validate_input is not True:
        return validate_input, server_status
    valid_blood_type = validate_blood_type(in_data)
    if valid_blood_type is not True:
        return valid_blood_type, 400

    add_patient_to_db(in_data["name"], in_data["id"], in_data["blood_type"])
    return "Patient successfully added", 200


def add_test_to_db(id, test_name, test_result):
    new_test = {"id": id,
                "test_name": test_name,
                "test_result": test_result}
    test.append(new_test)
    logging.info(new_test)
    return True


@app.route("/add_test", methods=["POST"])
def add_tests():
    tests = request.get_json()
    answer, server_status = process_new_tests(tests)
    return answer, server_status


def validate_new_test_info(in_dict):
    expected_keys = ("id",  "test_name", "test_result")
    expected_types = (int, str, int)
    for key, ty in zip(expected_keys, expected_types):
        if key not in in_dict.keys():
            return "{} key not found".format(key), 400
        if type(in_dict[key]) != ty:
            return "{} key has the wrong value type".format(key), 400
    return True, 200


def process_new_tests(in_data):
    validate_input, server_status = validate_new_test_info(in_data)
    if validate_input is not True:
        return validate_input, server_status

    add_test_to_db(in_data["id"], in_data["test_name"], in_data["test_result"])
    return "Test successfully added", 200


if __name__ == '__main__':
    init_server()
    app.run()