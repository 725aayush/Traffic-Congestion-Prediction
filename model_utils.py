import joblib
from utils.preprocess import preprocess_input

# Load the trained model
model = joblib.load('model/model.pkl')

def predict_traffic(data):
    processed = preprocess_input(data)
    prediction = model.predict(processed)
    return {"predicted_vehicles": int(prediction[0])}
