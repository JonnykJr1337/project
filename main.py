from data import db_session
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Привет!"


if __name__ == "__main__":
    db_session.global_init("db/paste.db")
    app.run()
