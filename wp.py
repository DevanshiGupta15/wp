import streamlit as st
import pickle
st.title("Weather Prediction App")
pn=st.number_input("Enter prediction")
maxt=st.number_input("Enter Max. temperature")
mint=st.number_input("Enter Min. temperature")
wind=st.number_input("Enter Wind speed")
button=st.button("Predict")

if button:
    lr=pickle.load(open("wp.pkl","rb"))
    res=lr.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"Today weather situation: {res}")