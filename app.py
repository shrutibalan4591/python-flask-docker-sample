from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    app.run(debug=True)
