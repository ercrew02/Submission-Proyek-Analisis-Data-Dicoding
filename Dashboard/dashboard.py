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
day_df = pd.read_csv('data/day.csv')  # Dataset harian
hour_df = pd.read_csv('data/hour.csv')  # Dataset per jam

# Judul utama
st.title("Bike Sharing Dashboard 🚴")
st.markdown("Dashboard ini menyajikan analisis penggunaan sepeda berdasarkan dataset Bike Sharing.")

# Sidebar untuk filter waktu
st.sidebar.markdown("### Rentang Waktu")
st.sidebar.markdown("2011/01/01 - 2012/12/31")

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
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.lineplot(x=pd.to_datetime(day_df['dteday']), y=day_df['cnt'], ax=ax1, color='blue', alpha=0.6)
ax1.set_title("Jumlah Pengguna Sepeda Harian")
ax1.set_xlabel("Tanggal")
ax1.set_ylabel("Jumlah Pengguna")
st.pyplot(fig1)

# Analisis waktu (jam)
st.markdown("### Pada jam berapa yang paling banyak dan paling sedikit disewa?")
hourly_counts = hour_df.groupby('hr')['cnt'].sum()
hour_max = hourly_counts.idxmax()
hour_min = hourly_counts.idxmin()

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

# Analisis cuaca
st.markdown("### Pengaruh kondisi cuaca terhadap jumlah penggunaan sepeda")
weather_counts = day_df.groupby('weathersit')['cnt'].mean()
fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.barplot(x=weather_counts.index, y=weather_counts.values, palette='viridis', ax=ax3)
ax3.set_title("Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
ax3.set_xlabel("Kondisi Cuaca")
ax3.set_ylabel("Rata-rata Jumlah Pengguna")
st.pyplot(fig3)

# Analisis musim
st.markdown("### Pengaruh musim terhadap penggunaan sepeda")
season_counts = day_df.groupby('season')['cnt'].mean()
fig4, ax4 = plt.subplots(figsize=(10, 5))
sns.barplot(x=season_counts.index, y=season_counts.values, palette='coolwarm', ax=ax4)
ax4.set_title("Penggunaan Sepeda Berdasarkan Musim")
ax4.set_xlabel("Musim")
ax4.set_ylabel("Rata-rata Jumlah Pengguna")
st.pyplot(fig4)

# Analisis hari kerja vs hari libur
st.markdown("### Pengaruh hari kerja dan hari libur terhadap jumlah pengguna sepeda")
workingday_counts = day_df.groupby('workingday')['cnt'].mean()
fig5, ax5 = plt.subplots(figsize=(10, 5))
sns.barplot(x=workingday_counts.index, y=workingday_counts.values, palette='pastel', ax=ax5)
ax5.set_title("Penggunaan Sepeda Berdasarkan Hari Kerja vs Hari Libur")
ax5.set_xlabel("Hari Kerja (0 = Libur, 1 = Kerja)")
ax5.set_ylabel("Rata-rata Jumlah Pengguna")
st.pyplot(fig5)

# Footer
st.markdown("---")
st.markdown("Erlangga - 2024")
