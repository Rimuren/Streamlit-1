import streamlit as st
import pandas as pd

def fibonacciSequence():
    st.header("Deret Fibonacci")

    n = st.number_input(
        "Masukkan jumlah bilangan Fibonacci (Max 100)",
        min_value=1,
        max_value=100,
        step=1,
        key="fibo_n"
    )

    if st.button("Generate", key="generate"):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])

        df = pd.DataFrame({
            "Index": list(range(n)),
            "Nilai Fibonacci": fib[:n]
        })

        st.write(f"Deret Fibonacci ({n} bilangan):")
        st.table(df)
