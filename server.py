from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods={"GET"})
def server_status():
    return "The server is on."


@app.route("/info", methods={"GET"})
def information():
    output = "This server will allow the user to request blood analyses"
    return output


@app.route("/HDL", methods={"POST"})
def hdl_request():
    """
    input info: {"HDL": 60}

    :return: string
    """
    from blood_tests import analyze_HDL
    in_data = request.get_json()
    print(in_data)
    HDL = in_data["HDL"]
    result = analyze_HDL(HDL)
    answer = {"HDL": HDL, "Analysis": result}
    if answer != "Normal":
        return "Bad HDL", 400
    # return "The result for a blood level of {} is {}".format(HDL, result)
    return jsonify(answer)
    # can only accept string returns so jsonify turns whatever your doing into
    # a json formatted string


@app.route("/say_hello/<person>/<age>", methods={"GET"})
def say_hello_function(person, age = 40):
    next_year = int(age) + 1
    output = "hello there, {}! You will be {} old next year".format(person, next_year)
    return output


if __name__ == '__main__':
    app.run()
