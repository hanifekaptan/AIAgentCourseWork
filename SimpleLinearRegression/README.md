# Maaş Tahmin Projesi

Bu proje, basit lineer regresyon algoritması kullanılarak geliştirilmiş bir maaş tahmin uygulamasıdır. Kullanıcıdan alınan iş deneyimi yılı bilgisine göre model bir maaş tahmini yapar ve FastAPI üzerinden JSON formatında yanıt döndürür. Arayüz ise FastAPI endpoint'ine istek göndererek tahmin sonucunu interaktif şekilde gösterir.


## Gereksinimler

- Python 3.7+
- `requirements.txt` dosyasında belirtilen bağımlılıklar
- Proje kökünde `model.pkl` dosyasının bulunması

## Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/hanifekaptan/AIAgentCourseWork.git
   cd AIAgentCourseWork/SimpleLinearRegression
   ```
2. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
3. `model.pkl` dosyasının proje kökünde olduğundan emin olun.

## Uygulamayı Çalıştırma

```bash
streamlit run main.py
```

Bu komut, arayüze ihtiyaç duyacağınız FastAPI sunucusunu (`uvicorn api:app --reload`) ve Streamlit arayüzünü aynı anda başlatır.

Uygulama ve arayüz `http://localhost:8501` adresinde çalışacaktır.

## API Dokümantasyonu

Swagger UI'a şu adresten ulaşabilirsiniz:

```
http://127.0.0.1:8000/docs
```

## Tahmin Uç Noktası

- **URL**: `/predict`
- **Metot**: `POST`
- **İstek Gövdesi**:
  ```json
  {
    "YearsExperience": 5.0
  }
  ```
- **Yanıt**:
  ```json
  {
    "prediction": 70000.0
  }
  ```

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. 
