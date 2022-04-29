from data import db_session
from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_required, logout_user, login_user
from data.users import User

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config["SECRET_KEY"] = "LONG_LONG_LONG_LONG_LONG)"


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def main():
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    form = request.form
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.login == form.get("login")).first()
    if user and user.check_password(form.get("password")):
        login_user(user, remember=bool(form.get("remember", False)))
        return redirect("/")
    return render_template("login.html", error="Пароль неверный, ты ублюдок! 666")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    db_session.global_init("db/paste.db")
    app.run()
