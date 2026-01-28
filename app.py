import streamlit as st
import pandas as pd
import joblib


model = joblib.load("model.joblib")


st.title("🎓 Prediksi Nilai TKA Siswa")
st.write("Masukkan data siswa untuk memprediksi nilai TKA")


jam_belajar = st.slider(
    "Jam belajar per hari",
    min_value=0,
    max_value=24,
    value=4
)

kehadiran = st.slider(
    "🧾 Persentase kehadiran (%)",
    min_value=0,
    max_value=100,
    value=80
)


bimbel = st.radio(
    "ikut bimbel",
    ["ya", "tidak"],
    horizontal=True
)


if st.button("Prediksi Nilai"):
    data_input = pd.DataFrame(
        [[jam_belajar, kehadiran, bimbel]],
        columns=[
            "jam_belajar_per_hari",
            "persen_kehadiran",
            "bimbel"
        ]
    )

    hasil = model.predict(data_input)[0]
    hasil = max(0, min(100, hasil))  # batasi 0–100

    st.balloons()
    st.success(f"📊 Prediksi Nilai TKA: **{hasil:.0f}**")
