import streamlit as st
import pandas as pd

#untuk bikin judul aplikasi nya
st.title("🧹 Data Cleaning Otomatis")
st.write("Upload file CSV lo, dan gw akan bersihin datanya secara otomatis!")

#untuk upload file
uploaded_file = st.file_uploader("Pilih file CSV atau Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    #baca file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file, engine="openpyxl")

    #ini bagian untuk baca file pas belum di cleaning (start)
    st.subheader("📋 Data Sebelum Cleaning")
    st.dataframe(df)
    st.write(f"Total baris: {len(df)}")
    st.write(f"Nilai kosong per kolom:")
    st.write(df.isnull().sum())
    #ini bagian untuk baca file pas belum di cleaning (end)

    #ini bagian pas udh selesai di cleaning (start)
    st.subheader("Proses Cleaning")

    kolom_teks = df.select_dtypes(include=['object']).columns

    for col in kolom_teks:
        df[col] = df[col].fillna("Tidak ada data!")
        df[col] = df[col].str.strip().str.title()


    kolom_number = df.select_dtypes(include=['number']).columns

    for col in kolom_number:
        df[col] = df[col].fillna(df[col].mean())

    df = df.drop_duplicates()

    
    st.success("✅ Data Berhasil dibersihkan")

    st.subheader("📊 Data Setelah Cleaning")
    st.dataframe(df)
    st.write(f"Total baris setelah cleaning: {len(df)}")

    #untuk bikin tombol download
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download Hasil Cleaning (CSV)",
        data=csv,
        file_name="hasil_cleaning.csv",
        mime="text/csv"
    )
    #ini bagian pas udh selesai di cleaning (end)