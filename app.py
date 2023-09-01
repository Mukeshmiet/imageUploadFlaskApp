from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/image')
def about():
    return render_template('image.html', filename='image.jpg')

@app.route('/notexist')
def about():
    return render_template('notexist.html')

@app.errorhandler(Exception)
def handle_error(error):
    print(error)
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)