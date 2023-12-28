# import package
import pickle
import streamlit as st
import pandas as pd
import numpy as numpy


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

def predict(LB, LT, KT, KM, GRS):
    
    # processing user input
    lists = [LB, LT, KT, KM, GRS]
    
    df = pd.DataFrame(lists).transpose()
    # making predictions using the train model
    prediction = model.predict(df)
    result = int(prediction)
    return result

#prediction
button = st.button('Prediksi')
    
# if button is pressed
if button:
# make prediction
    result = predict(LB, LT, KT, KM, GRS)
    st.success(f'Harga rumahnya sebesar Rp. {result*1000000}')

