from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
# secure_filename is used to sanitize and secure filename before storing it
from werkzeug.utils import secure_filename
import os
import jwt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import datetime
# To decode the base64 data URL to obtain the image data
import base64
from PIL import Image
from io import BytesIO


app = Flask(__name__)

# uploaded Images folder path
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'image')
# Check if the folder directory exists, if not then create it
if not os.path.exists(app.config['UPLOAD_FOLDER'] ):
    os.makedirs(app.config['UPLOAD_FOLDER'] )

# It Generates 'app_secret_key', a random secure secret key with 32 bytes (256 bits)
#import secrets
#SECRET_KEY = secrets.token_hex(32)

SECRET_KEY = 'b9dd0c9baeccb0cd3af3c9e14f26d405653e54afc742f46e9d7fb03a4e3e63b4'  

# create a limiter object
limiter_5 = Limiter( get_remote_address, app= app, default_limits=["5 per minute"] ) 

# Create a route to generate a JWT token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()   # a JSON request with user data
    if data['username'] == 'flaskApp' and data['password'] == 'App@123':
        token = jwt.encode({'user': data['username']}, SECRET_KEY, algorithm='HS256')
        print(token)
        return jsonify({'token': token})
    return jsonify({'message': 'Authentication failed'}), 401

#  Create a protected route that requires a valid JWT token to access
@app.route('/protected', methods=['GET'])
@limiter_5.limit("5 per minute")    # limit the number of requests to 5 per minute
def protected():
    token = request.headers.get('Authorization')
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({'message': 'Access granted'})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

# home page route  
@app.route('/')
def upload():
    return render_template('upload.html')

#capture route to capture image from camera, save it to UPLOAD_FOLDER and then render it on the same page
@app.route('/capture' , methods=['GET','POST'] )
def capture():
    filename=''     # using filename variable to display video feed and captured image alternatively on the same page
    image_data_url = request.form.get('image')
    if request.method == 'POST':
        # Decode the base64 data URL to obtain the image data
        image_data = base64.b64decode(image_data_url.split(',')[1])
        # Create an image from the decoded data
        img = Image.open(BytesIO(image_data))
        # Generate a filename with the current date and time
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        filename = f"img_{timestamp}.png"  # Change file extension to 'png'
        print(filename)
        # Save the image in PNG format
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        img.save(file_path, 'PNG')
        error_message = 'Image successfully captured'
        # use if you want to display all the images in the folder
        # image_files = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('capture.html', filename=filename)
    return render_template('capture.html', filename=filename)


# upload image route    
@app.route('/upload', methods=['POST'])
def upload_image():
    error_message = None
    if 'image' not in request.files:
        error_message = 'image input is required in the form'
        print(error_message)
    else:
        file = request.files['image']
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            error_message = 'image not selected'
            print(error_message)
        # check if the file is allowed or not by checking its extension
        elif not allowed_images(file.filename):
            error_message = 'invalid image format, allowed formats are - png, jpg, jpeg, gif only'
            print(error_message)
        else:
            # secure_filename is used to sanitize and secure filename before storing it
            filename = secure_filename(file.filename)
            # check if the file with the same name already exists or not
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
    #check if the image file exists or not in the folder
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        return render_template('image.html', filename=filename)
    else:
        return render_template('notexist.html'), 404

# image display route from video feed
@app.route('/capturedimage/<filename>')
def captured(filename):
    # returned the image path to template where it is rendered
    return send_from_directory(app.config['UPLOAD_FOLDER'], path=filename)

# allowed image formats checking function
def allowed_images(filename):
    if '.' not in filename:
        return False
    allowed_extensions = ('png', 'jpg', 'jpeg', 'gif')
    return filename.rsplit('.')[-1].lower() in allowed_extensions

# error handling route
@app.errorhandler(Exception)
def handle_error(error):
    print(error)
    return render_template('error.html'), 404

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # running app with ssl certificate for https connection
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'), debug=False)
    # app.run(debug=True)