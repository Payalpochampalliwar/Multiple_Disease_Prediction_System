# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:38:54 2024

@author: sneha
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabeties_model = pickle.load(open('C:/Users/sneha/Downloads/Disease_Project/saved_models/diabetes_model.sav', 'rb'))

stroke_model = pickle.load(open('C:/Users/sneha/Downloads/Disease_Project/saved_models/stroke_model.sav', 'rb'))

heart_model = pickle.load(open('C:/Users/sneha/Downloads/Disease_Project/saved_models/heart_model.sav', 'rb'))

covid_model = pickle.load(open('C:/Users/sneha/Downloads/Disease_Project/saved_models/covid_model.sav', 'rb'))

breastcancer_model = pickle.load(open(r'C:\Users\sneha\Downloads\Disease_Project\saved_models\trained_model.sav', 'rb'))




#sidebar for navigation

with st.sidebar:
    
    select = option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Stroke Prediction',
                          'Heart Disease Prediction',
                          'Covid19 Prediction',
                          'Breast Cancer Prediction'],
                         
                         icons = ['activity', 'thermometer', 'heart', 'droplet', 'person'],

                         
                         default_index = 0)
    
    
#Diabetes Prediction Page
if (select == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose level')
    
    with col3:
        BloodPressure = st.text_input('Bloodpressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin level')
    
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age')
    
    #code for prediction
    diab_dignosis = ''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabeties_model.predict([[Pregnancies, Glucose, BloodPressure,	SkinThickness, Insulin,	BMI, DiabetesPedigreeFunction,	Age	]])
        
        if (diab_prediction[0] == 1):
            diab_daignosis = 'The person is Not Diabetic'
            
        else:
            diab_daignosis = 'The person is Diabetic'
            
    st.success(diab_dignosis)
    
        
if (select == 'Stroke Prediction'):
    
    #page title
    st.title('Stroke Prediction using ML')
        
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
        
    with col1:
        gender = st.text_input('Gender')
            
    with col2:
        age = st.text_input('Age')
        
    with col3:
        hypertension = st.text_input('Hypertension value')
            
    with col1:
        heart_disease = st.text_input('Heart Disease value')
        
    with col2:
        ever_married = st.text_input('Insulin level')
        
    with col3:
        work_type = st.text_input('Work Type')
            
    with col1:
        Residence_type = st.text_input('REsidence Type')
        
    with col2:
        avg_glucose_level = st.text_input('Average Glucose level')
        
    with col3:
        bmi = st.text_input('BMI')
        
    with col1:
        smoking_status = st.text_input('Smoking Status')
        
    #code for prediction
    stroke_dignosis = ''
        
    #creating a button for prediction
        
    if st.button('Stroke Test Result'):
        stroke_prediction = stroke_model.predict([[gender,	age,	hypertension,	heart_disease,	ever_married,	work_type,	Residence_type,	avg_glucose_level,	bmi,	smoking_status	]])
            
        if (stroke_prediction[0] == 0):
            stroke_daignosis = 'The Person does not have a Stroke'
            
        else:
            stroke_daignosis = 'The Person have a Stroke'
                
    st.success(stroke_dignosis)
        
    
if (select == 'Heart Disease Prediction'):
        
        #page title
        st.title('Heart Disease Prediction using ML')
        
        #getting the input data from the user
        #columns for input fields
        col1, col2, col3 = st.columns(3)
            
        with col1:
            age = st.text_input('Age')
                
        with col2:
            sex = st.text_input('Sex')
            
        with col3:
            cp = st.text_input('Chest Pain Type')
                
        with col1:
            trtbps = st.text_input('Resting Blood Pressure')
            
        with col2:
            chol = st.text_input('Serum Cholestrol')
            
        with col3:
            fbs = st.text_input('Fasting Blood Sugar')
                
        with col1:
            restecg = st.text_input('Resting ElectroCardiographic Results')
            
        with col2:
            thalachh = st.text_input('Maximum Heart Rate Achieved')
            
        with col3:
            exng = st.text_input('Exercise Induced Angina')
            
        with col1:
            oldpeak = st.text_input('ST Depression')
            
        with col2:
            slp = st.text_input('Slope of Peak')
            
        with col3:
            caa = st.text_input('Number of Major Vessels')
            
        with col1:
            thall = st.text_input('thal')
        #code for prediction
        heart_dignosis = ''
            
        #creating a button for prediction
            
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_model.predict([[age, sex,	cp,	trtbps,	chol,	fbs,	restecg,	thalachh,	exng,	oldpeak,	slp,	caa,	thall	]])
                
            if (heart_prediction[0] == 0):
                heart_daignosis = 'The Person does not have a Heart Disease'
                
            else:
                heart_daignosis = 'The Person have a Heart Disease'
                    
        st.success(heart_dignosis)
            

if (select == 'Covid19 Prediction'):
    
    #page title
    st.title('Covid19 Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
        
    with col1:
        USMER = st.text_input('Treatment level')
            
    with col2:
        MEDICAL_UNIT = st.text_input('Type of Institution')
        
    with col3:
        SEX = st.text_input('Sex')
            
    with col1:
        PATIENT_TYPE = st.text_input('Type of Patient')
        
    with col2:
        DATE_DIED = st.text_input('Patient Died Date')
        
    with col3:
        INTUBED = st.text_input('Ventilation Connection')
            
    with col1:
        PNEUMONIA = st.text_input('Pneumonia')
        
    with col2:
        AGE = st.text_input('Age')
        
    with col3:
        PREGNANT = st.text_input('Number of Pregnancies')
        
    with col1:
        DIABETES = st.text_input('Diabetes level')
        
    with col2:
        COPD = st.text_input('Chronic Pulmonary')
        
    with col3:
        ASTHMA = st.text_input('Asthma')
        
    with col1:
        INMSUPR = st.text_input('Immunosuppressedk')
    
    with col2:
        HIPERTENSION = st.text_input('Hypertension ')
    
    with col3:
        OTHER_DISEASE = st.text_input('Other disease ')
        
    with col1: 
        CARDIOVASCULAR = st.text_input('Cardiovascular')
                        
    with col2:
        OBESITY = st.text_input('Obese')
        
    with col3:
        RENAL_CHRONIC = st.text_input('Chronic Renal Disease ')
    
    with col1:
        TOBACCO = st.text_input('Tobacco user')

    with col2:
        ICU = st.text_input('ICU')

    #code for prediction
    covid_dignosis = ''
        
    #creating a button for prediction
        
    if st.button('Covid19 Disease Test Result'):
        covid_prediction = covid_model.predict([[USMER,	MEDICAL_UNIT,	SEX,	PATIENT_TYPE,	DATE_DIED,	INTUBED,	PNEUMONIA,	AGE,	PREGNANT,	DIABETES, COPD,	ASTHMA,	INMSUPR,	HIPERTENSION,	OTHER_DISEASE,	CARDIOVASCULAR,	OBESITY,	RENAL_CHRONIC,	TOBACCO,	ICU	]])
            
        if (covid_prediction[0] == 0):
            covid_daignosis = 'Prediction: COVID-19 Positive (Severe).'
            
        else:
            covid_daignosis = 'Prediction: COVID-19 Negative or Mild.'
                
    st.success(covid_dignosis)
    
if (select == 'Breast Cancer Prediction'):
    
    #page title
    st.title('Breast Cancer Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
        
    with col1: 
        mean_radius = st.text_input('Mean Radius Value')
        
    with col2: 
        mean_texture = st.text_input('Mean Texture Value')
    
    with col3: 
        mean_perimeter = st.text_input('Prerimeter mean Value')
    
    with col1: 
        mean_area = st.text_input('Mean Area Value')
    
    with col2: 
        mean_smoothness = st.text_input('Mean Smoothness Value')
    
    with col3:
        mean_compactness = st.text_input('Mean Compactness Value')
   
    with col1:
        mean_concavity = st.text_input('Mean Concavity Value')
    
    with col2: 
        mean_concave_points = st.text_input('Concave points Value')
    
    with col3:
        mean_symmetry = st.text_input('Mean Symmetry Value')
    
    with col1:
        mean_fractal_dimension = st.text_input('Mean Fractal Value')
    
    with col2: 
        radius_se = st.text_input(' Radius Value')
    
    with col3:
        texture_se = st.text_input(' Texture Value')
    
    with col1:
        perimeter_se = st.text_input(' Perimeter Value')
    
    with col2: 
        area_se = st.text_input(' Area Value')
    
    with col3:
        smoothness_se = st.text_input(' Smoothness Value')
    
    with col1:
        compactness_se = st.text_input(' Compactness Value')
    
    with col2:
        concavity_se = st.text_input(' Concavity Value')
    
    with col3:
        concave_points_se = st.text_input(' Concave Points Value')
    
    with col1:
        symmetry_se = st.text_input(' Symmetry Value')
    
    with col2: 
        fractal_dimension_se = st.text_input(' Fractal Dimension Value')
    
    with col3:
        worst_radius = st.text_input('Worst Radius Value')
    
    with col1:
        worst_texture = st.text_input('Worst Texture Value')
    
    with col2: 
        worst_perimeter = st.text_input('Worst Perimeter Value')
    
    with col3: 
        worst_area = st.text_input('Worst area Value')
    
    with col1:
        worst_smoothness = st.text_input('Worst Smoothness Value')
    
    with col2: 
        worst_compactness  = st.text_input('Worst Compactness Value')
    
    with col3:
        worst_concavity = st.text_input('Worst Concavity Value')
    
    with col1:
        worst_concave_points = st.text_input('Concave Points Value')
    
    with col2:
        worst_symmetry = st.text_input('Worst symmetry Value')
    
    with col3:
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension Value')
    
    #code for prediction
    breastcancer_dignosis = ''
        
    #creating a button for prediction
        
    if st.button('Breast cancer Disease Test Result'):
        breastcancer_prediction = breastcancer_model.predict([[float(mean_radius), float(mean_texture), float(mean_perimeter), float(mean_area), float(mean_smoothness),
        float(mean_compactness), float(mean_concavity), float(mean_concave_points), float(mean_symmetry),
        float(mean_fractal_dimension), float(radius_se), float(texture_se), float(perimeter_se), float(area_se),
        float(smoothness_se), float(compactness_se), float(concavity_se), float(concave_points_se),
        float(symmetry_se), float(fractal_dimension_se), float(worst_radius), float(worst_texture),
        float(worst_perimeter), float(worst_area), float(worst_smoothness), float(worst_compactness),
        float(worst_concavity), float(worst_concave_points), float(worst_symmetry), float(worst_fractal_dimension)]])
            
        if (breastcancer_prediction[0] == 0):
            breastcancer_daignosis = 'The Breast Cancer is Malignant'
            
        else:
            breastcancer_daignosis = 'The Breast Cancer is Benign'
                
    st.success(breastcancer_dignosis)





