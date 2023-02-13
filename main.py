import flask
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('base.html', title='Заготовка',
                           username=user)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")