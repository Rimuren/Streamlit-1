import streamlit as st

st.title("🧮 Aplikasi Multi Fungsi dengan Streamlit")

# Membuat tab
tab1, tab2, tab3 = st.tabs(["Kalkulator", "Konversi Suhu", "Deret Fibonacci"])

# =========================
# TAB 1: Kalkulator
# =========================
with tab1:
    st.header("Kalkulator Sederhana")
    a = st.number_input("Masukkan angka pertama", value=0.0)
    b = st.number_input("Masukkan angka kedua", value=0.0)
    operator = st.selectbox("Pilih Operator", ["+", "-", "×", "÷"])

    if st.button("Hitung"):
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

# =========================
# TAB 2: Konversi Suhu
# =========================
with tab2:
    st.header("Konversi Suhu")

    opsi_satuan = ["Celcius", "Reamur", "Fahrenheit"]
    satuan_awal = st.selectbox("Pilih satuan input", opsi_satuan)
    nilai = st.number_input(f"Masukkan suhu dalam {satuan_awal}", value=0.0)

    if st.button("Konversi"):
        if satuan_awal == "Celcius":
            r = (4/5) * nilai
            f = (9/5) * nilai + 32
            st.write(f"{nilai} °C = {r} °R")
            st.write(f"{nilai} °C = {f} °F")

        elif satuan_awal == "Reamur":
            c = (5/4) * nilai
            f = (9/4) * nilai + 32
            st.write(f"{nilai} °R = {c} °C")
            st.write(f"{nilai} °R = {f} °F")

        elif satuan_awal == "Fahrenheit":
            c = (5/9) * (nilai - 32)
            r = (4/9) * (nilai - 32)
            st.write(f"{nilai} °F = {c} °C")
            st.write(f"{nilai} °F = {r} °R")

# =========================
# TAB 3: Deret Fibonacci
# =========================
with tab3:
    st.header("Deret Fibonacci")

    n = st.number_input("Masukkan jumlah bilangan Fibonacci", min_value=1, max_value=100, step=1)

    if st.button("Generate"):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])

        st.write(f"Deret Fibonacci ({n} bilangan):")
        st.write(fib[:n])
