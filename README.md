Proje Adı

API ile AI model eğitimi

Açıklama

Bu Flask uygulaması, Rastgele Orman sınıflandırıcıyı kullanan bir makine öğrenmesi API'si sunar. Aşağıdakileri yapmanıza izin verir:

Önceden eğitilmiş modelleri yükleme
Yeni veriler üzerinde tahmin yapma (hem tekil örnekler hem de CSV dosyaları)
CSV verilerinden yeni modeller eğitme
Gereksinim duyulanlar

Gerekli kütüphaneleri ve sürümlerini listeleyin:

Flask >=1.0
scikit-learn >=0.24
pandas >=1.0
joblib >=0.12
Kurulum

Gerekli bağımlılıkların nasıl kurulacağını açıklayın:

Bu depoyu kopyalayın veya kodu indirin.
Terminalde proje dizinine gidin.
pip install -r requirements.txt komutunu çalıştırın.
Kullanım

API'yi Çalıştırma:

python app.py komutunu kullanarak API sunucusunu başlatın (ana scriptinizin adı farklıysa app.py yerine onu yazın).
Varsayılan olarak, API http://127.0.0.1:5000/ (localhost portu 5000) üzerinde çalışır. Bunu Flask scriptiniz içindeki app.run çağrısında değiştirebilirsiniz.
API Endpoints (Bağlantı Noktaları):

GET /models: Kullanılabilir önceden eğitilmiş modelleri listeler.
POST /models: Bir önceden eğitilmiş modeli isme göre yükler (istek gövdesinde model_name parametresini sağlayın).
DELETE /models/<model_name>: Yüklenmiş bir modeli kaldırır.
POST /models/<model_name>/predict: Tek bir veri noktası üzerinde tahmin yapar (istek gövdesinde data parametresini JSON nesnesi olarak sağlayın).
POST /models/<model_name>/predict_csv: Bir CSV dosyası üzerinde tahminler yapar (dosyayı multipart form data isteğinde file alanı kullanarak yükleyin).
POST /models/train: Bir CSV dosyasından yeni bir Rastgele Orman modeli eğitir (dosyayı file alanı kullanarak yükleyin ve form data alanlarında model_name ve target_column parametrelerini sağlayın).
