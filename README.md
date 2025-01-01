# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini merupakan tugas akhir dalam program Dicoding Data Science. Tujuannya adalah untuk menganalisis dataset penyewaan sepeda dan menjawab beberapa pertanyaan bisnis yang berkaitan dengan penggunaan sepeda berdasarkan kondisi cuaca, musim, waktu, dan kategori hari (hari kerja/libur). Analisis ini dilakukan menggunakan Jupyter Notebook dan berisi berbagai tahapan seperti data wrangling, exploratory data analysis (EDA), hingga visualisasi data.

## Struktur Proyek

### 1. Menentukan Pertanyaan Bisnis
Proyek ini bertujuan menjawab pertanyaan-pertanyaan berikut:
- Bagaimana pengaruh kondisi cuaca terhadap jumlah penggunaan sepeda?
- Bagaimana pengaruh musim terhadap penggunaan sepeda?
- Bagaimana pola penggunaan sepeda berdasarkan waktu (jam)?
- Apakah hari kerja dan hari libur memengaruhi jumlah pengguna sepeda?

### 2. Import Semua Packages/Library yang Digunakan
Library yang digunakan dalam proyek ini meliputi:
- **numpy**: Untuk manipulasi data numerik.
- **pandas**: Untuk manipulasi dan analisis data.
- **matplotlib** dan **seaborn**: Untuk visualisasi data.

### 3. Data Wrangling
Tahapan ini mencakup:
- **Gathering Data**: Memuat dataset dari file CSV.
- **Assessing Data**: Memeriksa tipe data, missing value, duplikasi, dan statistik deskriptif.
- **Cleaning Data**: Menghapus duplikasi data dan mengubah tipe data yang diperlukan.

### 4. Exploratory Data Analysis (EDA)
EDA dilakukan untuk menjawab pertanyaan bisnis:
1. **Pengaruh Kondisi Cuaca**:
   - Menganalisis rata-rata jumlah pengguna berdasarkan kondisi cuaca.
   - Memberikan label deskriptif pada kategori cuaca.
2. **Pengaruh Musim**:
   - Menganalisis rata-rata jumlah pengguna berdasarkan musim.
3. **Pola Penggunaan Berdasarkan Waktu (Jam)**:
   - Mengidentifikasi pola penggunaan sepeda sepanjang hari.
4. **Pengaruh Hari Kerja dan Hari Libur**:
   - Membandingkan rata-rata jumlah pengguna pada hari kerja dan hari libur.

### 5. Visualisasi Data
Visualisasi dilakukan menggunakan grafik untuk memberikan pemahaman lebih baik:
- Grafik batang untuk menunjukkan pengaruh kondisi cuaca dan musim.
- Grafik garis untuk menggambarkan pola penggunaan berdasarkan waktu.
- Analisis hari kerja dan hari libur menggunakan grafik batang.

### 6. Teknik Analisis Lanjutan
1. **Analisis Clustering**:
   - Mengelompokkan data berdasarkan jumlah penyewaan sepeda (Low, Medium, High Usage).
2. **Analisis Geospatial**:
   - Menggunakan peta interaktif untuk memvisualisasikan distribusi penggunaan berdasarkan musim.
3. **RFM Analysis**:
   - Menganalisis pengguna berdasarkan Recency, Frequency, dan Monetary untuk mengelompokkan mereka ke dalam segmen loyalitas.

## Hasil Analisis
- **Kondisi Cuaca**: Pengguna sepeda terbanyak terjadi saat cuaca cerah atau berawan ringan.
- **Musim**: Musim panas memiliki jumlah pengguna tertinggi, sementara musim semi memiliki jumlah pengguna terendah.
- **Waktu (Jam)**: Pola penggunaan menunjukkan puncak di pagi hari (7-9) dan sore hari (17-19).
- **Hari Kerja vs Hari Libur**: Penggunaan sepeda lebih banyak terjadi pada hari kerja dibandingkan hari libur.

## Cara Menjalankan Proyek
1. Pastikan Anda memiliki **Python** dan **Jupyter Notebook** terinstal.
2. Instal library yang diperlukan menggunakan `pip install -r requirements.txt`.
3. Jalankan file notebook `bike_sharing_analysis.ipynb`.

## Dataset
Dataset yang digunakan dapat ditemukan pada direktori `data/` dengan nama file `day.csv` dan `hour.csv`.



# Bike Sharing Dashboard 🚴🌆

## Deskripsi

Bike Sharing Dashboard adalah proyek tugas akhir dari program Dicoding Data Science. Dashboard ini dirancang menggunakan Streamlit untuk menampilkan analisis data penggunaan sepeda berdasarkan dataset Bike Sharing. Dashboard menyajikan berbagai visualisasi interaktif untuk membantu pengguna memahami pola penggunaan sepeda dalam berbagai kondisi waktu, cuaca, dan musim.

---

## Fitur Utama
1. **Ringkasan Statistik:**
   - Total penggunaan sepeda (harian, pengguna terdaftar, dan pengguna kasual).
2. **Analisis Temporal:**
   - Visualisasi tren penggunaan sepeda harian.
   - Identifikasi jam dengan penggunaan tertinggi dan terendah.
3. **Pengaruh Cuaca:**
   - Analisis penggunaan sepeda berdasarkan kondisi cuaca.
4. **Pengaruh Musim:**
   - Pola penggunaan sepeda di setiap musim.
5. **Hari Kerja vs Hari Libur:**
   - Perbandingan penggunaan sepeda pada hari kerja dan hari libur.

---

## Teknologi yang Digunakan
- **Python**
- **Streamlit**
- **Pandas**
- **Seaborn**
- **Matplotlib**

---

## Dataset
Proyek ini menggunakan dua dataset utama:
1. **`day.csv`**: Data penggunaan sepeda per hari.
2. **`hour.csv`**: Data penggunaan sepeda per jam.

Dataset mencakup informasi seperti:
- Jumlah pengguna sepeda (`cnt`)
- Pengguna terdaftar dan kasual
- Kondisi cuaca
- Musim
- Hari kerja atau hari libur

---

## Instalasi dan Penggunaan

### 1. Clone Repository
```bash
$ git clone <repository-url>
$ cd <repository-folder>
```

### 2. Install Dependencies
Pastikan Anda sudah menginstal Python dan pip. Install semua dependencies dengan perintah berikut:
```bash
$ pip install -r requirements.txt
```

### 3. Jalankan Aplikasi Streamlit
Jalankan perintah berikut untuk menjalankan aplikasi di localhost:
```bash
$ streamlit run app.py
```

Aplikasi akan berjalan di `http://localhost:8502/`.

### 4. Deploy ke Replit

#### Langkah-langkah:
1. Buat akun di [Replit](https://replit.com/).
2. Upload file proyek ke Replit.
3. Jalankan perintah berikut di Replit:
   ```bash
   $ pip install streamlit pandas seaborn matplotlib
   $ streamlit run app.py
   ```
4. Share URL dari Replit untuk akses publik.

Anda bisa mengakses hasil deploy saya di https://ercrew02-submission-proyek-analisis-d-dashboarddashboard-dzbobs.streamlit.app/


## Kontributor
- **Nama**: Erlangga
- **Tahun**: 2024


## Penutup
Proyek ini memberikan wawasan penting mengenai pola penggunaan sepeda, yang dapat membantu penyedia layanan bike sharing dalam mengoptimalkan operasi mereka. Analisis mendalam dilakukan melalui berbagai teknik statistik dan visualisasi, serta analisis lanjutan seperti clustering dan RFM.


