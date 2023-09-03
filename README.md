# Image Upload and Capture App 
(Visit: https://capture-upload-image-app.onrender.com/ )

Welcome to the Image Upload and Capture App repository! This project aims to create a versatile web application, Android, and iOS app using the Python Flask framework. With this app, users can easily upload images to the server and also capture photos using their device's camera, all while enjoying a seamless user experience.

## Features

- **Image Upload**: Users can effortlessly upload images from their device's storage to the app. This feature is perfect for sharing existing photos.
    ##Visit: (https://capture-upload-image-app.onrender.com/)  -- to upload image

- **Camera Capture**: Want to snap a new photo? No problem! The app allows users to use their device camera to capture pictures instantly, the captured image will automatically upload on server, providing a dynamic and interactive experience.
    ##Visit: (https://capture-upload-image-app.onrender.com/capture)  -- to capture image from camera and upload it

- **Key based authentication system using JWT token**: Want to test authentication by http POST method on (https://capture-upload-image-app.onrender.com/login) with json body " {"username":"flaskApp", "password":"App@123"} ", that will give access token or authentication failed message in json, after that you can test generated token by http GET method on ( https://capture-upload-image-app.onrender.com/protected ) with header value "  'Authorization': '<your access token here>'  ", this will give you json message that 'Access granted' or 'Token has expired' or 'Invalid token' based on the access token.

- **Set your access limit**: With Flask limiter you can easily apply rate limit i.e. if number of server hits exceeded your apply limit then user cannot access website untill the set time passes, you can easily set "3 per minute" or "60 per hour" or "200 per day". In this you can easily manage traffic on your server.

- **Cross-Platform Compatibility**: This project is designed to work seamlessly across multiple platforms, including web, Android, and iOS. Users can access the app on their preferred device.

## Installation

To get started with the Image Upload and Capture App, follow these installation instructions:

1. Clone the repository to your local machine:
2. Navigate to the project directory and then Install the required dependencies using :  pip install -r requirements.txt
3. Open terminal at project folder and then run the app using : "python app.py" 
4. If Ask then use pass: "App@123" for SSL, make sure debugging if False
5. Connect your device with the same wifi network
6. Then in your browser navigate to the address something similar to (eg. https://192.168.24.53:5000) shown in the terminal.


### License

This project is licensed under the MIT License.

### Contact

If you have any questions or suggestions, please feel free to contact us at " mukesh.kumar.me.2018@miet.ac.in " .

Happy coding!
