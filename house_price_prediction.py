# import package
import pickle
import pandas as pd
import numpy as numpy
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# making sidebar
with st.sidebar:
    selected = option_menu("Main Menu",
    ["About Project", "Analytics",
     "Prediction"],
    default_index=0)

# navigation with sidebar
if (selected == "About Project"):
    st.title("House Price Prediction with machine learning")
    
    st.text("")
    st.subheader("Problem Statement")
    multi_line5 = '''Berdasarkan data pada Badan Pusat Statistik (BPS) dalam Survei Sosial Ekonomi (Susenas) Tahun 2023 mencatat kesenjangan
    angka kebutuhan rumah (backlog) kepemilikan rumah sepanjang tahun 2023 turun menjadi 9,9 juta unit dari tahun sebelumnya yaitu 10,5 juta unit.
    Angka backlog kelayakan hunian juga mengalami penurunan signifikan dari 16,14 juta unit (2022) menjadi 14,84 juta unit pada tahun 2023. 
    Tren angka backlog kepemilikan rumah terus mengalami penurunan dari 12,75 juta unit pada tahun 2020 menjadi 12,72 unit di 2021.
    Angkanya berkurang lagi menjadi 10,51 juta unit pada tahun 2022 dan menjadi 9,95 juta unit di tahun 2023,” papar Direktur Jenderal 
    Perumahan Kementerian Pekerjaan Umum dan Perumahan Rakyat (PUPR), Iwan Suprijanto, dalam paparannya yang dikutip Rabu, 13 Desember 2023.
    '''
    st.markdown(f'<div style="text-align: justify;">{multi_line5}</div>', unsafe_allow_html=True)
    st.text("")
    img = Image.open("Resources/tabel_backlog.png")
    st.image(img, caption="Tabel backlog perumahan tahun 2023 bersumber dari BPS ")
    
    multi_line6 = '''Harga rumah dapat dipengaruhi oleh berbagai faktor seperti lokasi geografis, luas tanah, jumlah kamar, fasilitas di sekitar, dan banyak lagi.
    Analisis manual terhadap kombinasi variabel-variabel ini menjadi rumit dan sulit dilakukan secara akurat. Dengan memanfaatkan teknik data science, kita
    dapat mengidentifikasi pola dan hubungan yang kompleks di antara variabel-variabel ini untuk membuat prediksi harga yang lebih tepat.. 
    '''
    st.markdown(f'<div style="text-align: justify;">{multi_line6}</div>', unsafe_allow_html=True)
    
    st.text("")
    st.subheader("Tujuan Project")
    
    multi_line7 = '''Goals dari project akhir ini yaitu mengembangkan sebuah model machine learning yang dapat melakukan prediksi terhadap sebuah harga properti.
    Penggunaan teknik machine learning dalam proyek ini memungkinkan pengembangan model prediktif yang dapat "belajar" dari data historis. 
    Dengan memanfaatkan algoritma-algoritma seperti linear regresi, KNN, serta random forest, kita dapat meningkatkan akurasi prediksi dan menghasilkan model yang mampu 
    menyesuaikan diri dengan perubahan tren pasar. 
    '''
    st.markdown(f'<div style="text-align: justify;">{multi_line7}</div>', unsafe_allow_html=True)

