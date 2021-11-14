import PIL.Image
import face_recognition
import dlib
import face_recognition_models
import numpy as np
from PIL import Image, ImageFile, ImageDraw

predictor_68_point_model = face_recognition_models.pose_predictor_model_location()
pose_predictor_68_point = dlib.shape_predictor(predictor_68_point_model)

pose_predictor = pose_predictor_68_point


image = np.array(PIL.Image.open("obama.jpg"))
face_detector = dlib.get_frontal_face_detector()
face_locations = face_detector(image, 1)

landmarks = [pose_predictor(image, face_location) for face_location in face_locations]

landmarks_as_tuples = [[(p.x, p.y) for p in landmark.parts()] for landmark in landmarks]

face_landmarks_list = [{ 
"chin": points[0:17], 
"left_eyebrow": points[17:22], 
"right_eyebrow": points[22:27],
"nose_bridge": points[27:31], 
"nose_tip": points[31:36],
"left_eye": points[36:42], 
"right_eye": points[42:48],
"top_lip": points[48:55] + [points[64]] + [points[63]] + [points[62]] + [points[61]] + [points[60]],
"bottom_lip": points[54:60] + [points[48]] + [points[60]] + [points[67]] + [points[66]] + [points[65]] + [points[64]]
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
