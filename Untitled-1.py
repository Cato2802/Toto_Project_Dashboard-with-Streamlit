import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header('Dashboard')
plot_data = st.sidebar.multiselect('Select data', ['open', 'close'], ['open', 'close'])
st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('open', 'close'))

st.sidebar.subheader('Line chart parameters')
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("USD/VND", "23,667 VND", "1.2 VND")
col2.metric("Change", "0.2%", "-8%")
col3.metric("Volume", "1 million", "4 million")

# Row B
usd_vnd = pd.read_csv('https://raw.githubusercontent.com/Cato2802/Toto_dashboard/main/D%E1%BB%AF%20li%E1%BB%87u%20L%E1%BB%8Bch%20s%E1%BB%AD%20USD_VND%20(1).csv', parse_dates=['date'])

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Line chart for Open and Close/month')
    st.line_chart(usd_vnd.set_index('date')[['open', 'close']], height=plot_height)

# Row C
st.markdown('### Line chart/Day')
st.line_chart(usd_vnd, x='date', y=plot_data, height=plot_height)


###If you want to run the Streamlit dictionary: Open cmd, Navigate to the code file directory using 'cd', Enter the command 'streamlit run Untitled-1.py'.
