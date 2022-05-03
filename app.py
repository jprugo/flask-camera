from flask import Flask, request, jsonify
import cv2

app = Flask(__name__)
video = cv2.VideoCapture(0)


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