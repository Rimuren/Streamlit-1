import streamlit as st

def calculator():
    st.header("Kalkulator Sederhana")
    a = st.number_input("Masukkan angka pertama", value=0, step=1, key="a")
    b = st.number_input("Masukkan angka kedua", value=0, step=1, key="b")
    operator = st.selectbox("Pilih Operator", ["+", "-", "×", "÷"], key="operator")

    if st.button("Hitung", key="hitung"):
        if operator == "+":
            hasil = a + b
        elif operator == "-":
            hasil = a - b
        elif operator == "×":
            hasil = a * b
        elif operator == "÷":
            hasil = "Tidak bisa dibagi 0" if b == 0 else a / b
        else:
            hasil = "Operator tidak dikenali"

        st.success(f"Hasil: {hasil}")
