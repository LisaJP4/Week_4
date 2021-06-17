from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///animals.db"

db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return "This is a Todo App"

@app.route('/')
@app.route('/add')
def add():
    return "Add a new Todo"

if __name__ == "__main__":
    app.run(debug=True)