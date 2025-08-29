import streamlit as st

from page.calculator import calculator
from page.fibonacciSequence import fibonacciSequence
from page.temperatureConvert import temperatureConvert

st.title("🧮 Aplikasi dengan Streamlit")

# Tab
tab1, tab2, tab3 = st.tabs(["Kalkulator", "Konversi Suhu", "Deret Fibonacci"])

with tab1:
    calculator()

with tab2:
    temperatureConvert()

with tab3:
    fibonacciSequence()

