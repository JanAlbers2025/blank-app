import streamlit as st
import pandas as pd
import requests 
import mag4 as mg

st.title("My new app by JA")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# df = pd.read

city = 'London'
api_key = 'a4bdcb7161792c27f6e7f41968c0a911'  # this key is no longer valid, you need to produce your own for this to work --> done

url1 = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=3&appid={api_key}'
response1 = requests.get(url1)
lat = response1.json()[0]['lat']
lon = response1.json()[0]['lon']
print(f'response 1 status code is: {response1.status_code}')

st.selectbox('Select something:',('1','2','3'))
st.slider('Adjust by sliding')
age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)