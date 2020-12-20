import numpy as np
import face_recognition
import joblib
import os


WEIGHT_MODEL = joblib.load('model/weight_predictor.model')
HEIGHT_MODEL = joblib.load('model/height_predictor.model')


def get_face_encoding(image_path):
    image = face_recognition.load_image_file(image_path)
    my_face_encoding = face_recognition.face_encodings(image)
    if not my_face_encoding:
        raise ValueError("no face found")
    return my_face_encoding[0].tolist()


def predict_height_weight_BMI(input_image):
    try:
        face_enc = get_face_encoding(input_image)
        input_array = np.expand_dims(
            np.array(face_enc),
            axis=0
        )
        height = np.exp(HEIGHT_MODEL.predict(input_array)).item()
        weight = np.exp(WEIGHT_MODEL.predict(input_array)).item()
        bmi = weight / (height ** 2)
        category = get_category(bmi)
        return {
            'height': height,
            'weight': weight,
            'bmi': bmi,
            'category': category
        }
    except ValueError as e:
        raise ValueError(e)
    except Exception as ex:
        raise Exception(ex)


def get_category(bmi):
    if (bmi < 18.5):
        return "Underweight"
    elif (bmi < 24.9):
        return "Normal"
    elif (bmi < 29.9):
        return "Overweight"
    else:
        return "Obese"
