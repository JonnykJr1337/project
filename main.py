from data import db_session
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("base.html")


if __name__ == "__main__":
    db_session.global_init("db/paste.db")
    app.run()
