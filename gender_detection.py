import cv2
import requests
import base64
from tkinter import filedialog, Tk
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env file

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
API_URL =os.getenv('API_URL')

def choose_image():
    Tk().withdraw()  # Hide main Tkinter window
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.jfif")],
        title="Choose an image"
    )
    return file_path

def detect_gender(image_path):
    with open(image_path, 'rb') as f:
        img_data = base64.b64encode(f.read()).decode()

    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'image_base64': img_data,
        'return_attributes': 'gender'
    }

    response = requests.post(API_URL, data=data)
    if response.status_code != 200:
        print("API error:", response.status_code, response.text)
        return []

    return response.json().get("faces", [])

def draw_results(image_path, faces):
    img = cv2.imread(image_path)
    for face in faces:
        attrs = face['attributes']
        gender = attrs['gender'].get('value', 'Unknown')
        rect = face['face_rectangle']
        x, y, w, h = rect['left'], rect['top'], rect['width'], rect['height']

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, f"{gender}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Gender Detection Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    print("loading...")
    image_path = choose_image()
    if image_path:
        print("Selected image:", image_path)
        print("loading..")
        faces = detect_gender(image_path)
        if faces:
            print(f"Detected {len(faces)} face(s).")
            for face in faces:
                attrs = face['attributes']
                gender = attrs['gender'].get('value', 'Unknown')
                print("gender: ",gender)

            draw_results(image_path, faces)
        else:
            print("No faces detected.")
    else:
        print("No image selected.")

if __name__ == "__main__":
    main()
