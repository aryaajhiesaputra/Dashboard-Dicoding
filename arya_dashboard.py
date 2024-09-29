import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('fix_data.csv')

# Create a title for the dashboard
st.title('Dashboard Penyewaan Sepeda')

# Display some basic statistics
st.subheader('Statistik Dasar')
col1, col2, col3 = st.columns(3)
col1.metric('Total Penyewa', df['cnt'].sum().round(2))
col2.metric('Biasa', df['casual'].sum().round(2))
col3.metric('Registrasi', df['registered'].sum().round(2))

# Display a line plot to compare the casual and registered users over time
st.subheader('Comparison of Casual and Registered Users Over Time')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['dteday'], df['casual'], label='Casual')
ax.plot(df['dteday'], df['registered'], label='Registered')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penyewa')
ax.set_title('Perbandingan Jumlah Penyewa Casual dan Registered dari Waktu ke Waktu')
ax.legend()
st.pyplot(fig)

# Display a bar chart of the total count of bikes by weekday
st.subheader('Total Penyewa dalam Hari')
weekday_counts = df.groupby('weekday')['cnt'].sum()
fig, ax = plt.subplots()
ax.bar(weekday_counts.index, weekday_counts.values)
ax.set_xlabel('Hari')
ax.set_ylabel('Total Penyewa')
ax.set_title('Total Penyewa dalam Hari')
st.pyplot(fig)

# Display a bar chart of the top 5 months with the highest total count of bikes
st.subheader('5 Bulan dengan Penyewa Terbanyak')
top_months = df.groupby('mnth')['cnt'].sum().sort_values(ascending=False).head(5)
fig, ax = plt.subplots()
ax.bar(top_months.index, top_months.values)
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Penyewa')
ax.set_title('5 Bulan dengan Penyewa Terbanyak')
st.pyplot(fig)

# Display a scatter plot of the relationship between temperature and total count of bikes
st.subheader('Hubungan Antara Suhu dan Jumlah Penyewa')
fig, ax = plt.subplots()
ax.scatter(df['temp'], df['cnt'])
ax.set_xlabel('Suhu')
ax.set_ylabel('Total Penyewa')
ax.set_title('Hubungan Antara Suhu dan Total Penyewa')
st.pyplot(fig)
