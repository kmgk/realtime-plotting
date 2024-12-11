import streamlit as st

st.title('streamlit Tutorial')
input_num = st.number_input('Input a number', value=0)

result = input_num ** 2
st.write('Result: ', result)
