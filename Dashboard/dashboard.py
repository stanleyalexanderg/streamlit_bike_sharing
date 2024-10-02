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
season_select = st.sidebar.multiselect("Pilih Musim", df["season"].unique())
weathersit_select = st.sidebar.multiselect("Pilih Kondisi Cuaca", df["weathersit"].unique())

#FILTER DATA
filter = df[(df["season"].isin(season_select)) & (df["weathersit"].isin(weathersit_select))]

#DATA YANG DITAMPILKAN
st.subheader("Data yang Ditampilkan")
st.dataframe(filter.head(10))

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
st.write("1. Cuaca yang cerah ataupun berawan dapat meningkatkan hasil penyewaan sepeda, sedangkan cuaca yang buruk, seperti hujan atau bersalju dapat menurunkan hasil penyewaan sepeda")
st.write("2. Banyak orang yang menyewa sepeda pada musim gugur, namun pada musim semi tidak banyak yang ingin menyewa sepeda dibandingkan pada musim lainnya")
