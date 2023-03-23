import flask
from flask import Flask
from flask import render_template
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

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

@app.route("/answer")
@app.route("/auto_answer")
def answer():
    inf = {
        "title": "Анкета",
        "name": "Mark",
        "surname": "Watny",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": True
    }
    return render_template("auto_answer.html", inf=inf, title=inf["title"])

@app.route("/login", methods=["GET", "POST"])
def double_protection():
    form = LoginForm()
    return render_template("double_protection.html", title="Аварийный доступ", form=form)

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

print("works")