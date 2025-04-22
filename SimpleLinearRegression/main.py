import streamlit as st
import requests
import os

os.system("uvicorn api:app --reload")

st.set_page_config(page_title="Maaş Tahmin Uygulaması", layout="centered")

st.title("Maaş Tahmin Uygulaması")

st.markdown("""
Bu proje, basit lineer regresyon algoritması kullanılarak geliştirilmiş bir maaş tahmin uygulamasıdır.
Kullanıcıdan alınan iş deneyimi yılı bilgisine göre model bir maaş tahmini yapar ve FastAPI üzerinden JSON formatında yanıt döndürür.
Bu arayüz ise FastAPI endpoint'ine istek göndererek tahmin sonucunu interaktif şekilde gösterir.
"""
)

years = st.number_input(
    "Deneyim Yılı:", min_value=0.0, max_value=50.0, value=5.0, step=0.1
)

if st.button("Tahmin Et"):
    try:
        payload = {"YearsExperience": years}
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        response.raise_for_status()
        data = response.json()
        prediction = data.get("prediction")
        if prediction is not None:
            st.success(f"Tahmin Edilen Maaş: {prediction:,.2f} ₺")
        else:
            st.error("Beklenmeyen yanıt formatı.")
    except requests.exceptions.RequestException as e:
        st.error(f"API isteğinde hata oluştu: {e}")
    except Exception as e:
        st.error(f"Beklenmeyen bir hata: {e}")

st.write("\n---\n")
st.write("*Not:*\nFastAPI uygulamanızı `uvicorn api:app --reload` komutuyla çalıştırmayı unutmayın ve ardından bu sayfayı `streamlit run main.py` ile başlatın.")

