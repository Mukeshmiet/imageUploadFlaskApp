from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename     # secure_filename is used to sanitize and secure filename before storing it
import os


app = Flask(__name__)

# uploaded Images folder path: 'C:/Users/Dell/Downloads/userImages'  or 'userImages'
app.config['UPLOAD_FOLDER'] = 'userImages'       

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    # secure_filename is used to sanitize and secure filename before storing it
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print('Image successfully uploaded')
    return redirect(url_for('image', filename=filename))

@app.route('/image/<filename>')
def image(filename):
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        return render_template('image.html', filename=filename)


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)