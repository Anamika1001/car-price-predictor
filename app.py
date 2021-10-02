import streamlit as st
import pickle
import numpy as np

pipe=pickle.load(open('model.pkl','rb'))

st.title('Car Price Predictor')
selected_fuel_type=st.selectbox('Select Fuel Type',['Diesel','Petrol'])
selected_seller_type=st.selectbox('Select Seller Type',['Individual','Dealer'])
selected_transmission=st.selectbox('Select transmission Type',['Manual','Automatic'])
selected_owner=st.selectbox('Select owner',['First Owner','Second Owner','Third Owner','Fourth & Above Owner'])
engine=st.number_input('Enter Engine in cc')
max_power=st.number_input('Enter Max_Power in bhp')
purchase_year=st.number_input('Purchase Year')
brands=['Maruti', 'Hyundai', 'Mahindra', 'Tata', 'Honda', 'Ford', 'Toyota',
       'Chevrolet', 'Renault', 'Volkswagen', 'Nissan', 'Skoda', 'Datsun',
       'Mercedes-Benz', 'BMW', 'Fiat', 'Audi', 'Jeep', 'Mitsubishi', 'Volvo',
       'Jaguar', 'Isuzu', 'Ambassador', 'Force', 'Land', 'Kia', 'Daewoo', 'MG',
       'Ashok', 'Lexus', 'Opel']
selected_brands=st.selectbox('Select brand',brands)
if st.button('Predict Price'):
    input_query=np.array([[selected_fuel_type,selected_seller_type,selected_transmission,
    selected_owner,engine,max_power,(2020 - purchase_year),selected_brands]])
    price=pipe.predict(input_query)[0]
    st.header(f"Price should be somewhere {str(int(price))}")
