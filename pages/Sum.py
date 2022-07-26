import streamlit as st
from apps.Sum_App.sum import sum

st.title('Sum App')

a = st.number_input('Enter a:', step=1)
b = st.number_input('Enter b:', step=1)
result = sum(a, b)

st.header('Result: ' + str(result))
