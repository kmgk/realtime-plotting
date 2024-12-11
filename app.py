import streamlit as st
import pandas as pd
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

url = "https://raw.githubusercontent.com/kmgk/realtime-plotting/refs/heads/main/02_CBA9_flowpath5_sample1_Tscan_heating_9T_probe1mA.txt"
df = pd.read_csv(url, sep='\t')

st.title('リアルタイムプロット')
st.write(now.strftime('%H:%M:%S'))
st.scatter_chart(df, x=" _temp_A ", y=" _diff ")
st.scatter_chart(df, x=' _time ', y=" _temp_A ")
st.scatter_chart(df, x=" _time ", y=" _diff ")
# Index(['_sqrt_TW_freq ', ' _amp ', ' _theta ', ' _DCV ', ' _time ',
#        ' _sensor_temp ', ' _diff ', ' _tesla ', ' _temp_A ', ' _temp_B ', ' '],