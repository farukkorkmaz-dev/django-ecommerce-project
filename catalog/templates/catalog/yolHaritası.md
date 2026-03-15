E-Ticaret Yol Haritası (Phase by Phase)
1. Faz: Temel Yapı ve Ürün Yönetimi (Şu an buradayız)
Bu aşamada dükkanın "mallarını" ve "vitrinini" hallediyoruz.

Kategoriler ve Ürünler: (Yaptık ✅)

Product Detay Sayfası: Bir ürüne tıklayınca onun açıklamasını, stok durumunu ve büyük resmini görmek.

Arama ve Filtreleme: Kategoriye göre veya isme göre ürün bulma.

2. Faz: Kullanıcı (User) Sistemi
Müşteri kim? Bilmemiz lazım.

Kayıt / Giriş (Register/Login): Django'nun hazır User modelini genişleterek profil sayfası ekleyeceğiz.

Adres Yönetimi: Kullanıcının teslimat adreslerini kaydedebilmesi.

3. Faz: Sepet (Cart) Sistemi
İşin en zevkli ve teknik kısmı.

Sepete Ekle/Çıkar: Veritabanında veya "Session" (oturum) bazlı sepet tutma.

Miktar Güncelleme: Sepette ürün adedini artırıp azaltma.

4. Faz: Sipariş (Order) & Ödeme (Payment)
Checkout Sayfası: Sepetteki ürünleri siparişe dönüştürme.

Sipariş Durumu: "Hazırlanıyor", "Kargoya Verildi" gibi statüler.

Mock Ödeme: Gerçek kredi kartı çekiyormuş gibi yapan ama aslında sadece onay veren bir sistem (iYzico gibi sistemlerin simülasyonu).

5. Faz: Sosyal Özellikler & Detaylar
Yorum ve Puan (Review & Rating): Ürünü satın alanların yıldız vermesi.

Favoriler (Wishlist): Sonra alırım dedikleri ürünler.

E-posta Bildirimi: "Siparişiniz alındı" maili.