from bottle import route, run, template


@route("/new-party")
def new_party():
    return template("new_party")


@route("/")
def main_page():
    return template("main_page")


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True, reloader=True)
