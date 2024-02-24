import joblib

def load_model():
    model_path = 'Store\models\model1.joblib'
    model = joblib.load(model_path)
    return model