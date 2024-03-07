# <font color="#000080"> Qia E-commerce Dashboard ✨</font>
# Setup environment
```python
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```
# Intalasi dan Konfigurasi

```python
!pip install streamlit babel -q
!wget -q -O - ipv4.icanhazip.com
! streamlit run dashboard.py & npx localtunnel --port 8501
```
- `!pip install streamlit babel -q`: Ini adalah perintah untuk menginstal paket Streamlit dan Babel menggunakan pip. -q digunakan untuk mode "quiet", yang berarti output instalasi tidak akan ditampilkan ke layar.

- `!wget -q -O - ipv4.icanhazip.com`: Perintah ini menggunakan wget untuk mengunduh data dari ipv4.icanhazip.com, yang kemungkinan besar adalah untuk mendapatkan alamat IP publik dari host Anda saat ini. Opsi -q digunakan untuk mode "quiet", yang berarti wget tidak akan menampilkan keluaran apa pun ke layar, dan -O - digunakan untuk menunjukkan bahwa output akan ditampilkan di stdout.

- `!streamlit run dashboard.py & npx localtunnel --port 8501`: Ini adalah gabungan dari dua perintah. Yang pertama adalah streamlit run dashboard.py, yang menjalankan aplikasi Streamlit menggunakan file dashboard.py sebagai argumen. & digunakan untuk menjalankan perintah tersebut di latar belakang. Kemudian, perintah npx localtunnel --port 8501 digunakan untuk membuat terowongan lokal menggunakan port 8501, yang akan memungkinkan akses ke aplikasi Streamlit melalui internet menggunakan URL yang dibuat oleh localtunnel.


<font size="3">Streamlit dapat digunakan dengan bahasa pemrograman Python. Jadi sebelumnya saya sudah membuat file bernama dashboard.py. berikut dibawah ini adalah code yang sudah saya buat</font>


```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_rfm_df(df):
    rfm_df = df.groupby(by="customer_id", as_index=False).agg({
        "order_delivered_customer_date": "max", 
        "order_id": "nunique",
        "payment_value": "sum"
    })
    rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]
    
    rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
    recent_date = df["order_delivered_customer_date"].dt.date.max()
    rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)
    rfm_df.drop("max_order_timestamp", axis=1, inplace=True)
    
    return rfm_df

all_df = pd.read_csv("all.csv")

all_df["order_delivered_customer_date"] = pd.to_datetime(all_df["order_delivered_customer_date"])

min_date = all_df["order_delivered_customer_date"].min()
max_date = all_df["order_delivered_customer_date"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

st.header('Alesandora Dashboard :sparkles:')
rfm_df = create_rfm_df(all_df)
st.subheader("Best Customer Based on RFM Parameters")
 
col1, col2, col3 = st.columns(3)
 
with col1:
    avg_recency = round(rfm_df.recency.mean(), 1)
    st.metric("Average Recency (days)", value=avg_recency)
 
with col2:
    avg_frequency = round(rfm_df.frequency.mean(), 2)
    st.metric("Average Frequency", value=avg_frequency)
 
with col3:
    avg_frequency = format_currency(rfm_df.monetary.mean(), "AUD", locale='es_CO') 
    st.metric("Average Monetary", value=avg_frequency)
 
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(35, 15))
colors = ["#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9"]
 
sns.barplot(y="recency", x="customer_id", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("customer_id", fontsize=30)
ax[0].set_title("By Recency (days)", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=30)
ax[0].tick_params(axis='x', labelsize=25, rotation=90)
 
sns.barplot(y="frequency", x="customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("customer_id", fontsize=30)
ax[1].set_title("By Frequency", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=30)
ax[1].tick_params(axis='x', labelsize=25, rotation=90)
 
sns.barplot(y="monetary", x="customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel("customer_id", fontsize=30)
ax[2].set_title("By Monetary", loc="center", fontsize=50)
ax[2].tick_params(axis='y', labelsize=30)
ax[2].tick_params(axis='x', labelsize=25, rotation=90)
 
st.pyplot(fig)
```

<font size="3">Setelah sudah menyelesaikan langkah diatas, selanjutnya akan muncul output yang berisi url untuk melihat streamlit yang sudah kita buat tadi</font>


```python
35.224.127.238
[##................] - fetchMetadata: sill resolveWithNewModule yargs-parser@20
Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.


  You can now view your Streamlit app in your browser.

  Network URL: http://172.28.0.12:8501
  External URL: http://35.224.127.238:8501

npx: installed 22 in 10.02s
your url is: https://hungry-coats-post.loca.lt
```
<font size="3">ini adalah url yang kita dapatkan untuk melihat streamlit yang sudah kita buat: **https://tough-berries-rhyme.loca.lt**</font>

![Text Alternatif](https://s9.gifyu.com/images/SUSUs.png)


<font size="3">ini adalah tampilan awal link url nya setelah kita buka, namun kita harus memasukan **Tunnel Password** nya terlebih dahulu.</font>

<font size="3">**Tunnel Password** nya dapat kita lihat di hasil output dari code install package yang tadi sudah kita jalankan</font>

![Text Alternatif](https://s9.gifyu.com/images/SUSVU.jpg)

<font size="3"> angka ini **35.224.127.238** adalah Tunnel Password yang kita butuhkan untuk membuka dashboard kita.</font>

![Text Alternatif](https://s9.gifyu.com/images/SUSZ3.png)

<font size="3">lalu klick **"Submit"** dan Dashboard yang kita buat akan terlihat</font>


![Text Alternatif](https://s9.gifyu.com/images/SUHIl.png)

![Text Alternatif](https://s9.gifyu.com/images/SUHIZ.png)

<font size="3">Berikut merupakan tampilan dari <font size="4" color="#000080"><b>Qia E-commerce Dashboard ✨</b></font>
</font>

<font size="3">note: 
URL Streamlit (misalnya, URL aplikasi Streamlit yang dijalankan di server lokal Anda) tidak bisa diakses di luar jaringan lokal secara default karena alasan keamanan. Ini adalah tindakan keamanan yang umumnya diterapkan oleh sistem operasi dan firewall untuk melindungi jaringan dari akses yang tidak sah.Saat menjalankan aplikasi Streamlit secara lokal, itu hanya dapat diakses melalui URL yang berbasis localhost seperti http://localhost:8501. Ini berarti aplikasi hanya dapat diakses dari komputer yang menjalankannya.</font>
