# API ile AI Model Eğitimi 

## Proje Genel Bakış

Bu Flask web uygulaması, Rastgele Orman sınıflandırıcıyı kullanarak güçlü bir makine öğrenmesi API'si oluşturur. Uygulama, önceden eğitilmiş modeller yüklemenize, yeni veriler üzerinde tahminler yapmanıza ve hatta CSV verilerinden yeni modeller eğitmenize olanak tanır.

## Başlarken

### Gereksinimler

- Flask >=1.0
- scikit-learn >=0.24
- pandas >=1.0
- joblib >=0.12

### Kurulum

Başlamak için basit adımları izleyin:

1. Bu depoyu kopyalayın veya kodunu indirin.
2. Terminalinizi kullanarak proje dizinine gidin.
3. Gerekli bağımlılıkları yüklemek için `pip install -r requirements.txt` komutunu çalıştırın.

### Kullanım

#### API'yi Çalıştırma

API sunucusunu başlatmak için basitçe `python app.py` komutunu çalıştırın (ana scriptinizin adı farklıysa `app.py` yerine onu kullanın). Varsayılan olarak, API `http://127.0.0.1:5000/` (localhost portu 5000) üzerinde çalışacaktır. Farklı bir adres tercih ederseniz, bunu Flask scriptinizdeki `app.run` çağrısında kolayca değiştirebilirsiniz.

#### API Uç Noktaları

Uygulama, çeşitli görevleri gerçekleştirmek için kullanabileceğiniz birkaç uç nokta sunar:

- **GET /models**: Kullanıma hazır önceden eğitilmiş modellerin listesini alın.
- **POST /models**: Bir önceden eğitilmiş modeli yükleyin. İstek gövdesinde `model_name` parametresini sağlayın.
- **DELETE /models/\<model_name\>**: Belirtilen önceden eğitilmiş modeli kaldırın.
- **POST /models/\<model_name\>/predict**: Tek bir veri noktası üzerinde tahmin yapın. İstek gövdesinde JSON nesnesi olarak `data` parametresini sağlayın.
- **POST /models/\<model_name\>/predict_csv**: Bir CSV dosyası üzerinde toplu tahminler yapın. Dosyayı multipart form verileri aracılığıyla `file` alanı ile yükleyin.
- **POST /models/train**: Yeni bir Rastgele Orman modeli eğitin. CSV dosyasını `file` alanı ile yükleyin ve form verileri aracılığıyla `model_name` ve `target_column` parametrelerini belirtin.

## Özellikler ve Gelecek Geliştirmeler

Bu uygulama, makine öğrenmesi modellerini kolayca dağıtmanıza ve kullanmanıza olanak tanır. Gelecekteki geliştirmeler, farklı türde modellerin desteklenmesini, daha gelişmiş eğitim seçeneklerini ve API'nin performansını ve ölçeklenebilirliğini iyileştirmeyi içerebilir.

Katkılar ve geri bildirimler memnuniyetle karşılanır! Lütfen bu projeye katkıda bulunmak veya herhangi bir sorunuz veya öneriniz varsa bizimle iletişime geçmek için çekinmeyin.
