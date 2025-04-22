# İkinci El Araba Fiyat Tahmini

## Açıklama

Bu proje, kullanıcı tarafından girilen araç özelliklerine dayanarak ikinci el araba fiyatlarını tahmin eden, Streamlit ile oluşturulmuş basit bir web uygulamasıdır.

## Özellikler

-   İkinci el araba bilgilerini içeren `usedCars.xls` veri setini yükler.
-   Önceden eğitilmiş ölçekleyici (`scaler.pkl`), kodlayıcı (`encoder.pkl`) ve regresyon modelini (`model.pkl`) yükler.
-   Araç özelliklerini girmek için Streamlit kullanarak etkileşimli bir kullanıcı arayüzü sunar:
    -   Kilometre (Mileage)
    -   Silindir Sayısı (Cylinder)
    -   Motor Hacmi (Liter)
    -   Kapı Sayısı (Doors)
    -   Marka (Make)
    -   Model
    -   Donanım Seviyesi (Trim)
    -   Kasa Tipi (Type)
-   Yüklenen nesneleri kullanarak veri ön işleme (sayısal özelliklerin ölçeklenmesi, kategorik özelliklerin one-hot kodlanması) yapar.
-   Yüklenen regresyon modelini (Lasso Regresyon) kullanarak araba fiyatını tahmin eder.
-   Tahmin edilen fiyatı kullanıcıya gösterir.

## Dosyalar

-   `main.py`: Kullanıcı arayüzünü ve tahmin mantığını çalıştıran ana Streamlit uygulama betiği.
-   `usedCars.xls`: Seçim kutularını doldurmak için kullanılan (ve model eğitiminde kullanılmış olan) ikinci el araba bilgilerini içeren veri seti.
-   `scaler.pkl`: Sayısal özellikleri ölçeklemek için kullanılan kaydedilmiş Scikit-learn `StandardScaler` nesnesi.
-   `encoder.pkl`: Kategorik özellikleri kodlamak için kullanılan kaydedilmiş Scikit-learn `OneHotEncoder` nesnesi.
-   `model.pkl`: Fiyat tahmini için kullanılan kaydedilmiş Scikit-learn regresyon modeli (Lasso Regresyon).
-   `requirements.txt`: Gerekli Python kütüphanelerini listeler.
-   `analysis.ipynb`: Veri analizi, model eğitimi ve `.pkl` dosyalarının kaydedilmesi için kullanılan Jupyter not defteri (çalışma zamanı uygulamasının bir parçası değildir).

## Kurulum

1.  **Depoyu klonlayın:**
    ```bash
    git clone https://github.com/hanifekaptan/AIAgentCourseWork.git
    cd MultiLinearRegression
    ```

2.  **Bağımlılıkları yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

## Uygulamayı Çalıştır

1.  Gerekli dosyaların (`main.py`, `usedCars.xls`, `scaler.pkl`, `encoder.pkl`, `model.pkl`, `requirements.txt`) proje dizininde olduğundan emin olun.
2.  Streamlit uygulamasını terminalinizden çalıştırın:
    ```bash
    streamlit run main.py
    ```
3.  Uygulama web tarayıcınızda açılacaktır. Araç özelliklerini girin ve tahmini almak için "Tahmin Et" düğmesine tıklayın.


