import streamlit as st
import pandas as pd

# Load sample data for symptoms and drugs
SYMPTOM_DISEASE_DATA = {
    "fever": ["Viral Fever", "Malaria", "Dengue"],
    "cough": ["Common Cold", "Flu", "Tuberculosis"],
    "headache": ["Migraine", "Tension Headache", "Sinusitis"],
}

DRUG_INFO_DATA = {
    "paracetamol": {"use": "Reduces fever and pain", "warnings": "Avoid overdose; max 4g/day"},
    "ibuprofen": {"use": "Reduces inflammation and pain", "warnings": "Take after food; not for ulcers"},
    "amoxicillin": {"use": "Antibiotic for bacterial infections", "warnings": "Do not take without prescription"},
}

# Step 3: Streamlit App Layout
st.title("MediGuide AI")
st.subheader("Empowering Safe Medical Decisions")
st.write("**Disclaimer:** This app provides general information and is not a substitute for professional medical advice.")

# Step 4: Symptom Checker Section
st.header("1. Symptom Checker")
selected_symptoms = st.multiselect("Select your symptoms:", SYMPTOM_DISEASE_DATA.keys())

if st.button("Check Possible Conditions"):
    if selected_symptoms:
        results = []
        for symptom in selected_symptoms:
            results.extend(SYMPTOM_DISEASE_DATA.get(symptom, []))
        st.write("### Possible Conditions:")
        st.write(", ".join(set(results)))
        st.warning("Consult a doctor if symptoms persist.")
    else:
        st.error("Please select at least one symptom.")

# Step 5: Drug Safety Advisor Section
st.header("2. Drug Safety Advisor")
drug_name = st.text_input("Enter a drug name:")

if st.button("Check Drug Info"):
    drug_info = DRUG_INFO_DATA.get(drug_name.lower())
    if drug_info:
        st.write(f"**Use:** {drug_info['use']}")
        st.write(f"**Warnings:** {drug_info['warnings']}")
    else:
        st.error("Drug not found in our database. Please consult a doctor.")

# Step 6: Health Tips Section
st.header("3. Health Tips")
st.write("### General Health Tips:")
st.markdown(
    """
    - Avoid self-medicating without proper consultation.
    - Drink plenty of water and stay hydrated.
    - Wash your hands regularly to prevent infections.
    - Ensure proper sleep and exercise daily.
    """
)
