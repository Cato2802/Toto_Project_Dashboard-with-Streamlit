import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header('Dashboard')
plot_data = st.sidebar.multiselect('Chọn dữ liệu', ['Giá mở cửa', 'Giá đóng cửa'], ['Giá mở cửa', 'Giá đóng cửa'])
st.sidebar.subheader('Thiết lập màu cho biểu đồ nhiệt độ')
time_hist_color = st.sidebar.selectbox('Màu theo', ('Giá mở cửa', 'Giá đóng cửa'))

st.sidebar.subheader('Thiết lập biểu đồ đường')
plot_height = st.sidebar.slider('Chọn chiều cao của biểu đồ', 200, 500, 250)

# Hàng A
st.markdown('### Các Chỉ Số')
col1, col2, col3 = st.columns(3)
col1.metric("Giá FPT", "60,000 VND", "1,000 VND")
col2.metric("Thay đổi", "0.5%", "-2%")
col3.metric("Khối lượng", "2 triệu", "3 triệu")

# Hàng B
fpt_stock = pd.read_csv('https://github.com/Cato2802/Toto_Project_Dashboard-with-Streamlit/blob/main/Du%CC%9B%CC%83%20lie%CC%A3%CC%82u%20Li%CC%A3ch%20su%CC%9B%CC%89%20FPT.csv', parse_dates=['Ngày'])

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Biểu đồ đường cho Giá mở cửa và Giá đóng cửa/tháng')
    st.line_chart(fpt_stock.set_index('Ngày')[['Giá mở cửa', 'Giá đóng cửa']], height=plot_height)

# Hàng C
st.markdown('### Biểu đồ đường/ngày')
st.line_chart(fpt_stock, x='Ngày', y=plot_data, height=plot_height)

