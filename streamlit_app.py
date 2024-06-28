import streamlit as st 
import pandas as pd
import plotly.express as px 
import matplotlib.pyplot as plt
import requests
#from st_aggrid import AgGrid

#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def main() : 
  st.header('Halaman Streamlit Muh. Chaerul')
  
  # Menampilkan Metrics
  st.write('Metrics')
  st.metric(label="Temperature", value="25 °C", delta="-1.2 °C")
  
  # Menampilkan Tabel
  st.subheader('Menampilkan Tabel House')
  st.write('yang bersumber dari tabel house_clean.csv')
  st.markdown('# Data Tabel House')
  st.dataframe(house)

  #matplotlib chart 
  st.subheader('Menampilkan Chart')
  fig,ax = plt.subplots()
  plt.scatter(house['bedrooms'],house['price'])
  st.pyplot(fig)
  plotly_fig = px.scatter(house['bedrooms'],house['price'])
  st.plotly_chart(plotly_fig)
  
  # Membuat Button
  st.subheader('Menampilkan Button')
  click_me_btn = st.button('Click Me')
  st.write(click_me_btn) #Return True kalo di Click 
  check_btn = st.checkbox('Klik Jika Setuju')
  if check_btn :
    st.write('Anda Setuju')
    
  # Membuat Radio Button
  st.subheader('Menampilkan Radio Button')
  radio_button= st.radio('Choose below',[x for x in range(1,3)])
  st.write('Anda Memilih',radio_button)
    
  #slider 
  st.subheader('Menampilkan Slider')
  age_slider = st.slider('Berapa Usia Anda',0,100)
  st.write('Usia Anda',age_slider)
    
  #Input (Typing)
  st.subheader('Menampilkan kalkulator Sederhana')
  num_input = st.number_input('Input Berapapun')
  st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))
  



  
  #sidebar 
  sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
  sidebar_radio_button = st.sidebar.radio('Pilih Menu',options=['A','B','C'])
    
  #columns :
  st.subheader('Menampilkan gambar pada 3 kolom')
  col1, col2, col3 = st.columns(3)

  with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
  #atau dengan assignment 
  image_col1 = col1.image("https://static.streamlit.io/examples/cat.jpg")

  with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

  with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
  #expander 
  #dengan with atau dengan assignment 
  expander = st.expander("Klik Untuk Detail ")
  expander.write('Anda Telah Membuka Detail')





  

if __name__ == '__main__' : 
  main()
