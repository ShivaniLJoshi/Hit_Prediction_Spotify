# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:46:36 2021

@author: Shivani Joshi
"""





# Importing all necessary libraries
import streamlit as st
import pickle
#import pandas as pd
import numpy as np
import gzip

# Loading the saved Model
model = pickle.load(gzip.open("final_model.pkl"))



def predict_hit(features):
    
    features = np.array(features).astype(np.float64).reshape(1, -1)
    prediction = model.predict(features)
    print(prediction)

    return prediction


def main():
    st.title("Spotify Hit Predictor")
    html_temp = html_temp = """
        <div style = "background-color: tomato; padding: 10px;">
            <center><h1>SPOTIFY HIT PREDICTION</h1></center>
        </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    danceability =   st.text_input("danceability", "Type Here")
    energy =         st.text_input("energy", "Type Here")
    key =            st.text_input("key", "Type Here")
    loudness =       st.text_input("loudness", "Type Here")
    mode =           st.text_input("mode", "Type Here")
    speechiness =    st.text_input("speechiness", "Type Here")
    acousticness =   st.text_input("acousticness", "Type Here")
    instrumentalness = st.text_input("instrumentalness", "Type Here")
    liveness =       st.text_input("liveness", "Type Here")
    valence =        st.text_input("valence", "Type Here")
    tempo =          st.text_input("tempo", "Type Here")
    duration_ms =    st.text_input("duration_ms ", "Type Here")
    time_signature = st.text_input("time_signature", "Type Here")
    chorus_hit =     st.text_input("chorus_hit", "Type Here")
    sections =       st.text_input("sections ", "Type Here")
    result = ""
    if st.button("Predict"):
        features = [danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature,chorus_hit,sections]
        result = predict_hit(features)
    st.success('The output is {}'.format(result))

if __name__ == '__main__':
    main()