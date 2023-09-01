from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hi, I am Mukesh Kumar'

@app.route('/about')
def about():
    return 'On the way to become a Python Developer'

if __name__ == '__main__':
    app.run(debug=True)