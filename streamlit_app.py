
import streamlit as st 

def main() : 
  st.header('Assalamualaikum Wr. Wb.')
  st.subheader('Selamat datang pada Web Aplikasi kami....')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

if __name__ == '__main__' : 
  main()
