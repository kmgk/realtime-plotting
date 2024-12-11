import streamlit as st
import pandas as pd

url = "https://raw.githubusercontent.com/kmgk/realtime-plotting/refs/heads/main/02_CBA9_flowpath5_sample1_Tscan_heating_9T_probe1mA.txt"
df = pd.read_csv(url, sep='\t')
st.title('streamlit Tutorial')
input_num = st.number_input('Input a number', value=0)

result = input_num ** 2
st.write('Result: ', result)

st.line_chart(df.filter(items=[' _amp ']))
st.scatter_chart(df, x=" _temp_A ", y=" _diff ")