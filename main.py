from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/fun/', methods=["GET", "POST"])
def fun():

    return render_template('fun.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        get_first = request.form.get('first')
        get_last = request.form.get('last')

        return render_template("result.html", get_first_tem=get_first, get_last_tem=get_last)


if __name__ == '__main__':
    app.run(debug=True)
