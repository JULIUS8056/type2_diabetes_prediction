#from catboost import CatBoostClassifierst
import numpy as np
import pickle
import streamlit as st
model=pickle.load(open('C:/Users/Julius/Downloads/MODEL FILES/Type-2-diabetes-prediction.pk1','rb'))

def main():
    #title of the app
    st.title("Clinical Decision Support System for Prediction of Type 2 Diabetes")
    #input setup
    fbs=st.text_input("Blood Sugar level ")
    bmi=st.text_input("Body Mass Index")
    waist=st.text_input("Waist Circumference")
    age=st.text_input("Age")
    gender=st.text_input("Gender","M/F ?")
    fhd=st.text_input("Family History of Diabetes","Y/N ?")
    fhh=st.text_input("Family History of Hypertension","Y/N ?")
    heu=st.text_input("History of Excess Urine","Y/N ?")
    hew=st.text_input("History of Excess Water Intake","Y/N ?")
    rex=st.text_input("Did you do excercise regularly","Y/N ?")
    hef=st.text_input("History of Excess Food Intake","Y/N ?")
    phd=st.text_input("Did you have other type of diabetes before","Y/N ?")
    #action button
    if st.button("Predict"):
        makeprediction=model.predict([[fbs,bmi,waist,age,gender,fhd,fhh,heu,hew,rex,hef,phd]])
    #display of result
    st.success("Your result shows that you {}".format(makeprediction))
   
if __name__=='__main__':
    main()
