# -*- coding: utf-8 -*-
"""Stunting_XGBoost.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1adWJ5YSKFS97c-x38fxrs2cWacj7655x

# Import Library dan Read Data
"""

# Model ini dibuat dengan menggunakan Scikit-Learn versi 1.5

# Karena terdapat perubahan pada API Scikit-Learn versi 1.6 keatas,
# maka untuk penggunaan model ini diharapkan agar tidak melakukan update sklearn.
# Apabila dilakukan update, maka akan terdapat gangguan pada proses Cross-Validation

from google.colab import drive
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency, pearsonr, spearmanr
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
import xgboost as xgb
from sklearn.metrics import confusion_matrix, classification_report

drive.mount('/content/drive', force_remount=True)
file_path = '/content/drive/MyDrive/Dataset/data_balita.csv'

data = pd.read_csv(file_path)

"""# Explorasi Data"""

print("Informasi Dataset:")
print(data.info())

print("\nPreview Data:")
print(data.head())

# 1. Analisis Statistik Umur
print("1. Analisis Statistik Umur:")
umur_stats = data['Umur (bulan)'].describe()
print(umur_stats)
print(f"Rentang Umur: {data['Umur (bulan)'].min()} - {data['Umur (bulan)'].max()} bulan\n")

# 2. Analisis Statistik Tinggi Badan
print("2. Analisis Statistik Tinggi Badan:")
tinggi_badan_stats = data['Tinggi Badan (cm)'].describe()
print(tinggi_badan_stats)
# Hitung Kuartil
q1 = data['Tinggi Badan (cm)'].quantile(0.25)
q2 = data['Tinggi Badan (cm)'].quantile(0.50)  # Median
q3 = data['Tinggi Badan (cm)'].quantile(0.75)
print(f"\nKuartil Tinggi Badan:")
print(f"Q1 (25%): {q1:.2f} cm")
print(f"Q2 (Median): {q2:.2f} cm")
print(f"Q3 (75%): {q3:.2f} cm\n")

# 3. Frekuensi Jenis Kelamin
print("3. Frekuensi Jenis Kelamin:")
gender_freq = data['Jenis Kelamin'].value_counts()
gender_persen = data['Jenis Kelamin'].value_counts(normalize=True) * 100
for gender, freq in gender_freq.items():
    persen = gender_persen[gender]
    print(f"{gender}: {freq} ({persen:.2f}%)")
print()

# 4. Frekuensi Status Gizi
print("4. Frekuensi Status Gizi:")
status_gizi_freq = data['Status Gizi'].value_counts()
status_gizi_persen = data['Status Gizi'].value_counts(normalize=True) * 100
for status, freq in status_gizi_freq.items():
    persen = status_gizi_persen[status]
    print(f"{status}: {freq} ({persen:.2f}%)")

# Visualisasi

# 1. Histogram Umur
plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
data['Umur (bulan)'].hist(bins=20)
plt.title('Distribusi Umur')
plt.xlabel('Umur (bulan)')
plt.ylabel('Frekuensi')

# 2. Boxplot Tinggi Badan
plt.subplot(2,2,2)
sns.boxplot(x=data['Tinggi Badan (cm)'])
plt.title('Boxplot Tinggi Badan')
plt.xlabel('Tinggi Badan (cm)')

