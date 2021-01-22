from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    name = "cll"
    age = "20"
    info = "未婚"
    return render_template("index.html", **locals())


if __name__ == '__main__':
    app.run(debug=True)
