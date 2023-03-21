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

@app.route("/list_prof/<list_type>")
def show_list(list_type):
    professions = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач",
                   "инженер по терраформированию", "климатолог", "специалист по радиационной защите",
                   "астрогеолог", "гляциолог", "инженер жизнеобеспечения", "метеоролог",
                   "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    return render_template("show_list.html", list_type=list_type, professions=professions)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

print("works")