# 3. Pie Chart Jenis Kelamin
plt.subplot(2,2,3)
data['Jenis Kelamin'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribusi Jenis Kelamin')

# 4. Bar Plot Status Gizi
plt.subplot(2,2,4)
data['Status Gizi'].value_counts().plot(kind='bar')
plt.title('Frekuensi Status Gizi')
plt.xlabel('Status Gizi')
plt.ylabel('Frekuensi')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Korelasi Pearson untuk variabel numerik
print("1. Korelasi Pearson antara Umur dan Tinggi Badan:")

# Hitung korelasi Pearson
pearson_corr, p_value = pearsonr(data['Umur (bulan)'], data['Tinggi Badan (cm)'])

print(f"Koefisien Korelasi Pearson: {pearson_corr:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpretasi korelasi
if p_value < 0.05:
    print("Korelasi statistik signifikan pada α = 0.05")
else:
    print("Tidak ada korelasi statistik signifikan")

# Korelasi Spearman (untuk data tidak linear)
print("\n2. Korelasi Spearman antara Umur dan Tinggi Badan:")
spearman_corr, spearman_p = spearmanr(data['Umur (bulan)'], data['Tinggi Badan (cm)'])

print(f"Koefisien Korelasi Spearman: {spearman_corr:.4f}")
print(f"P-value: {spearman_p:.4f}")

if spearman_p < 0.05:
    print("Korelasi statistik signifikan pada α = 0.05")
else:
    print("Tidak ada korelasi statistik signifikan")


# Scatter plot untuk visualisasi
plt.figure(figsize=(10, 6))
plt.scatter(data['Umur (bulan)'], data['Tinggi Badan (cm)'], alpha=0.5)
plt.title('Hubungan Tinggi Badan dan Umur')
plt.xlabel('Umur (bulan)')
plt.ylabel('Tinggi Badan (cm)')

plt.figure(figsize=(15, 5))

# Boxplot Tinggi Badan berdasarkan Status Gizi
plt.subplot(1, 3, 1)
sns.boxplot(x='Jenis Kelamin', y='Tinggi Badan (cm)', data=data)
plt.title('Distribusi Tinggi Badan per Jenis Kelamin')

# Boxplot Tinggi Badan berdasarkan Jenis Kelamin
plt.subplot(1, 3, 2)
sns.boxplot(x='Status Gizi', y='Tinggi Badan (cm)', data=data)
plt.title('Distribusi Tinggi Badan per Status Gizi')

# Boxplot Status Gizi berdasarkan Umur
plt.subplot(1, 3, 3)
sns.boxplot(x='Status Gizi', y='Umur (bulan)', data=data)
plt.title('Distribusi Umur per Status Gizi')
plt.tight_layout()
plt.show()

# Uji Chi-Square untuk Jenis Kelamin dan Status Gizi
print("Uji Independensi Chi-Square (Jenis Kelamin vs Status Gizi):")

# Buat tabel kontingensi
contingency_table = pd.crosstab(data['Jenis Kelamin'], data['Status Gizi'])
print("\nTabel Kontingensi:")
print(contingency_table)

# Uji Chi-Square
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

print(f"\nNilai Chi-Square: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")
print(f"Derajat Kebebasan: {dof}")

# Interpretasi
if p_value < 0.05:
    print("Ada hubungan signifikan antara Jenis Kelamin dan Status Gizi")
else:
    print("Tidak ada hubungan signifikan antara Jenis Kelamin dan Status Gizi")

# Visualisasi hubungan
plt.figure(figsize=(10, 6))
sns.heatmap(contingency_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Hubungan Jenis Kelamin dan Status Gizi')
plt.xlabel('Status Gizi')
plt.ylabel('Jenis Kelamin')
plt.show()

"""# Preprocessing Data"""

required_columns = [
    'Umur (bulan)',
    'Jenis Kelamin',
    'Tinggi Badan (cm)',
    'Status Gizi'
]

missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    print("Kolom yang hilang:", missing_columns)
else:
    print("Kolom pada dataset sudah lengkap")

print("\nMissing Values:")
print(data.isnull().sum())

data = data.dropna()

le_gender = LabelEncoder()
data['jenis_kelamin_encoded'] = le_gender.fit_transform(data['Jenis Kelamin'])

le_status_gizi = LabelEncoder()
data['status_gizi_encoded'] = le_status_gizi.fit_transform(data['Status Gizi'])

print("Preview Data Setelah Preprocessing:")
print(data.head())

# Deteksi outliers menggunakan Z-Score
numeric_cols = ['Tinggi Badan (cm)', 'Umur (bulan)']

print("Deteksi Outliers menggunakan Z-Score:")
for col in numeric_cols:
    # Hitung Z-Score
    z_scores = np.abs(stats.zscore(data[col]))

    # Tentukan outliers (Z-Score > 3)
    outliers = data[z_scores > 3]

    print(f"\nOutliers pada {col}:")
    print(f"Jumlah Outliers: {len(outliers)}")
    print(f"Persentase Outliers: {len(outliers)/len(data)*100:.2f}%")

    # Tampilkan beberapa outliers
    if len(outliers) > 0:
        print("\nContoh Outliers:")
        print(outliers)

# Deteksi outliers menggunakan Metode IQR (Interquartile Range)
print("\nDeteksi Outliers menggunakan IQR:")
numeric_cols = ['Tinggi Badan (cm)', 'Umur (bulan)']

for col in numeric_cols:
    # Hitung IQR
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1

    # Tentukan batas bawah dan atas
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Temukan outliers
    outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]

    print(f"\nOutliers pada {col}:")
    print(f"Jumlah Outliers: {len(outliers)}")
    print(f"Persentase Outliers: {len(outliers)/len(data)*100:.2f}%")
    print(f"Rentang Normal: {lower_bound:.2f} - {upper_bound:.2f}")

    # Tampilkan beberapa outliers
    if len(outliers) > 0:
        print("\nContoh Outliers:")
        print(outliers.head())

# Penanganan Ouliers

# Tidak dilakukan karena persentase outliers yang sangat rendah dan tidak mempengaruhi model secara signifikan

# Pembagian Dataset
X = data[['Umur (bulan)', 'Tinggi Badan (cm)', 'jenis_kelamin_encoded']]
y = data['status_gizi_encoded']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Menampilkan jumlah kelas sebelum undersampling
print("Jumlah kelas sebelum undersampling:")
print(pd.Series(y_train).value_counts())

# Menggunakan RandomUnderSampler untuk mengurangi data mayoritas
undersampler = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = undersampler.fit_resample(X_train, y_train)

# Menampilkan jumlah kelas setelah undersampling
print("Jumlah kelas setelah undersampling:")
print(pd.Series(y_resampled).value_counts())

"""# Implementasi Model"""

model = xgb.XGBClassifier(
    learning_rate=0.1,
    max_depth=6,
    n_estimators=200,
    subsample=0.8,
    objective='multi:softprob',
    num_class=len(np.unique(y))
)

model.fit(X_resampled, y_resampled)

y_pred = model.predict(X_test)

matplotlib.rcParams.update({
    'figure.figsize': (25, 10),
    'figure.dpi': 200,
    'font.size': 10
})

plt.figure()
# for i in range(min(model.n_estimators, 2)): # Print Sebagian
for i in range(model.n_estimators):           # Print Keseluruhan
    xgb.plot_tree(
        model,
        num_trees=i,
        feature_names=list(X.columns),
        ax=plt.gca())
    plt.title(f'Pohon ke-{i+1}')
    plt.show()

"""# Evaluasi Model"""

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')

print("Cross-Validation Scores:")
print(cv_scores)
print(f"Mean CV Score: {cv_scores.mean():.4f}")
print(f"Standard Deviation: {cv_scores.std():.4f}")

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10,8))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=le_status_gizi.classes_,
    yticklabels=le_status_gizi.classes_
)
plt.title('Confusion Matrix')
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.tight_layout()
plt.show()

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=le_status_gizi.classes_
))

