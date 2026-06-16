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

    df["nama_produk"] = df["nama_produk"].str.title()
    df["kategori"] = df["kategori"].str.title()
    df["tanggal"] = pd.to_datetime(df["tanggal"], dayfirst=True, errors="coerce")
    df["qty"] = df["qty"].fillna(df["qty"].mean())
    df["harga"] = df["harga"].fillna(df["harga"].mean())
    df = df.dropna(subset=["nama_produk", "tanggal"])
    df = df.reset_index(drop=True)
    df["tanggal"] = df["tanggal"].dt.strftime("%Y-%m-%d")

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