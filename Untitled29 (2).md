# <font color="#000080"> Qia E-commerce Dashboard ✨</font>
# Setup environment

conda create --name main-ds python=3.9 
//
conda activate main-ds
//
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel

# Intalasi dan Konfigurasi

!pip install streamlit babel -q
!wget -q -O - ipv4.icanhazip.com
! streamlit run dashboard.py & npx localtunnel --port 8501


<font size="3">Streamlit dapat digunakan dengan bahasa pemrograman Python. Jadi sebelumnya saya sudah membuat file bernama dashboard.py</font>


```python
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')  # Menggunakan whitegrid sebagai tema

import pandas as pd

# Data untuk grafik pertama
review_scores = [5, 4, 1, 3, 2]
counts = [56910, 19007, 11282, 8097, 3114]

# Data untuk grafik kedua (dari DataFrame orders_customers_df)
orders_customers_df = pd.DataFrame({
    "customer_city": ["sao paulo", "rio de janeiro", "belo horizonte", "brasilia", "curitiba", "campinas", "porto alegre", "salvador", "guarulhos", "sao bernardo do campo"],
    "order_id": [15540, 6882, 2773, 2131, 1521, 1444, 1379, 1245, 1189, 938]
})

# Aplikasi Streamlit
st.set_page_config(page_title="Qia Ecommerce Dashboard", page_icon=":chart_with_upwards_trend:")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    

st.header('Qia E-commerce Dashboard \U0001F4AB')

# Grafik pertama
st.subheader("Number of High Rating Scores")
plt.figure(figsize=(10, 5))
plt.bar(review_scores, counts, color="#72BCD4")
plt.title("Number of High Rating Scores", loc="center", fontsize=20)
plt.xlabel("Rating Score", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
st.pyplot(plt)

# Grafik kedua
st.subheader("Top 10 Cities by Number of Orders")
top_cities = orders_customers_df.sort_values(by='order_id', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_cities['customer_city'], top_cities['order_id'], color="#72BCD4")
plt.title("Top 10 Cities by Number of Orders", loc="center", fontsize=20)
plt.xlabel("Number of Orders", fontsize=14)
plt.ylabel("City", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.gca().invert_yaxis()
st.pyplot(plt)
```

<font size="3">baik sekarang kita sudah mempunyai data Dashboard.py. seperti contoh diatas.</font>


```python
!pip install streamlit babel -q
!wget -q -O - ipv4.icanhazip.com
! streamlit run dashboard.py & npx localtunnel --port 8501
```

<font size="3">Code diatas digunakan untuk menjalankan dashboard kita dilokal host</font>

- `!pip install streamlit babel -q`: Ini adalah perintah untuk menginstal paket Streamlit dan Babel menggunakan pip. -q digunakan untuk mode "quiet", yang berarti output instalasi tidak akan ditampilkan ke layar.

- `!wget -q -O - ipv4.icanhazip.com`: Perintah ini menggunakan wget untuk mengunduh data dari ipv4.icanhazip.com, yang kemungkinan besar adalah untuk mendapatkan alamat IP publik dari host Anda saat ini. Opsi -q digunakan untuk mode "quiet", yang berarti wget tidak akan menampilkan keluaran apa pun ke layar, dan -O - digunakan untuk menunjukkan bahwa output akan ditampilkan di stdout.

- `!streamlit run dashboard.py & npx localtunnel --port 8501`: Ini adalah gabungan dari dua perintah. Yang pertama adalah streamlit run dashboard.py, yang menjalankan aplikasi Streamlit menggunakan file dashboard.py sebagai argumen. & digunakan untuk menjalankan perintah tersebut di latar belakang. Kemudian, perintah npx localtunnel --port 8501 digunakan untuk membuat terowongan lokal menggunakan port 8501, yang akan memungkinkan akses ke aplikasi Streamlit melalui internet menggunakan URL yang dibuat oleh localtunnel.

<font size="3">Setelah berhasil menginstall package tersebut, selanjutnya akan ada output berisi:</font>


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

<font size="3">kali ini kita sudah mendapatkan url dari Dashboard yang telah kita buat tadi.</font>

<font size="3">your url is: **https://tough-berries-rhyme.loca.lt**</font>

![Text Alternatif](https://s9.gifyu.com/images/SUSUs.png)


<font size="3">ini adalah tampilan awal link url nya setelah kita buka, namun kita harus memasukan **Tunnel Password** nya terlebih dahulu.</font>

<font size="3">**Tunnel Password** nya dapat kita lihat di hasil output dari code install package yang tadi sudah kita jalankan</font>

![Text Alternatif](https://s9.gifyu.com/images/SUSVU.jpg)

<font size="3"> angka ini **35.224.127.238** adalah Tunnel Password yang kita butuhkan untuk membuka dashboard kita.</font>

![Text Alternatif](https://s9.gifyu.com/images/SUSZ3.png)

<font size="3">lalu klick **"Submit"** dan Dashboard yang kita buat akan terlihat</font>


![Text Alternatif](https://s9.gifyu.com/images/SUSaK.png)

![Text Alternatif](https://s9.gifyu.com/images/SUSaI.png)

<font size="3">Berikut merupakan tampilan dari <font size="4" color="#000080"><b>Qia E-commerce Dashboard ✨</b></font>
</font>

<font size="3">note: 
URL Streamlit (misalnya, URL aplikasi Streamlit yang dijalankan di server lokal Anda) tidak bisa diakses di luar jaringan lokal secara default karena alasan keamanan. Ini adalah tindakan keamanan yang umumnya diterapkan oleh sistem operasi dan firewall untuk melindungi jaringan dari akses yang tidak sah.Saat menjalankan aplikasi Streamlit secara lokal, itu hanya dapat diakses melalui URL yang berbasis localhost seperti http://localhost:8501. Ini berarti aplikasi hanya dapat diakses dari komputer yang menjalankannya.</font>
