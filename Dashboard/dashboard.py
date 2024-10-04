import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("Dashboard/day.csv")
    df["season"] = df["season"].map({1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"})
    df["weathersit"] = df["weathersit"].map({1: "Clear/Partly Cloudy", 2: "Mist/Cloudy", 3: "Light Snow/Rain", 4: "Heavy Rain/Snow"})
    return df

df = load_data()

st.title("Analisis Bike Sharing Dataset")

#SIDEBAR
st.sidebar.header("Filter Data")
season_select = st.sidebar.multiselect("Pilih Musim", df["season"].unique(), default=df["season"].unique())
weathersit_select = st.sidebar.multiselect("Pilih Kondisi Cuaca", df["weathersit"].unique(), default=df["weathersit"].unique())

#FILTER DATA
filter = df[(df["season"].isin(season_select)) & (df["weathersit"].isin(weathersit_select))]

#DATA YANG DITAMPILKAN
st.subheader("Data yang Ditampilkan")
st.dataframe(filter.head(10))

#EDA
st.subheader("Exploratory Data Analysis (EDA)")

#MENGATUR GRAFIK DENGAN MATRIKS 2X2 DENGAN UKURAN GAMBAR 16X10
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

#GRAFIK PERTAMA: Pengaruh Suhu dan Cuaca Terhadap Jumlah Penyewaan
sns.scatterplot(data=df, x="temp", y="cnt", hue="weathersit", ax=axes[0, 0])
axes[0, 0].set_title("Pengaruh Suhu dan Cuaca Terhadap Jumlah Sepeda yang Disewa")
axes[0, 0].set_xlabel("Suhu")
axes[0, 0].set_ylabel("Jumlah Penyewaan")

#GRAFIK KEDUA: Pengaruh Kecepatan Angin dan Musim Terhadap Jumlah Penyewaan
sns.scatterplot(data=df, x="windspeed", y="cnt", hue="season", palette="Set3", s=100, ax=axes[0, 1])
axes[0, 1].set_title('Pengaruh Kecepatan Angin dan Musim Terhadap Sepeda yang Disewa')
axes[0, 1].set_xlabel('Kecepatan Angin')
axes[0, 1].set_ylabel('Jumlah Penyewaan')

#GRAFIK KETIGA: Total Penyewaan Berdasarkan Musim dan Kondisi Cuaca
sns.barplot(data=df, x='season', y='cnt', hue='weathersit', palette='coolwarm', ax=axes[1, 0])
axes[1, 0].set_title('Total Penyewaan Sepeda Berdasarkan Musim dan Kondisi Cuaca')
axes[1, 0].set_xlabel('Musim')
axes[1, 0].set_ylabel('Jumlah Penyewaan')

#MENGKOSONGKAN BARIS 2 KOLOM 2
fig.delaxes(axes[1, 1])

#MENAMPILKAN GRAFIK SESUAI MATRIKS 2X2
plt.tight_layout()
st.pyplot(fig)

#VISUALISASI 1
st.subheader("Pengaruh Cuaca Terhadap Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots()
sns.barplot(data=filter, x="weathersit", y="cnt", ax=ax)
plt.title("Jumlah Penyewaan Berdasarkan Kondisi Cuaca")
st.pyplot(fig)

#VISUALISASI 2
st.subheader("Pengaruh Musim Terhadap Jumlah Penyewaan Sepeda")
fig2, ax2 = plt.subplots()
sns.barplot(data=filter, x="season", y="cnt", ax=ax2)
plt.title("Jumlah Penyewaan Berdasarkan Musim")
st.pyplot(fig2)

st.subheader("Kesimpulan Analisa Bike Sharing")
st.write("Berdasarkan analisa dataset Bike-Sharing, dapat disimpulkan beberapa hal, yaitu:")
st.write("1. Cuaca yang cerah ataupun berawan dapat meningkatkan hasil penyewaan sepeda per harinya, sedangkan cuaca yang buruk, seperti hujan atau bersalju dapat menurunkan hasil penyewaan sepeda per harinya")
st.write("2. Banyak orang yang menyewa sepeda pada musim gugur, namun pada musim semi tidak banyak yang ingin menyewa sepeda dibandingkan pada musim lainnya")
