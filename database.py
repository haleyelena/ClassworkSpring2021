def create_database_entry(name, id_no, age):
    #new_patient = [name, id_no, age, []]
    new_patient = {"name": name, "id": id_no, "age": age, "test": list()}
    return new_patient

def print_dictionary(db):
    other_data = ["Room 2", "Room 3", "Room 4", "Room 5"]
    for i, patient in enumerate(db):
        print(i)
        print("Name: {}, id: {}, age: {}".format(patient[0],patient[1], patient[2]))
        print("Patient is in {}".format(other_data[i]))

def find_patient(id_no, db):
    for patient in db:
        if patient[1] == id_no:
            answer = patient[0]
            break
    return answer

def add_test_result(id_no, db, test_name, test_results):
    for patient in db:
        if patient["id"] == id_no: 
            patient["test"].append((test_name, test_results))
    
def print_db(db):
    for patient in db:
        print_patient(patient)

def print_patient(patient):
    for key in patient:
        print(" {} = {}".format(key, patient[key]))

def demo(patient):
    if "name" in patient:
        print("Name is {}".format(patient["name"]))
    if "DOB" in patient:
        print("DOB is {}".format(patient["DOB"]))

def minor_or_adult(patient):
    if patient["age"] >= 18:
        print("Adult")
    else:
        print("Minor")

def main():
    db = list()
    db.append(create_database_entry("Ann Ables", 1, 30))
    db.append(create_database_entry("Bob Boyles", 2, 31))
    db.append(create_database_entry("Chris Chou", 3, 32))
    db.append(create_database_entry("David Dinkins", 4, 33))
    print_db(db)
    demo(db[0])
    minor_or_adult(db[0])
    #print(db)
    #add_test_result(3, db, "HDL", 65)
    #print(db)
    #add_test_result(3, db, "LDL", 80)
    #print(db)
    

if __name__ == "__main__":
    main()
    