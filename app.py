import streamlit as st
import pandas as pd
import pickle

# App title and description
st.title("🏡 Housing Prices Prediction")

st.write("""
### Project Description
We trained a KNN model to predict house prices based on:
- Lot Area
- Basement Square Feet
- Number of Bedrooms
- Garage Capacity
""")

# Load the model once
with open("trained_pipe_knn.sav", 'rb') as f:
    model = pickle.load(f)

# User input
LotArea = st.number_input("Lot Area (sq ft)", min_value=0)
TotalBsmtSF = st.number_input("Basement Area (sq ft)", min_value=0)
BedroomAbvGr = st.number_input("Number of Bedrooms", min_value=0)
GarageCars = st.number_input("Garage Capacity (cars)", min_value=0)

# Predict button
if st.button("Predict House Price"):
    new_data = pd.DataFrame({
        'LotArea': [LotArea],
        'TotalBsmtSF': [TotalBsmtSF],
        'BedroomAbvGr': [BedroomAbvGr],
        'GarageCars': [GarageCars]
    })

    prediction = model.predict(new_data)
    st.success(f"🏠 Estimated House Price: ${prediction[0]:,.2f}")
