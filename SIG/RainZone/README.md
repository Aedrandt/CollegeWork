# Prediksi Rawan Banjir Kota Bengkulu
Proyek ini melakukan analisis dan pemodelan prediksi tingkat kerawanan banjir di wilayah Kota Bengkulu. Kategori dearah terpisah menjadi sembilan kecamatan yang ada di Kota Bengkulu. Pendekatan yang dilakukan adalah dengan menggunakan Machine Learning yaitu algoritma Random Forest(RF). Algoritma RF dipilih karena sesuai dengan tipe proyek ini yang mengklasifikasikan suatu daerah (Rawan banjir atau tidak). Kemudian, dengan tahapan perata-rataan dari banyaknya pohon acak yang dibuat RF dapat mengurangi kemungkinan kesalahan prediksi.

## Data yang Digunakan
- Batas Wilayah Kecamatan di Kota Bengkulu
- Data Penggunaan/Tutupan Lahan
- Data Kelas Kemiringan Lereng
- Data Elevasi Wilayah
- Data Curah Hujan(2020-2024)
- Data Kecamatan yang Rawan Banjir

## Model Prediksi
Model dari proyek ini dapat didownload pada file dengan nama "SIG_RainZone.ipynb".
Atau dengan mengakses Google Colab berikut: https://colab.research.google.com/drive/17-B5rcm8vaw2zkTDP0UZhzAhBxgJdZTd?usp=sharing

## Peta Daerah Rawan Banjir di Kota Bengkulu
Peta daerah rawan banjir ini dapat dilihat melalui file "peta_prediksi_banjir.html".

## Penggunaan
Proyek ini dikembangkan dengan menggunakan Google Colab. Penggunaan ulang proyek ini dapat dilakukan mmelalui langkah berikut:
1. Download/Copy file Model Prediksi.
2. Unduh Dataset yang diperlukan (Terdapat pada folder ini), kemudian extract dan simpan ke dalam Drive pribadi anda.
3. Modifikasi Path/Jalur untuk mengakses dataset, sesuai dengan tempat anda menyimpannya.
4. Jalankan sel sesuai dengan urutannya dari atas ke bawah.
