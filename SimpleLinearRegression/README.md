# Maaş Tahmini

Önceden eğitilmiş bir model kullanarak iş deneyimi yılına göre maaş tahmini yapan basit bir FastAPI uygulamasıdır.

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

FastAPI sunucusunu Uvicorn ile başlatın:

```bash
uvicorn main:app --reload
```

Uygulama `http://127.0.0.1:8000` adresinde çalışacaktır.

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