"""# Analisis Kepentingan Fitur"""

feature_importance = model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(10,6))
sns.barplot(x=feature_importance, y=feature_names)
plt.title('Kepentingan Fitur dalam Prediksi Status Gizi')
plt.xlabel('Skor Kepentingan')
plt.ylabel('Fitur')
plt.tight_layout()
plt.show()

"""# Uji Prediksi"""

# Fungsi untuk mendapatkan input dari pengguna
def get_user_input():
    jenis_kelamin = input("Masukkan jenis kelamin anak (Laki-laki/Perempuan): ")
    umur = int(input("Masukkan umur anak (bulan): "))
    tinggi_badan = float(input("Masukkan tinggi badan anak (cm): "))
    return umur, jenis_kelamin, tinggi_badan

# Mendapatkan data baru dari pengguna
umur_baru, jenis_kelamin_baru, tinggi_badan_baru = get_user_input()

# Membuat DataFrame baru dengan data yang dimasukkan oleh pengguna
data_baru = pd.DataFrame({
    'Umur (bulan)': [umur_baru],
    'Jenis Kelamin': [jenis_kelamin_baru],
    'Tinggi Badan (cm)': [tinggi_badan_baru]
})

# Lakukan preprocessing pada data baru
data_baru['jenis_kelamin_encoded'] = le_gender.fit_transform(data_baru['Jenis Kelamin'])

# Siapkan fitur untuk prediksi
X_baru = data_baru[['Umur (bulan)', 'Tinggi Badan (cm)', 'jenis_kelamin_encoded']]

# Lakukan prediksi
prediksi = model.predict(X_baru)
prediksi_proba = model.predict_proba(X_baru)

# Ubah hasil prediksi menjadi label asli
data_baru['status_gizi_prediksi'] = le_status_gizi.inverse_transform(prediksi)

# Tampilkan hasil prediksi
print("\nHasil Prediksi untuk Data Baru:")
print(data_baru[['Umur (bulan)', 'Jenis Kelamin', 'Tinggi Badan (cm)', 'status_gizi_prediksi']])
print("\nProbabilitas Prediksi:")
print(prediksi_proba)