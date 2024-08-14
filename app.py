from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URi"]
@app.route('/')
def index():
    return render_template("index.html")
    if __name__ == '__main__':
     app.run(debug = True)