if (selected == "Analytics"):
    tab1, tab2 = st.tabs(["Introduction","Visualization"])
    
    with tab1:
        st.header("Exploratory Data Analysis (EDA)")
        
        st.subheader('**Pendahuluan Umum :**')
        multi_line1 = '''"Dalam rangka menghadirkan analisis data yang komprehensif, kita akan memulai dengan menjelajahi dataset yang telah dikumpulkan. 
        Dataset ini merupakan kumpulan data yang relevan dengan tujuan proyek data science kita."'''
        st.markdown(f'<div style="text-align: justify;">{multi_line1}</div>', unsafe_allow_html=True)
        
        st.subheader('**Deskripsi Dataset :**')
        multi_line2 = '''Sebelum kita memasuki tahap analisis, mari kita terlebih dahulu memahami struktur dan karakteristik dari dataset yang akan kita gunakan.
        Dataset ini mencakup informasi seputar data ukuruan luas tanah, luas bangunan, jumlah kamar tidur, jumlah kamar mandi & garasi yang diharapkan dapat memberikan inshigt untuk melakukan pembuatan model prediksi."'''
        st.markdown(f'<div style="text-align: justify;">{multi_line2}</div>', unsafe_allow_html=True)
        
        st.subheader('**Sumber Data :**')
        multi_line3 = '''""Dataset yang digunakan dalam proyek ini diperoleh dari situs Kaggle.com pada link = https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah. 
        Keterpahaman terhadap sumber data sangat penting untuk memastikan validitas dan relevansi analisis yang akan kita lakukan."'''
        st.markdown(f'<div style="text-align: justify;">{multi_line3}</div>', unsafe_allow_html=True)
        
        st.text("")
        st.caption("**Dataset Harga Rumah :**")
        # import dataset
        st.caption("Tabel 1. Data sebelum pre processing")
        data_rumah = pd.read_csv("Resources/raw data/daftar_harga_rumah/data_rumah.csv")
        st.dataframe(data_rumah, hide_index=True)
        st.caption("Tabel 2. Data setelah pre processing")
        data = pd.read_csv("Resources/raw data/daftar_harga_rumah/harga_rumah.csv")
        st.dataframe(data, width=800, hide_index=True)
                
        st.write("Penjelasan keterangan setiap kolom :")
        st.markdown("- LB = Luas Bangunan")
        st.markdown("- LT = Luas Tanah")
        st.markdown("- KT = Kamar Tidur")
        st.markdown("- KM = Kamar Mandi")
        st.markdown("- GRS = Garasi")
        
        st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:20px;
        }
        </style>
        ''', unsafe_allow_html=True)

        st.subheader('**Tujuan Analisis :**')
        multi_line4 = '''"Analisis data yang efektif dimulai dengan pemahaman yang mendalam terhadap dataset. Dalam konteks ini, 
        kita akan menyelidiki dataset ini untuk melakukan suatu prediksi terhadap harga sebuah rumah dengan spesifikasi tertentu."'''
        st.markdown(f'<div style="text-align: justify;">{multi_line4}</div>', unsafe_allow_html=True)
        
    with tab2:
        st.caption("Tabel 3. Deskripsi data")
        st.dataframe(pd.read_csv("Resources/raw data/daftar_harga_rumah/analisas_deskriptif.csv"), width=800, hide_index=True)
        
        st.caption("Gambar 1. Data Info")
        img = Image.open("Resources/data_info.png")
        st.image(img, caption='Pengecekan tipe data dan nilai null pada data')
        
        st.caption("Gambar 2. Perbandingan harga dengan beberapa atribut feature")
        img = Image.open("Resources/perbandingan.png")
        st.image(img, caption='visualisasi data dengan regplot')
        
        col3, col4 = st.columns(2)        
        with col3:
            st.caption("Gambar 3. Analisa Univariat terhadap variabel luas tanah")
            img = Image.open("Resources/LT_analisis_univariat.png")
            st.image(img, caption='visualisasi dengan line plot dan boxplot')
        with col4:
            st.caption("Gambar 4. Analisa Univariat terhadap variabel luas bangunan")
            img = Image.open("Resources/LB_analisis_univariat.png")
            st.image(img, caption='visualisasi dengan line plot dan boxplot')
        
        col5, col6 = st.columns(2)
        with col5:
            st.caption("Gambar 5. Analisa Univariat terhadap variabel jumlah kamar tidur")
            img = Image.open("Resources/KT_analisis_univariat.png")
            st.image(img, caption='visualisasi dengan bar plot dan boxplot')
        with col6:
            st.caption("Gambar 6. Analisa Univariat terhadap variabel jumlah kamar mandi")
            img = Image.open("Resources/KM_analisis_univariat.png")
            st.image(img, caption='visualisasi dengan bar plot dan boxplot')
        
        col7, col8 = st.columns(2)
        with col7:
            st.caption("Gambar 7. Analisa Univariat terhadap variabel jumlah garasi")
            img = Image.open("Resources/GRS_analisis_univariat.png")
            st.image(img, caption='visualisasi dengan bar plot dan boxplot')   
            
        st.caption("Gambar 8. Persebaran data rumah(Pairplot)")
        img = Image.open("Resources/Analisa bivariat antara independent variabel dan dependent variabel.png")
        st.image(img)

if (selected == "Prediction"):
    
    # loading model
    house_price_predict_model = pickle.load(open('house_price_prediction.sav','rb'))

    # Title apps
    st.title('Prediksi Harga Rumah')

    # input user
    col1, col2 = st.columns(2)
    LB = col1.number_input(label = 'Masukan Luas Bangunan', min_value=0)
    LT = col2.number_input(label = 'Masukan Luas Tanah', min_value=0)
    KT = col1.number_input(label = 'Masukan  Jumlah Kamar Tidur', min_value=0)
    KM = col2.number_input(label = 'Masukan  Jumlah Kamar Mandi', min_value=0)
    GRS = col1.number_input(label = 'Masukan Jumlah Garasi', min_value=0)

    # load the train model
    with open('house_price_prediction.sav', 'rb') as rf:
        model = pickle.load(rf)
    
    # Prediction Function 
    def predict(LB, LT, KT, KM, GRS):
        
        # processing user input
        lists = [LB, LT, KT, KM, GRS]
        
        df = pd.DataFrame(lists).transpose()
        
        # making predictions using the train model
        prediction = model.predict(df)
        result = int(prediction)
        return result

    #prediction button
    button = st.button('Prediksi')
        
    # if button is pressed
    if button:
    # make prediction
        result = predict(LB, LT, KT, KM, GRS)
        st.success(f'Harga rumahnya sebesar Rp. {result*1000000}')
