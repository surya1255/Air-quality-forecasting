# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:56:53 2023

@author: rupesh
"""

import streamlit as st
import pandas as pd
import pickle
import sklearn
from statsmodels.tsa.holtwinters import Holt

st.title('Carbon Dioxide (CO2) Prediction')
model = pickle.load(open(r'model.pkl','rb'))
                    

st.sidebar.header('User Input Parameters')

month = [st.sidebar.selectbox('month', ('Jan','Feb','Mar','April','May','Jun','July','Aug','Sep','Oct','Nov','Dec'))]
year = st.sidebar.selectbox('year',(2015,2016,2017,2018,2019,2020,2021,2022,2023,2024))


mth = 0
for i in month:
    if i=='Jan':
        mth=1
    elif i=='Feb':
        mth=2
    elif i=='Mar':
        mth=3
    elif i=='April':
        mth=4
    elif i=='May':
        mth=5
    elif i=='June':
         mth=6
    elif i=='July':
         mth=7
    elif i=='Aug':
          mth=8
    elif i=='Sep':
          mth=9
    elif i=='Oct':
          mth=10
    elif i=='Nov':
          mth=11
    elif i=='Dec':
        mth=12
        
prediction = model.predict(pd.datetime(year,mth,1))
data = pd.DataFrame({'Month':month,'Year':year,'The carbon dioxide emission':prediction})
st.write(data)




























