Overview
This project is a Medical Expense Prediction Web Application built using Flask, HTML, CSS, and JavaScript for the frontend, and scikit-learn for the machine learning model. The app predicts a person’s medical expenses based on several input features like age, BMI, smoking habits, and more. The model is deployed in a Flask application, with an attractive and user-friendly interface, making it accessible for end users to predict their expected medical costs.

Features
Input Features:
Age
Body Mass Index (BMI)
Number of children
Smoking status (yes/no)
Region of residence
Prediction: Provides estimated medical expenses based on the input features using a trained machine learning model.
User Interface: Built using HTML, CSS, and JavaScript to ensure an intuitive and visually appealing user experience.
Machine Learning Model: Uses a Linear Regression model trained on a healthcare dataset to predict medical expenses.
Technologies Used
Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript
Machine Learning: Scikit-learn
Model Persistence: Pickle
How It Works
The user inputs their details (age, BMI, children, smoking habits, region) into the web form.
These inputs are sent to the Flask backend, where they are processed.
The trained machine learning model predicts the user's expected medical expenses based on the input features.
The result is displayed on the frontend in INR (Indian Rupees).
