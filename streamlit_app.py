import streamlit as st
import pandas as pd 
st.title('🎈 MY FRIST PROJECT')

st.write('LETS GO!')

with st.expander("DATA"):
  st.write('**OUR DATA**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

with st.expander("Visualization"):
  st.scatter_chart(data=df , x='bill_length_mm' , y='bill_depth_mm', color='species')

with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Torgersen', 'Dream', ' Biscoe'))
  bill_length_mm = st.slider("bill_length_mm", 32.1, 59.6, 43.9)
