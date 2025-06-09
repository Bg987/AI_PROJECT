# Gender Detection from Uploaded Images using Face++ API

This Python project allows you to detect the gender of faces in an uploaded image using the Face++ API.  
The program lets you select an image file via a GUI file picker, sends the image to the Face++ API for face and gender detection, and displays the results visually with bounding boxes and gender labels.

---

## Features

- Select image files (`.jpg`, `.jpeg`, `.png`, `.jfif`) through a file dialog GUI  
- Detects faces and classifies gender for each detected face using Face++ API  
- Draws bounding boxes and gender labels on the image  
- Displays the annotated image using OpenCV  
- Uses environment variables to securely manage API credentials
    API_KEY=your_faceplusplus_api_key
    API_SECRET=your_faceplusplus_api_secret
    API_URL=https://api-us.faceplusplus.com/facepp/v3/detect

---

## Prerequisites

- Python 3.7 or higher  
- A Face++ API account with valid API Key and Secret (sign up at [https://www.faceplusplus.com/])  
- Install required Python packages listed in `req.txt` (pip install -r requirements.txt)

---

## Setup

1. Clone this repository or download the code files.
2. file structure.
    <br>├── gender_detection_upload.py - <b>Main Python script</b>
    <br>├── .env - <b>Environment variables file (secrets)</b>
    <br>├── .gitignore - <b>Git ignore file (includes .env)</b>
    <br>├── requirements.txt - <b>Python dependencies</b>
    <br>└── README.md - <b>This README file</b>
3. Run -  <b><u>python gender_detection_upload.py</u></b>


