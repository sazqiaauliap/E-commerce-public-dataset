import streamlit as st
import matplotlib.pyplot as plt
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

st.title('Belajar Analisis Data')
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.header("Number of High Rating Scores")
    plt.figure(figsize=(8, 5))
    plt.bar(review_scores, counts, color="#72BCD4")
    plt.title("Number of High Rating Scores", loc="center", fontsize=16)
    plt.xlabel("Rating Score", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(plt)
    st.write("Berdasarkan data yang diberikan, sejumlah besar pelanggan memberikan penilaian positif. Sebanyak 75.917 pelanggan telah memberi peringkat produk dengan skor 4 atau 5, yang menunjukkan kepuasan. Ini menunjukkan mayoritas besar pelanggan merasa puas dengan kualitas dan kinerja produk. Namun, perlu dicatat bahwa ada juga sejumlah pelanggan yang memberikan penilaian lebih rendah, dengan 11.282 pelanggan memberi peringkat 1, yang mungkin menunjukkan ada hal yang perlu diperbaiki. Secara keseluruhan, data menunjukkan penerimaan positif untuk produk ini, dengan sebagian besar pelanggan menyatakan kepuasan.")

with tab2:
    st.header("Top 10 Cities by Number of Orders")
    top_cities = orders_customers_df.sort_values(by='order_id', ascending=False).head(10)
    plt.figure(figsize=(8, 6))
    plt.barh(top_cities['customer_city'], top_cities['order_id'], color="#72BCD4")
    plt.title("Top 10 Cities by Number of Orders", loc="center", fontsize=16)
    plt.xlabel("Number of Orders", fontsize=12)
    plt.ylabel("City", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.gca().invert_yaxis()
    st.pyplot(plt)
    st.write("Gambaran distribusi kota-kota di mana produk paling sering dibeli oleh pelanggan menunjukkan bahwa São Paulo memimpin dengan jumlah pelanggan tertinggi, total 15.540. Setelah São Paulo, kota-kota lain yang mencolok termasuk Rio de Janeiro dengan 6.882 pelanggan, Belo Horizonte dengan 2.773 pelanggan, Brasília dengan 2.131 pelanggan, dan Curitiba dengan 1.521 pelanggan. Distribusi ini menunjukkan konsentrasi penjualan di pusat-pusat perkotaan utama, dengan São Paulo sebagai pasar utama untuk penjualan produk.")
