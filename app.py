import testrunner
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.tpl")


@app.route("/results", methods=["POST"])
def results():
    address = request.form.get("address")
    print(request.form)
    XSS = request.form.get("XSSbutton", False)
    XSSResult = False
    if XSS:
        XSSResult = testrunner.xsstest(address)

    SQL = request.form.get("SQLbutton", False)
    SQLResult=False
    if SQL:
        SQLResult = testrunner.sqltest(address)
    return render_template("results.tpl", XSS=XSS, SQL=SQL, url=address,
                           XSSResult=XSSResult, SQLResult=SQLResult)

app.run("localhost", debug=True)
