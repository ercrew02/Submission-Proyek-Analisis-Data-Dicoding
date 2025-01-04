import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚴",
    layout="wide",
)

# Memuat dataset
day_df = pd.read_csv('Dashboard/day.csv')  # Dataset harian
hour_df = pd.read_csv('Dashboard/hour.csv')  # Dataset per jam

# Judul utama
st.title("Bike Sharing Dashboard 🚴")
st.markdown("Dashboard ini menyajikan analisis penggunaan sepeda berdasarkan dataset Bike Sharing.")

# Mengubah kategori menjadi deskriptif
day_df['weathersit'] = day_df['weathersit'].replace({1: 'Clear', 2: 'Cloudy', 3: 'Rainy'})
day_df['season'] = day_df['season'].replace({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
day_df['workingday'] = day_df['workingday'].replace({0: 'Holiday', 1: 'Working Day'})

# Menambahkan kategori deskriptif untuk jam
def categorize_hour(hour):
    if 0 <= hour < 6:
        return 'Early Morning'
    elif 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'
        
hour_df['hour_category'] = hour_df['hr'].apply(categorize_hour)


# Sidebar untuk filter interaktif
selected_date = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    [pd.to_datetime(day_df['dteday'].min()), pd.to_datetime(day_df['dteday'].max())],
    key="date_range",
)
# Pastikan rentang tanggal valid
if isinstance(selected_date, list) and len(selected_date) == 2:
    start_date, end_date = selected_date
else:
    start_date = pd.to_datetime(day_df['dteday'].min())
    end_date = pd.to_datetime(day_df['dteday'].max())

# Filter lainnya
st.sidebar.markdown("## Filter Data")
selected_hour_category = st.sidebar.multiselect("Kategori Jam", options=hour_df['hour_category'].unique(), default=hour_df['hour_category'].unique())
selected_weather = st.sidebar.multiselect("Pilih Kondisi Cuaca", options=day_df['weathersit'].unique(), default=day_df['weathersit'].unique())
selected_season = st.sidebar.multiselect("Pilih Musim", options=day_df['season'].unique(), default=day_df['season'].unique())
selected_workingday = st.sidebar.multiselect("Pilih Hari Kerja/Libur", options=day_df['workingday'].unique(), default=day_df['workingday'].unique())

# Filter dataset berdasarkan input pengguna
filtered_data_day = day_df[
    (pd.to_datetime(day_df['dteday']).between(start_date, end_date)) &
    (day_df['weathersit'].isin(selected_weather)) &
    (day_df['season'].isin(selected_season)) &
    (day_df['workingday'].isin(selected_workingday))
]

filtered_data_hour = hour_df[
    (hour_df['hour_category'].isin(selected_hour_category))
]

# Jika semua data kosong, tampilkan pesan
if filtered_data_day.empty:
    st.warning("Tidak ada data yang cocok dengan filter yang dipilih untuk data harian.")
if filtered_data_hour.empty:
    st.warning("Tidak ada data yang cocok dengan filter yang dipilih untuk data jam.")

# Menghitung data utama
total_sharing = day_df['cnt'].sum()
total_registered = day_df['registered'].sum()
total_casual = day_df['casual'].sum()

# Menampilkan angka utama
st.markdown("### Daily Sharing")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sharing Bike", f"{total_sharing}")
col2.metric("Total Registered", f"{total_registered}")
col3.metric("Total Casual", f"{total_casual}")


# Performa penjualan (cnt harian)
st.markdown("### Performa penjualan perusahaan dalam beberapa tahun terakhir")
if not filtered_data_day.empty:
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=pd.to_datetime(filtered_data_day['dteday']), y=filtered_data_day['cnt'], ax=ax1, color='blue', alpha=0.6)
    ax1.set_title("Jumlah Pengguna Sepeda Harian")
    ax1.set_xlabel("Tanggal")
    ax1.set_ylabel("Jumlah Pengguna")
    st.pyplot(fig1)
else:
    st.info("Tidak ada data untuk performa penjualan sesuai filter yang dipilih.")

# Analisis waktu (jam)
if not filtered_data_hour.empty:
    st.markdown("### Pada jam berapa yang paling banyak dan paling sedikit disewa?")
    hourly_counts = filtered_data_hour.groupby('hr')['cnt'].sum()
    # Menentukan jam dengan penyewa terbanyak dan tersedikit
    hour_max = hourly_counts.idxmax()  # Jam dengan jumlah penyewa terbanyak
    hour_min = hourly_counts.idxmin()  # Jam dengan jumlah penyewa tersedikit
    # Membuat visualisasi
    fig2, ax2 = plt.subplots(1, 2, figsize=(15, 5))
    sns.barplot(x=hourly_counts.index, y=hourly_counts.values, ax=ax2[0], palette='Blues')
    ax2[0].set_title(f"Jam dengan banyak penyewa sepeda (Jam {hour_max})")
    ax2[0].set_xlabel("Jam")
    ax2[0].set_ylabel("Jumlah Penyewa")
    sns.barplot(x=hourly_counts.index, y=hourly_counts.values, ax=ax2[1], palette='Reds')
    ax2[1].set_title(f"Jam dengan sedikit penyewa sepeda (Jam {hour_min})")
    ax2[1].set_xlabel("Jam")
    ax2[1].set_ylabel("Jumlah Penyewa")
    st.pyplot(fig2)
else:
    st.info("Tidak ada data untuk performa penjualan sesuai filter yang dipilih.")

# Analisis cuaca
st.markdown("### Pengaruh kondisi cuaca terhadap jumlah penggunaan sepeda")
if not filtered_data_day.empty:
    weather_counts = filtered_data_day.groupby('weathersit')['cnt'].mean()
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=weather_counts.index, y=weather_counts.values, palette='viridis', ax=ax3)
    ax3.set_title("Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
    ax3.set_xlabel("Kondisi Cuaca")
    ax3.set_ylabel("Rata-rata Jumlah Pengguna")
    st.pyplot(fig3)
else:
    st.info("Tidak ada data untuk performa penjualan sesuai filter yang dipilih.")

# Analisis musim
st.markdown("### Pengaruh musim terhadap penggunaan sepeda")
if not filtered_data_day.empty:
    season_counts = filtered_data_day.groupby('season')['cnt'].mean()
    fig4, ax4 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=season_counts.index, y=season_counts.values, palette='coolwarm', ax=ax4)
    ax4.set_title("Penggunaan Sepeda Berdasarkan Musim")
    ax4.set_xlabel("Musim")
    ax4.set_ylabel("Rata-rata Jumlah Pengguna")
    st.pyplot(fig4)
else:
    st.info("Tidak ada data untuk performa penjualan sesuai filter yang dipilih.")

# Analisis hari kerja vs hari libur
st.markdown("### Pengaruh hari kerja dan hari libur terhadap jumlah pengguna sepeda")
if not filtered_data_day.empty:
    workingday_counts = filtered_data_day.groupby('workingday')['cnt'].mean()
    fig5, ax5 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=workingday_counts.index, y=workingday_counts.values, palette='pastel', ax=ax5)
    ax5.set_title("Penggunaan Sepeda Berdasarkan Hari Kerja vs Hari Libur")
    ax5.set_xlabel("Hari Kerja/Libur")
    ax5.set_ylabel("Rata-rata Jumlah Pengguna")
    st.pyplot(fig5)
else:
    st.info("Tidak ada data untuk performa penjualan sesuai filter yang dipilih.")

# Footer
st.markdown("---")
st.markdown("Erlangga - 2024")
