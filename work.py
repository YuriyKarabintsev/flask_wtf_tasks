import flask
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    print("index")
    return render_template('base.html', title='Заготовка')

@app.route("/training/<prof>")
def profession(prof):
    print(prof)
    return render_template("prof.html", prof=prof)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

print("works")