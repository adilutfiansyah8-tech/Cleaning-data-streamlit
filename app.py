import streamlit as st
import pandas as pd
import io

st.title("🧹 Data Cleaning Otomatis")
st.write("Upload file CSV lo, dan gw akan bersihin datanya secara otomatis!")

uploaded_file = st.file_uploader("Pilih file CSV atau Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        # Baca dulu tanpa header untuk deteksi baris yang benar
        df_temp = pd.read_excel(uploaded_file, engine="openpyxl", header=None)
        
        header_row = 0
        for i in range(min(5, len(df_temp))):
            non_null_count = df_temp.iloc[i].notna().sum()
            if non_null_count > 1:
                header_row = i
                break
        
        uploaded_file.seek(0)
        df = pd.read_excel(uploaded_file, engine="openpyxl", header=header_row)

    st.subheader("📋 Data Sebelum Cleaning")
    st.dataframe(df)
    st.write(f"Total baris: {len(df)}")
    st.write("Nilai kosong per kolom:")
    st.write(df.isnull().sum())

    st.subheader("Proses Cleaning")
    kolom_teks = df.select_dtypes(include=['object']).columns
    for col in kolom_teks:
        df[col] = df[col].str.strip().str.title()
    
    kolom_number = df.select_dtypes(include=['number']).columns
    for col in kolom_number:
        df[col] = df[col].fillna(df[col].mean())
    
    df = df.drop_duplicates()
    df = df.dropna()

    st.success("✅ Data Berhasil dibersihkan")
    st.subheader("📊 Data Setelah Cleaning")
    st.dataframe(df)
    st.write(f"Total baris setelah cleaning: {len(df)}")

    st.subheader("⬇️ Download Hasil")
    col1, col2 = st.columns(2)
    
    with col1:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📄 Download CSV",
            data=csv,
            file_name="hasil_cleaning.csv",
            mime="text/csv"
        )
    
    with col2:
        buffer = io.BytesIO()
        df.to_excel(buffer, index=False, engine="openpyxl")
        st.download_button(
            label="📊 Download Excel",
            data=buffer.getvalue(),
            file_name="hasil_cleaning.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
