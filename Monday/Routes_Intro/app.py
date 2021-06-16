from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Type a country in and find out it's meaning..."

@app.route('/Germany/')
def Germany():
    return "Germany is a beautiful country. Berlin is a wonderful city for tourists."

@app.route('/France/')
def France():
    return "Oh no! France is terrible! The metro smells almost as bad as the river!"

if __name__=='__main__':
    app.run(debug=True)