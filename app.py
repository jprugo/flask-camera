from flask import Flask, request, jsonify
from cv2 import cv2

app = Flask(__name__)

from sys import platform
if platform == "linux" or platform == "linux2" or platform == "darwin":
    # Linux and Mac
    video = cv2.VideoCapture(0)
elif platform == "win32":
    # Windows...
    video = cv2.VideoCapture(0, cv2.CAP_DSHOW)




@app.route('/takepicture', methods = ['POST'])
def takeimage():
    id = request.form['id']
    path = f'{id}.jpg'
    _, frame = video.read()
    cv2.imwrite(path, frame)
    return jsonify({
        "imagePath": path,
    }), 201

if __name__ == '__main__':
    app.run()
    app.debug = True
