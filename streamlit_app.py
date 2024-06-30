import streamlit as st 
import pandas as pd
import plotly.express as px 
import matplotlib.pyplot as plt
import requests
#from st_aggrid import AgGrid

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Iris Data Visualisation",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk mengubah warna sidebar
st.markdown(
    """
    <style>
    /* Mengubah warna sidebar */
    .css-1lcbmhc {
        background-color: #FFA500 !important; /* Oranye */
    }
    .css-18e3th9 {
        padding-top: 3rem !important;
    }
    .css-18ni7ap {
        padding: 1.5rem 1rem 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def main() : 
  st.header('Selamat Datang Streamlit Muh. Chaerul')

#-------------------------------------------------------------------------------------------------------------
  # 4 columns Metrics :
  st.subheader('Metrics Data')
  col1, col2, col3, col4 = st.columns(4)

# Menampilkan Metrics1
  with col1:
    st.metric(label="Jumlah Data", value="124", delta="12 %")
    
# Menampilkan Metrics2
  with col2:
    st.metric(label="Temperature", value="25 °C", delta="-1.2 °C")

# Menampilkan Metrics3
  with col3:
    st.metric(label="Selisih", value="30", delta="10 %")

# Menampilkan Metrics4
  with col4:
    st.metric(label="Selisih", value="30", delta="10 %")
  
#-------------------------------------------------------------------------------------------------------------
  #sidebar 
  sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
  sidebar_radio_button = st.sidebar.radio('Aplikasi Prediksi Harga Rumah',options=['Data House','Deskripsi Data','Prediction'])

   ###Tombol untuk memindahkan konten
  if st.sidebar.button("Tampilkan di Mainbar"):
     st.session_state['show_content'] = True
  else:
     st.session_state['show_content'] = False

# Pilihan halaman dengan tabs
    tab = st.sidebar.radio("Pilih halaman:", ["Iris Data", "Visualisasi", "Prediction"])

#-------------------------------------------------------------------------------------------------------------
  
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
  st.subheader('Menampilkan Input kalkulator Sederhana')
  num_input = st.number_input('Input Berapapun')
  st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))
  

    
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
  st.subheader('Menampilkan Expander')
  expander = st.expander("Klik Untuk Detail ")
  expander.write('Anda Telah Membuka Detail')




  #Menampilkan hasil di mainbar
  st.title("Mainbar")
  if 'show_content' in st.session_state and st.session_state['show_content']:
     st.write(f"Teks dari sidebar: {input_text}")
     st.write(f"Angka dari sidebar: {input_number}")
  else:
     st.write("Tidak ada konten untuk ditampilkan.")

    #sidebar 
  st.subheader('Menampilkan sidebar')
  with st.form("Data Diri"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

  # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
      st.write("slider", slider_val, "checkbox", checkbox_val)
  st.write("Outside the form")


  
  # Insert containers separated into tabs:
  tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
  tab1.write("this is tab 1")
  tab2.write("this is tab 2")

  # You can also use "with" notation:
  with tab1:
     st.radio("Select one:", [1, 2])






if __name__ == '__main__' : 
  main()
