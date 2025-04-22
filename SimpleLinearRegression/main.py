import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.set_page_config(page_title="Deneyime Dayalı Maaş Tahmini", layout="centered")

st.title("Deneyime Dayalı Maaş Tahmini")

st.markdown("""
Bu proje, basit lineer regresyon algoritması kullanılarak geliştirilmiş bir maaş tahmin uygulamasıdır.
Kullanıcıdan alınan iş deneyimi yılı bilgisine göre model bir maaş tahmini yapar.
"""
)

years = st.number_input(
    "Deneyim Yılı:", min_value=0.0, max_value=50.0, value=5.0, step=0.1
)

if st.button("Tahmin Et"):
    try:
        prediction = round(model.predict(np.array([[years]]))[0], 2)
        st.metric(label="Tahmin Edilen Maaş:", value=f"{prediction} ₺")
    except Exception as e:
        st.error(f"Tahmin sırasında bir hata oluştu: {e}")

