from flask import Flask, render_template, request
import joblib  # Use joblib instead of pickle
import numpy as np

app = Flask(__name__)

# Load the model from the pickle file
model = joblib.load('model1.pkl')  # Use joblib.load() to load the saved model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form inputs from the user
    age = int(request.form['age'])
    sex = int(request.form['sex'])  # 1 for male, 0 for female
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = int(request.form['smoker'])  # 1 for smoker, 0 for non-smoker
    region = int(request.form['region'])  # Region encoded as an integer

    # Prepare the input array
    input_features = np.array([[age, sex, bmi, children, smoker, region]])

    # Get the prediction from the model
    prediction = model.predict(input_features)

    # Return the result as an HTML response
    return f"Predicted medical expenses: {prediction[0]:.2f} INR"

if __name__ == '__main__':
    app.run(debug=True)
