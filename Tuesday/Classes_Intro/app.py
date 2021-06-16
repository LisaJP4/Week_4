from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class

app = Flask(__name__) # create Flask object


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///world.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # create SQLALchemy object

class Countries(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    continent = db.Column(db.String(50))
    climate = db.Column(db.String(40))

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')