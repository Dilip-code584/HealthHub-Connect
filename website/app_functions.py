import pickle
import numpy as np
from sklearn.exceptions import InconsistentVersionWarning
import warnings
from sklearn.utils.validation import check_is_fitted

# Your existing imports remain unchanged

def get_model(path):
    model = load_model(path, compile=False)
    return model

def pred(path):
    data = load_img(path, target_size=(224, 224, 3))
    data = np.asarray(data).reshape((-1, 224, 224, 3))
    data = data * 1.0 / 255
    predicted = np.round(get_model('./website/app_models/pneumonia_model.h5').predict(data)[0])[0]
    return predicted

def ValuePredictor(to_predict_list):
    if len(to_predict_list) == 15:
        page = 'kidney'
        with open('./website/app_models/kidney_model.pkl', 'rb') as f:
            with warnings.catch_warnings():
                warnings.filterwarnings("error", category=InconsistentVersionWarning)
                try:
                    kidney_model = pickle.load(f)
                    check_is_fitted(kidney_model)  # Optional: Validate the model
                except InconsistentVersionWarning as w:
                    print(w)
                    # Handle the warning as per your requirements
        pred = kidney_model.predict(np.array(to_predict_list).reshape(-1, len(to_predict_list)))
    elif len(to_predict_list) == 10:
        page = 'liver'
        with open('./website/app_models/liver_model.pkl', 'rb') as f:
            liver_model = pickle.load(f)
        pred = liver_model.predict(np.array(to_predict_list).reshape(-1, len(to_predict_list)))
    elif len(to_predict_list) == 11:
        page = 'heart'
        with open('./website/app_models/heart_model.pkl', 'rb') as f:
            heart_model = pickle.load(f)
        pred = heart_model.predict(np.array(to_predict_list).reshape(-1, len(to_predict_list)))
    elif len(to_predict_list) == 9:
        page = 'stroke'
        with open('./website/app_models/avc_scaler.pkl', 'rb') as f:
            stroke_scaler = pickle.load(f)
        l1 = np.array(to_predict_list[2:]).reshape((-1, len(to_predict_list[2:]))).tolist()[0]
        l2 = stroke_scaler.transform(np.array(to_predict_list[0:2]).reshape((-1, 2))).tolist()[0]
        l = l2 + l1
        with open('./website/app_models/avc_model.pkl', 'rb') as f:
            stroke_model = pickle.load(f)
        pred = stroke_model.predict(np.array(l).reshape(-1, len(l)))
    elif len(to_predict_list) == 8:
        page = 'diabete'
        with open('./website/app_models/diabete_model.pkl', 'rb') as f:
            diabete_model = pickle.load(f)
        pred = diabete_model.predict(np.array(to_predict_list).reshape((-1, 8)))
        print(pred[0], page)
    return pred[0], page
