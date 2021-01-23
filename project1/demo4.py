from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

book = {
    "name": "斗破苍穹",
    "auhtor": "xx",
    "articles": [
        {
            "id": 11,
            "title": "第一章：奥术大师大所大所多",
            "content": "qweasdasdwqeq"

        },
        {
            "id": 22,
            "title": "第二章：奥术大师大所大所多",
            "content": "qweasdasdwqeq"

        },
        {
            "id": 33,
            "title": "第三章：奥术大师大所大所多",
            "content": "qweasdasdwqeq"

        },

    ]

}
users = [
    {
        "email": "496575233@qq.com",
        "password": "123456"
    }
]
currentuser = None


@app.route("/")
def index():
    global currentuser
    user = currentuser
    articles = book["articles"]
    return render_template("index.html", **locals())


@app.route("/<int:pk>")
def detail(pk):
    global currentuser
    user = currentuser
    article = None
    for a in book["articles"]:
        if a["id"] == pk:
            article = a
    return render_template("detail.html", **locals())


@app.route("/login", methods=["GET", "POST"])
def login():
    global currentuser
    if request.method == "GET":
        return render_template("login.html", **locals())
    elif request.method == "POST":
        user = None
        email = request.form.get("email")
        password = request.form.get("password")
        for u in users:
            if u["email"] == email and u["password"] == password:
                currentuser = u
                print(currentuser, "====")
                return redirect(url_for("index"))
        print("登录失败")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    global currentuser
    currentuser = None
    user = currentuser
    return redirect(url_for("index"))


@app.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html", **locals())
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        global users
        users.append({
            "email": email,
            "password": password
        })
        print("当前用户有", users)
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
