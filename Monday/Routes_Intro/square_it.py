from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Type a number in and have it be squared..."

@app.route('/squared/<int:number>')
def square(number):
    number = int(number)
    result = number * number
    return str(number) + "  squared is equal to:  " + str(result)

if __name__=='__main__':
    app.run(debug=True)