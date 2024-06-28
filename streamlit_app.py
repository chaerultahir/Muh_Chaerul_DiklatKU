import streamlit as st

def main() : 
  st.header('Assalamualaikum Wr Wb')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')
  st.write('Rumus ini hanya digunakan dalam perhitungan sisi pada segita siku-siku')

if __name__ == '__main__':
    main()


