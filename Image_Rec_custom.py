import PIL.Image
import face_recognition
import dlib
import face_recognition_models
import numpy as np
from PIL import Image, ImageFile, ImageDraw
from pkg_resources import resource_filename

predictor_35_point_model = resource_filename(__name__, "custom_predictor.dat")
pose_predictor_35_point = dlib.shape_predictor(predictor_35_point_model)

pose_predictor = pose_predictor_35_point


image = np.array(PIL.Image.open("obama-1080p.jpg"))
face_detector = dlib.get_frontal_face_detector()
face_locations = face_detector(image, 1)

landmarks = [pose_predictor(image, face_location) for face_location in face_locations]

landmarks_as_tuples = [[(p.x, p.y) for p in landmark.parts()] for landmark in landmarks]

face_landmarks_list = [{ 
"chin": points[0:6], 
"left_eyebrow": points[6:9], 
"right_eyebrow": points[9:12],
"nose_bridge": points[12:14],
"nose_tip": points[14:17],
"left_eye": points[17:21], 
"right_eye": points[21:25],
} for points in landmarks_as_tuples]
        
print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:

    for facial_feature in face_landmarks.keys():
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    for facial_feature in face_landmarks.keys():
        d.line(face_landmarks[facial_feature], width=5)

pil_image.show()
