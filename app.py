import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("iris.pkl", "rb"))
st.title("🌸 Iris Flower Prediction App")
st.write("Enter the flower measurements below to predict the Iris species.")
sepal_length = st.number_input("Sepal Length (cm)", min_value=4.3, max_value=7.9, step=0.1)
sepal_width  = st.number_input("Sepal Width (cm)", min_value=2.0, max_value=4.4, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=1.0, max_value=6.9, step=0.1)
petal_width  = st.number_input("Petal Width (cm)", min_value=0.1, max_value=2.5, step=0.1)
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    species_dict = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    st.success(f"🌼 Predicted Species: **{species_dict[prediction]}**")