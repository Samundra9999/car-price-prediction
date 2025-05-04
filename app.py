import streamlit as st
import pickle
import pandas as pd
import time

with open('linearRegModel.pkl', 'rb') as f:
    model = pickle.load(f)

data = pd.read_csv('final_car_data.csv')

model_list = sorted(data['model'].unique())
year = sorted(data['year'].unique(),reverse=True)
transmission = sorted(data['transmission'].unique())
fuel = sorted(data['fuelType'].unique())





st.header('Car Price Prediction')
model_name = st.selectbox('Model Name',model_list)
year = st.selectbox('Year of Manufacture',year)
mileage = st.number_input('Enter how far the car travels', min_value=1.0, step=1.0,max_value=63000.0)
transmission = st.selectbox('Transmission',transmission)
fuel = st.selectbox('Fuel Type',fuel)
mpg = st.number_input('mileage per gallon',min_value=35.0,step=1.0,max_value=80.0)
enginesize = st.number_input('Engine Size',min_value=1.0,step=0.1,max_value=2.3)

if st.button('Predict Price'):

    input_data = [[model, year,transmission,mileage,fuel,mpg,enginesize]]
    
    price = model.predict(pd.DataFrame(input_data,columns=['model','year','transmission','mileage','fuelType','mpg','engineSize']))

    with st.spinner('Predicting...'):

        time.sleep(3)
        st.success(f"Predicted Price: ${price[0]:,.0f}")
