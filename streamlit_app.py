import streamlit as st

st.title("Hola Mundo")
st.write("Esta es la primera Web")
nombre = st.text_input("Escribre tu nombre: ")
if nombre:
    st.write(f"!Hola , {nombre}")

''' Comando para lanzar streamlit run nombrefichero.py'''    

col1,col2,col3 = st.columns(3)

with col1:
    st.title("Hola Mundo 1")
    st.write("Esta es la primera Web 1")

with col2:
    st.title("Hola Mundo 2")
    st.write("Esta es la primera Web 2")

with col3:
    st.title("Hola Mundo 3")
    st.write("Esta es la primera Web ")    
