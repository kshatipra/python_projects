#widgets:slider
import streamlit as st
import pandas as pd 
import numpy as np

st.subheader('SLIDER')
st.slider('I am a slider')

#slider value is then squared
st.subheader('squaring at every value of x')
x = st.slider('x')
st.write(x, 'square is',  (x*x))

#use session state and keys
st.subheader("Session state and key")
st.text_input("Your name:", key = "name")
st.write(st.session_state.name)

#Use checkbox to show and hide data

st.subheader("Chekboxes to show and hide data")
if st.checkbox('Show DataFrame'):
    charts = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )
    charts

#Select boxes
st.subheader("Select boxes")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

#display dataframe
df

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option



