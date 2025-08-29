import streamlit as st

def temperatureConvert():
    st.header("Konversi Suhu")

    opsi_satuan = ["Celcius", "Reamur", "Fahrenheit"]
    satuan_awal = st.selectbox("Pilih satuan input", opsi_satuan, key="satuan")
    nilai = st.number_input(f"Masukkan suhu dalam {satuan_awal}", value=0, step=1, key="nilai")

    if st.button("Konversi", key="konversi"):
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
