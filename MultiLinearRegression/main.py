import streamlit as st
import pandas as pd
import joblib
import numpy as np

df = pd.read_excel("usedCars.xls")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")
model = joblib.load("model.pkl")
        
st.set_page_config(page_title="İkinci El Araba Fiyat Tahmini", layout="centered")
st.title(":red_car: İkinci El Araba Fiyat Tahmini")

st.markdown("""
Bu uygulama, araba özelliklerine dayalı ikinci el araba fiyat tahmini uygulamasıdır.
Lütfen aşağıdaki özellikleri seçin ve tahmin butonuna tıklayın.
""")

st.divider()

st.subheader("Araba Özelliklerini Giriniz:")
col1, col2 = st.columns(2)

with col1:
    mileage = st.number_input("Kilometre (Mil)", min_value=df["Mileage"].min(), max_value=df["Mileage"].max(), value=50000, step=1000)
    make = st.selectbox("Marka", sorted(df["Make"].unique()))
    carModel = st.selectbox("Model", sorted(df[df["Make"] == make]["Model"].unique()))
    doors = st.selectbox("Kapı Sayısı", sorted(df["Doors"].unique()))
    
with col2:
    cylinder = st.selectbox("Silindir Sayısı", sorted(df["Cylinder"].unique()))
    liter = st.number_input("Motor Hacmi", min_value=df["Liter"].min(), max_value=df["Liter"].max(), value=3.0, step=0.1, format="%.1f")
    trimOptions = df[(df["Make"] == make) & (df["Model"] == carModel)]["Trim"]
    trim = st.selectbox("Donanım Seviyesi", sorted(trimOptions.unique()))
    typeOptions = df[(df["Make"] == make) & (df["Model"] == carModel) & (df["Trim"] == trim)]["Type"]
    carType = st.selectbox("Kasa Tipi", sorted(typeOptions.unique()))
    
st.write(" ")

if st.button("Tahmin Et", use_container_width=True, type="primary"):
    try:
        numericArray = np.array([[mileage, cylinder, liter, doors]])
        categoryArray = np.array([[make, carModel, trim, carType]])

        numericScaled = scaler.transform(numericArray)
        categoryEncoded = encoder.transform(categoryArray)

        input = np.hstack([numericScaled, categoryEncoded])

        prediction = round(model.predict(input)[0], 2)

        st.metric(label="Tahmini Fiyat", value=f"{prediction} ₺")

    except Exception as e:
        st.error(f"Tahmin sırasında bir hata oluştu: {e}")
