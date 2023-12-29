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
    ["About Project", "Analysis",
     "Prediction"],
    default_index=0)

# navigation with sidebar

if (selected == "Analysis"):
    st.header("Exploratory Data Analysis (EDA)")
    
    st.subheader('**1. Pendahuluan Umum :**')
    multi_line1 = '''"Dalam rangka menghadirkan analisis data yang komprehensif, kita akan memulai dengan menjelajahi dataset yang telah dikumpulkan. 
    Dataset ini merupakan kumpulan data yang relevan dengan tujuan proyek data science kita."'''
    st.markdown(f'<div style="text-align: justify;">{multi_line1}</div>', unsafe_allow_html=True)
    
    st.subheader('**2. Deskripsi Dataset :**')
    multi_line2 = '''Sebelum kita memasuki tahap analisis, mari kita terlebih dahulu memahami struktur dan karakteristik dari dataset yang akan kita gunakan.
    Dataset ini mencakup informasi seputar data ukuruan luas tanah, luas bangunan, jumlah kamar tidur, jumlah kamar mandi & garasi yang diharapkan dapat memberikan inshigt untuk melakukan pembuatan model prediksi."'''
    st.markdown(f'<div style="text-align: justify;">{multi_line2}</div>', unsafe_allow_html=True)
    
    st.subheader('**3. Tujuan Analisis :**')
    multi_line3 = '''"Analisis data yang efektif dimulai dengan pemahaman yang mendalam terhadap dataset. Dalam konteks ini, 
    kita akan menyelidiki dataset ini untuk melakukan suatu prediksi terhadap harga sebuah rumah dengan spesifikasi tertentu."'''
    st.markdown(f'<div style="text-align: justify;">{multi_line3}</div>', unsafe_allow_html=True)

    st.subheader('**4. Sumber Data :**')
    multi_line4 = '''""Dataset yang digunakan dalam proyek ini diperoleh dari situs Kaggle.com pada link = https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah. 
    Keterpahaman terhadap sumber data sangat penting untuk memastikan validitas dan relevansi analisis yang akan kita lakukan."'''
    st.markdown(f'<div style="text-align: justify;">{multi_line4}</div>', unsafe_allow_html=True)
    
    st.text("")
    st.caption("**Dataset Harga Rumah :**")
    # import dataset
    data = pd.read_csv("Harga_Rumah.csv")
    st.dataframe(data, width=800)
    
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

    st.markdown("***Melakukan perbandingan harga dengan beberapa atribut feature***")
    img = Image.open("C:\\Users\\SIBGALAH ILHAM\\Downloads\\CSA_house_price_Prediction\\Resources\\perbandingan.png")
    st.image(img, caption='visualisasi data dengan regplot')
    
    st.markdown("***Melakukan Analisa Univariat terhadap variabel luas tanah***")
    img = Image.open("C:\\Users\\SIBGALAH ILHAM\\Downloads\\CSA_house_price_Prediction\\Resources\\LT_analisis_univariat.png")
    st.image(img, caption='visualisasi dengan kde dan boxplot')
    
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

