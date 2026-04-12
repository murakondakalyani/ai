import joblib

model = joblib.load("models/model.pkl")

def predict_severity(traffic):
    mapping = {'low':1, 'medium':2, 'high':3}
    val = mapping[traffic]
    return int(model.predict([[val]])[0])