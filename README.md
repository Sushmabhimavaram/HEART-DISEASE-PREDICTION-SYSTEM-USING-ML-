# HEART-DISEASE-PREDICTION-SYSTEM-USING-ML-


The integration of Machine Learning (ML) in healthcare is revolutionizing how medical
diagnoses are approached, offering rapid, data-driven insights that can assist both practitioners
and patients. This project, titled Heart Disease Prediction Using ML, is designed to predict
diseases—currently focused on heart disease—by analyzing patient information through trained
ML algorithms. The goal is to provide an accessible, web-based platform that empowers users
to assess potential health risks with minimal effort, using a user-friendly interface and reliable
backend prediction models.
The system employs a supervised learning model, specifically a Random Forest Classifier,
trained on a well-structured dataset containing various clinical features. These features include
patient metrics such as age, blood pressure, cholesterol levels, and other diagnostic attributes.
Once input data is submitted by the user, the application processes it and returns a prediction
indicating whether the user is likely to have a heart condition. This form of early warning system
can be crucial in prompting users to seek professional medical advice before a condition
worsens.
A Flask-based web framework powers the application’s interface, allowing users to interact
with the system through a simple form submission process. The project also incorporates a
feedback system, enabling users to rate their experience and submit comments. These feedback
entries are stored in a local SQLite database, which supports further improvements and
customization of the platform. Security considerations are taken into account to manage
feedback deletion, accessible only with admin-level credentials.
While the system is currently limited to heart disease prediction, it is structured to support
scalability and modular growth.This project not only showcases the potential of machine
learning in real-world healthcare applications but also emphasizes the importance of accessible
and preventive healthcare technologies. Through continuous development and feedback-based enhancements, the platform holds promise as a valuable tool in modern telemedicine.
