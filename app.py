import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("pmsm_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("PMSM Motor Speed Prediction")
st.write("Enter the input values to predict the motor speed.")

# Define input fields
ambient = st.number_input("Ambient Temperature", value=0.0)
coolant = st.number_input("Coolant Temperature", value=0.0)
u_d = st.number_input("Voltage d-axis (u_d)", value=0.0)
u_q = st.number_input("Voltage q-axis (u_q)", value=0.0)
torque = st.number_input("Torque", value=0.0)
i_d = st.number_input("Current d-axis (i_d)", value=0.0)
i_q = st.number_input("Current q-axis (i_q)", value=0.0)
pm = st.number_input("Permanent Magnet Temperature", value=0.0)
stator_yoke = st.number_input("Stator Yoke Temperature", value=0.0)
stator_tooth = st.number_input("Stator Tooth Temperature", value=0.0)
stator_winding = st.number_input("Stator Winding Temperature", value=0.0)
profile_id = st.number_input("Profile ID", value=0)  # Added missing feature

# Predict button
if st.button("Predict Motor Speed"):
    input_features = np.array([[ambient, coolant, u_d, u_q, torque, i_d, i_q, pm, stator_yoke, stator_tooth, stator_winding, profile_id]])
    prediction = model.predict(input_features)[0]  # Get the predicted value
    st.success(f"Predicted Motor Speed: {prediction:.2f} RPM")
