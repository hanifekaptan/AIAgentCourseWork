# Deneyime Dayalı Maaş Tahmini Uygulaması

## Açıklama

Bu proje, basit bir lineer regresyon modeli kullanarak kullanıcının girdiği iş deneyimi yılına göre maaş tahmini yapan interaktif bir web uygulamasıdır.

## Özellikler

-   Önceden eğitilmiş regresyon modelini (`model.pkl`) yükler.
-   İş deneyimi yılı girişi için interaktif sayısal alan.
-   Yüklenen regresyon modelini kullanarak maaş tahmini yapar.
-   Tahmin edilen ücreti kullanıcıya gösterir.

## Dosyalar

- `main.py`: Kullanıcı arayüzünü ve tahmin mantığını çalıştıran ana Streamlit uygulama betiği.
- `model.pkl`: Maaş tahmini için kullanılan kaydedilmiş basit doğrusal regresyon modeli.
- `requirements.txt`: Gerekli Python kütüphanelerini listeler.
- `analysis.ipynb`: Veri analizi, model eğitimi ve `.pkl` dosyalarının kaydedilmesi için kullanılan Jupyter not defteri (çalışma zamanı uygulamasının bir parçası değildir).

## Kurulum

1.  **Depoyu Klonlayın:**
    ```bash
    git clone https://github.com/hanifekaptan/AIAgentCourseWork.git
    cd SimpleLinearRegression
    ```

2.  **Bağımlılıkları Yükleyin:**
    Gerekli kütüphaneleri yüklemek için:
    ```bash
    pip install -r requirements.txt
    ```

## Uygulamayı Çalıştır

1.  Gerekli dosyaların (`main.py`, `model.pkl`, `requirements.txt`) proje dizininde olduğundan emin olun.
2.  Streamlit uygulamasını terminalinizden çalıştırın:
    ```bash
    streamlit run main.py
    ```
3.  Uygulama web tarayıcınızda açılacaktır. Araç özelliklerini girin ve tahmini almak için "Tahmin Et" düğmesine tıklayın.
