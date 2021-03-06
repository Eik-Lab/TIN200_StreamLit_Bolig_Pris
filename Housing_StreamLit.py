#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:40:22 2021

@author: uzaaft
"""
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from joblib import dump, load

st.write("""
         Nettside for å predikere Boligpriser  
         Dataen er fra Kaggle: https://www.kaggle.com/camnugent/california-housing-prices 
         """)
         
train_data = pd.read_csv("./California_Housing_Data/train_data.csv")
test_data = pd.read_csv("./California_Housing_Data/test_data.csv")
full_data = pd.read_csv("./California_Housing_Data/full_data.csv")


X = full_data
Y = X.pop("median_house_value")

st.sidebar.header("Input Verdier")

def verdier_fra_bruker():
    longitude = st.sidebar.slider('Longitude', float(full_data.longitude.min()), float(full_data.longitude.max()), float(full_data.longitude.mean()))
    latitude = st.sidebar.slider('Latitude', float(full_data.latitude.min()), float(full_data.latitude.max()), float(full_data.latitude.mean()))
    housing_median_age = st.sidebar.slider('Housing Median Age', float(full_data.housing_median_age.min()), float(full_data.housing_median_age.max()), float(full_data.housing_median_age.mean()))
    total_rooms = st.sidebar.slider('Total Rooms', float(full_data.total_rooms.min()), float(full_data.total_rooms.max()), float(full_data.total_rooms.mean()))
    total_bedrooms = st.sidebar.slider('Total Bedrooms', float(full_data.total_bedrooms.min()), float(full_data.total_bedrooms.max()), float(full_data.total_bedrooms.mean()))
    population = st.sidebar.slider('Population', float(full_data.population.min()), float(full_data.population.max()), float(full_data.population.mean()))
    households = st.sidebar.slider('Households', float(full_data.households.min()), float(full_data.households.max()), float(full_data.households.mean()))
    median_income = st.sidebar.slider('Median Income', float(full_data.median_income.min()), float(full_data.median_income.max()), float(full_data.median_income.mean()))
    
    data = {'Longitude': longitude,
            'Latitude': latitude,
            'Housing Median Age': housing_median_age,
            'Total Rooms': total_rooms,
            'Total Bedrooms': total_bedrooms,
            'Population': population,
            'Households': households,
            'Median Income': median_income}
    features = pd.DataFrame(data, index = [0])
    return features
    
input_data = verdier_fra_bruker()

st.write("Input verdier")
st.table(input_data)
st.write("---")
    
    
X = X.drop("Unnamed: 0", axis=1)
    
    
model = RandomForestRegressor()
model.fit(X,Y)


prediksjon = model.predict(input_data)
prediksjon = f"{prediksjon:,d }"
    
st.header("Prediksjon")
st.write("Basert på dine tall, gjetter modellen at bolig prisen er %s US dollar" % prediksjon)

    
    
    
    
    
    
    
    
    
    
    
    