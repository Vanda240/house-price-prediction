import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_house_price_model.pkl")
model_features = joblib.load("model_features.pkl")

st.title("House Price Prediction App")

area = st.number_input("Area", min_value=500, max_value=20000, value=5000)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
stories = st.number_input("Stories", min_value=1, max_value=5, value=2)

mainroad = st.selectbox("Main Road", ["No", "Yes"])
guestroom = st.selectbox("Guest Room", ["No", "Yes"])
basement = st.selectbox("Basement", ["No", "Yes"])
hotwaterheating = st.selectbox("Hot Water Heating", ["No", "Yes"])
airconditioning = st.selectbox("Air Conditioning", ["No", "Yes"])
prefarea = st.selectbox("Preferred Area", ["No", "Yes"])

parking = st.number_input("Parking", min_value=0, max_value=5, value=1)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)

if st.button("Predict Price"):
    input_data = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": 1 if mainroad == "Yes" else 0,
        "guestroom": 1 if guestroom == "Yes" else 0,
        "basement": 1 if basement == "Yes" else 0,
        "hotwaterheating": 1 if hotwaterheating == "Yes" else 0,
        "airconditioning": 1 if airconditioning == "Yes" else 0,
        "parking": parking,
        "prefarea": 1 if prefarea == "Yes" else 0,
        "furnishingstatus_semi-furnished": 1 if furnishingstatus == "semi-furnished" else 0,
        "furnishingstatus_unfurnished": 1 if furnishingstatus == "unfurnished" else 0
    }

    input_df = pd.DataFrame([input_data])
    input_df = input_df[model_features]

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted House Price: {prediction:,.2f}")