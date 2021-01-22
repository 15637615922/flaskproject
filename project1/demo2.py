from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "欢迎来到Flask"


@app.route("/<int:pk>")
def stage(pk):
    return f"欢迎来到Flask{pk}"


if __name__ == '__main__':
    app.run(host='192.168.11.26', port="4396", debug=True)
