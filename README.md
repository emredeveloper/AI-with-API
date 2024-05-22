Proje Adı

Burayı projenizin ismiyle değiştirin.

Açıklama

Bu Flask uygulaması, Rastgele Orman sınıflandırıcıyı kullanan bir makine öğrenmesi API'si sunar. Aşağıdakileri yapmanıza izin verir:

Önceden eğitilmiş modelleri yükleme
Yeni veriler üzerinde tahmin yapma (hem tekil örnekler hem de CSV dosyaları)
CSV verilerinden yeni modeller eğitme
Gereksinim duyulanlar

Gerekli kütüphaneleri ve sürümlerini listeleyin:

Flask
scikit-learn
pandas
joblib
Kurulum

Gerekli bağımlılıkların nasıl kurulacağını açıklayın:

Bu depoyu kopyalayın veya kodu indirin.
Terminalde proje dizinine gidin.
pip install -r requirements.txt komutunu çalıştırın (eğer bir requirements.txt dosyanız varsa ve bağımlılıklar listeleniyorsa).
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
Örnek Kullanım:

API ile curl veya Postman gibi araçlar kullanarak nasıl etkileşim kurabileceğinize dair bazı örnekler:

Modelleri Listeleme:

Bash
curl http://localhost:5000/models
Kodu dikkatli kullanın.
content_copy
Model Yükleme:

Bash
curl -X POST http://localhost:5000/models -H "Content-Type: application/json" -d '{"model_name": "benim_modelim"}'
Kodu dikkatli kullanın.
content_copy
Tahmin Yapma:

Bash
curl -X POST http://localhost:5000/models/benim_modelim/predict -H "Content-Type: application/json" -d '{"data": {"özellik1": 1.2, "özellik2": 3.4}}'
Kodu dikkatli kullanın.
content_copy
CSV'den Tahmin Yapma:

Verilerinizi içeren bir CSV dosyası hazırlayın.
Postman gibi bir araç kullanarak http://localhost:5000/models/benim_modelim/predict_csv adresine bir POST isteği gönderin.
file alanında CSV dosyasını seçin.
Yeni Model Eğitme:

Eğitim verilerinizi içeren bir CSV dosyası hazırlayın (hedef sütun dahil).
Postman kullanarak http://localhost:5000/models/train adresine bir POST isteği gönderin.
file alanında CSV dosyasını seçin.
İstenen model adını (örneğin, yeni_model) form data alanındaki model_name parametresinde sağlayın.
Hedef sütun adını (örneğin, hedef) form data alanındaki target_column parametresinde belirtin.
