import streamlit as st
import pandas as pd
import numpy as np
import joblib
from utils.constants import CAR_MAKES, CAR_MODELS, CAR_BODIES, CAR_TRIMS


# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load('models/estimate_veh_price.joblib')


veh_estim_model = load_model()



st.title("Price My Ride")
st.write("Tool which helps you estimate vehicle value (Data is from 2015)")


st.divider()

st.header("Provide Vehicle Data")

col1, col2, col3= st.columns(3)

with col1:
    make = st.selectbox("Make", CAR_MAKES, index=None)
    odometer = st.number_input("Mileage", min_value=0)

with col2:
    model = st.selectbox("Model", CAR_MODELS, index=None)
    body = st.selectbox("Body type", CAR_BODIES, index=None)

with col3:
    year = st.number_input("Year", min_value=1981, max_value=2015)
    trim = st.selectbox("Trim (optional)", CAR_TRIMS, index=None)

st.divider()

if st.button("Estimate value", type = "primary", use_container_width=True):
   if not make or not model or not body:
        st.error("Please fill in all fields before estimating.")
   else:
        if not trim:
             trim = "base"
        input_data = pd.DataFrame({
            "make": [make.lower().replace(" ", "")],
            "model": [model.lower().replace(" ", "")],
            "trim": [trim.lower().replace(" ", "")],
            "body": [body.lower().replace(" ", "")],
            "year": [year],
            "odometer": [odometer]
        })
   try:

            prediction = veh_estim_model.predict(input_data)
            
            # Display result formatted as currency
            st.success(f"Estimated Price: ${prediction[0]:,.2f}")
            
   except Exception as e:
            print(f"Error making prediction: {e}")

st.write("JUST TESTING AUTOMATION 3")






