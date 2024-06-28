import streamlit as st 
import pandas as pd 
#import requests
#from st_aggrid import AgGrid


#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def main() : 
  st.header('Halaman Streamlit Muh. Chaerul')
  
  st.write('Metrics')
  st.metric(label="Temperature", value="25 °C", delta="-1.2 °C")
  
  st.subheader('Menampilkan Tabel House')
  st.write('yang bersumber dari tabel house_clean.csv')
  st.markdown('# Data Tabel House')
  st.dataframe(house)


  



if __name__ == '__main__' : 
  main()
