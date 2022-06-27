from json import dumps
from flask import Flask, request, Response
from cv2 import cv2
from pathlib import Path

app = Flask(__name__)

video = cv2.VideoCapture(0)

basePath = str(Path(__file__).parent.resolve()).replace('\\' , '/')

@app.route('/takepicture', methods = ['POST'], )
def takeimage():
    # The id received by the client
    id = request.form['id']
    path = f'{id}.jpg'
    _, frame = video.read()
    cv2.imwrite(path, frame)
    
    return Response(dumps({
        "imagePath": f"{basePath}/{path}",
    }), mimetype='application/json;  charset=utf-8', status=201)
    

if __name__ == '__main__':
    app.run(port=3000)
    app.debug = True
