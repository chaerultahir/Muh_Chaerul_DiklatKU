import streamlit as st 
import pandas as pd 
#import requests
#from st_aggrid import AgGrid


#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def main() : 
  st.header('Halaman Streamlit Muh. Chaerul')
  st.subheader('This is Subheader')
  st.markdown('# Data Tabel Housse')
  st.dataframe(house)
  



if __name__ == '__main__' : 
  main()
