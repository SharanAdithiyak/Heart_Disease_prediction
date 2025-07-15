import pickle
import os

from flask import Flask, render_template, request

import numpy as np


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model
model_path = os.path.join(BASE_DIR, 'model', 'model (1).pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Load scaler
scaler_path = os.path.join(BASE_DIR, 'model', 'scaler.pkl')
with open(scaler_path, 'rb') as file1:
    scaler = pickle.load(file1)

imputer_path = os.path.join(BASE_DIR, 'model', 'imputer.pkl')
with open(imputer_path, 'rb') as file2:
    imputer = pickle.load(file2)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:

        features = [float(request.form[f'feature{i}']) for i in range(1, 14)]
        features_array = np.array([features])

        # Apply imputation
        features_imputed = imputer.transform(features_array)

        # Then scale
        features_scaled = scaler.transform(features_imputed)

        # Then predict
        prediction = model.predict(features_scaled)[0]

        result = "Heart Disease Detected 💔" if prediction == 1 else "No Heart Disease ❤️"
        return render_template('result.html', prediction=result)
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
