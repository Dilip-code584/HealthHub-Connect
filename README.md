-Access-Platform# Health-Access-Platform
Health Hub Using AI
I have predicted here in the video only for one disease,but we can do the same for all...
By harnessing the power of artificial intelligence, our innovative project is dedicated to transforming the realm of healthcare. Through the utilization of advanced predictive models, we aim to forecast the probability of developing critical conditions such as stroke, liver disease, heart ailments, diabetes, and pneumonia. Our system leverages the latest trends and comprehensive patient data to offer precise and reliable insights, enabling early identification and proactive management of potential health risks. With a focus on preventive care, our AI-driven solution endeavors to empower individuals and healthcare providers with valuable information, fostering a proactive approach to health maintenance and disease prevention. Embracing the potential of AI, we are committed to revolutionizing healthcare by delivering personalized and data-driven predictions, ultimately contributing to improved patient outcomes and a healthier society.

Machine learning (ML) in healthcare has emerged as a game-changing force, revolutionizing diagnosis, treatment, and patient care. Its ability to analyze vast datasets has paved the way for personalized medicine and predictive analytics, enhancing treatment outcomes and patient satisfaction. ML algorithms are being employed to interpret medical images, predict disease progression, and optimize treatment plans, driving precision medicine and tailored interventions. The integration of ML with wearable devices and remote monitoring has facilitated continuous health tracking and early intervention, empowering individuals to actively manage their health. Furthermore, the trend towards explainable AI and ethical considerations in healthcare ML is shaping a transparent and responsible approach to leveraging these technologies for the benefit of patients, healthcare providers, and society as a whole.


In my application AltairCare i have used machine learning and deep learning algorithms to train highly accurate models and thus allowing users to check their chance of having one of the following diseases:

    Liver Disease
    Pneumonia Disease
    Kidney Disease
    Diabete Disease
    Stroke Disease
    Heart Disease

Prediction Page-
![Screenshot from 2024-03-10 00-22-48](https://github.com/Dilip-code584/HealthHub-Connect/assets/128896508/d9860799-d502-40d7-9d84-280cc511df75)


Each Disease have it's own page with an overview and symptoms that patient may have, and also the prediction model information and required parameters that user must provide
Disease Page-
![Screenshot from 2024-03-10 00-19-21](https://github.com/Dilip-code584/HealthHub-Connect/assets/128896508/3d95c653-ac83-4bd6-9fc0-b7f20041f49f)

All the datasets used to train the models can be found in the Kaggle website
Libraries Used :

    Flask: for backend web development
    Scikit-learn & tensorflow: for training the diseases prediction models
    sqlalchemy: library for handling sqlite database

 How to run this project :
Clone this repository:

git clone https://github.com/Dilip-code584/HealthHub-Connect.git 
cd Healthcare-AI-WebApp

Install requirements (using a virtual environment is preferable):

pip install -r requirements.txt

Run this command to start local server:

python3 app.py

