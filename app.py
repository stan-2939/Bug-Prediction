import numpy as np
import streamlit as st
import pandas as pd
import pickle
from collections import Counter
import model
from PIL import Image

image = Image.open('bugimage.jpg')




feature_col=pickle.load(open("features.sav",'rb'))

nav = st.sidebar.radio("Navigation",["Home","Prediction","Working"])
if nav=="Home":
    st.title("Predict The Bugs In Your Code")
    st.image(image)
    st.write("Bug Prediction and Identification is a key activity for software maintenance. This website uses machine learning models to assess code, making use of it's ability to learn from large number of parameters (features) and faster decision making. You just need to fill in the parameters and the website will predict whether your code has a bug with 98.5% accuracy.")

def predict():
    row = np.array([a,b,c,d,e,f,g,h,i,j,k,l])
    X_in=pd.DataFrame([row])
    prediction_res=model.predict(X_in)
    st.write(prediction_res)
    if prediction_res==0:
       st.success("There is no bug in the code")
    if prediction_res==1:
       st.error("There is bug in the code")
        
if nav=="Prediction":
    st.title("Enter The Parameters")
    ca,cb,cc=st.columns(3)
    a=ca.number_input("Enter loc")
    b=cb.number_input("Enter n")
    c=cc.number_input("Enter v")
    cd,ce,cf=st.columns(3)
    d=cd.number_input("Enter d")
    e=ce.number_input("Enter i")
    f=cf.number_input("Enter lOCode")
    cg,ch,ci=st.columns(3)
    g=cg.number_input("Enter lOComment")
    h=ch.number_input("Enter uniq_Op")
    i=ci.number_input("Enter uniq_Opnd")
    cj,ck,cl=st.columns(3)
    j=cj.number_input("Enter total_Op")
    k=ck.number_input("Enter total_Opnd")
    l=cl.number_input("Enter branchCount")
    st.button("predict",on_click=predict)

if nav=="Working":
    st.title("This is how the model actually works")
    st.write("The machine learning models deployed after vigorous training and testing phases provide the output prediction as of whether the code you've written contains a bug or not.")
    st.write("")
    st.write("The model we have used here is ExtraTrees Classifier and the accuracy of the model is 98.5%")
    st.write("")














