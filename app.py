from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename     # secure_filename is used to sanitize and secure filename before storing it
import os


app = Flask(__name__)

# uploaded Images folder path: 'C:/Users/Dell/Downloads/userImages'  or 'userImages'
app.config['UPLOAD_FOLDER'] = 'userImages'       


# home page route  
@app.route('/')
def upload():
    return render_template('upload.html')


# upload image route    
@app.route('/upload', methods=['POST'])
def upload_image():
    error_message = None
    if 'image' not in request.files:
        error_message = 'image input is required in the form'
        print(error_message)
    else:
        file = request.files['image']
        if file.filename == '':
            error_message = 'image not selected'
            print(error_message)
        elif not allowed_images(file.filename):
            error_message = 'invalid image format, allowed formats are - png, jpg, jpeg, gif only'
            print(error_message)
        else:
            # secure_filename is used to sanitize and secure filename before storing it
            filename = secure_filename(file.filename)
            if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
                error_message = 'Image with the same name already exists.'
                print(error_message)
            else:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print('Image successfully uploaded')
                return redirect(url_for('image', filename=filename))
        
        return render_template('upload.html', error_message=error_message)


# image name display route   
@app.route('/image/<filename>')
def image(filename):
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        return render_template('image.html', filename=filename)
    else:
        return render_template('notexist.html'), 404


# allowed image formats checking function
def allowed_images(filename):
    if '.' not in filename:
        return False
    allowed_extensions = ('png', 'jpg', 'jpeg', 'gif')
    return filename.rsplit('.')[-1].lower() in allowed_extensions

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)