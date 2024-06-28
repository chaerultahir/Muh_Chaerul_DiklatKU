import streamlit as st 
import pandas as pd 
#import requests
#from st_aggrid import AgGrid


#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def main() : 
  st.header('Halaman Streamlit Muh. Chaerul')
  st.subheader('Menampilkan Tabel House')
  st.write('yang bersumber dari tabel house_clean.csv')
  st.markdown('# Data Tabel House')
  st.dataframe(house)

  st.write('Metrics')
  st.metric(label="Temperature", value="70 °F", delta="-1.2 °F")
  



if __name__ == '__main__' : 
  main()
