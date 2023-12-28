# import package
import pickle
import streamlit as st

# loading model
house_price_predict_model = pickle.load(open('house_price_prediction.sav','rb'))

# Title apps
st.title('House Prediction')

# input user
LB = st.text_input('Masukan Luas Bangunan')
LT = st.text_input('Masukan Luas Tanah')
KT = st.text_input('Masukan  Jumlah Kamar Tidur')
KM = st.text_input('Masukan  Jumlah Kamar Mandi')
GRS = st.text_input('Masukan Jumlah Garasi')

# prediction
house_price_predict = ''

# button
if st.button('Prediksi Harga'):
    house_price = house_price_predict_model.predict([[LB, LT, KT, KM, GRS]])

# function
    if(house_price[0] == 1):
        house_price_predict = 'test'
    st.success