import sys
sys.path.append("..")
import face_alignment
from skimage import io
import numpy as np
import os

import base64
from flask import Flask, request, jsonify


os.environ['KMP_DUPLICATE_LIB_OK']='True'

def decode(base64_string):
    if isinstance(base64_string, bytes):
        base64_string = base64_string.decode("utf-8")

    imgdata = base64.b64decode(base64_string)
    img = io.imread(imgdata, plugin='imageio')
    return img

# application = Flask(__name__)


input = io.imread('Baby_Face.jpg')
img = decode(request.args["img"])
print("Trying to do the stuff")

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, face_detector='sfd', device='cpu')

preds = fa.get_landmarks_from_image(img)
preds = np.asarray(preds).tolist()

jsonify(preds)


# @application.route("/", methods=["GET"])
# def home():
#     img = decode(request.args["img"])
#     print("Trying to do the stuff")

#     fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, face_detector='sfd', device='cpu')

#     preds = fa.get_landmarks_from_image(img)
#     preds = np.asarray(preds).tolist()

#     return jsonify(preds)


# if __name__ == "__main__":
#     application.run(host="0.0.0.0", debug=True, port=8080)


# inputs: image, weight, height, age, ethnicity
# @app.route("/get/<weight>/<height>/<age>/<ethnicity>", methods=["GET"])
# def home(weight, height, age, ethnicity):
