# 🧹 Data Cleaning Otomatis — Web App

Aplikasi web berbasis **Streamlit** untuk membersihkan data CSV/Excel secara otomatis langsung dari browser — tanpa perlu install Python atau menjalankan script apapun.

---

## 📋 Deskripsi Project

Klien cukup buka link, upload file, dan langsung download hasilnya. Tidak perlu tau Python, tidak perlu install apapun.

```
Upload CSV/Excel  →  Otomatis dibersihkan  →  Download hasil
```

Ini adalah versi web app dari project **Data Cleaning & Export** yang sebelumnya hanya bisa dijalankan via terminal.

---

## ✨ Fitur

- ✅ Upload file **CSV** atau **Excel (.xlsx)**
- ✅ Tampilkan data mentah sebelum cleaning
- ✅ Deteksi dan tampilkan jumlah nilai kosong per kolom
- ✅ Cleaning otomatis — standarisasi huruf, tanggal, isi nilai kosong
- ✅ Tampilkan hasil setelah cleaning
- ✅ **Tombol download** hasil cleaning langsung dari browser

---

## 🧹 Proses Cleaning yang Dilakukan

| Masalah | Solusi |
|---|---|
| Huruf tidak konsisten (`kemeja`, `KEMEJA`) | Distandarisasi ke Title Case |
| Format tanggal berantakan | Dikonversi ke format `YYYY-MM-DD` |
| Nilai kosong di kolom qty | Diisi dengan rata-rata kolom |
| Nilai kosong di kolom harga | Diisi dengan rata-rata kolom |
| Baris tanpa nama produk / tanggal | Dihapus otomatis |

---

## 🗂️ Struktur File

```
Streamlit Project/
│
├── app.py        → Script utama web app
└── README.md
```

---

## 🧠 Konsep yang Digunakan

### Streamlit Components
```python
st.title()          # Judul halaman
st.write()          # Teks biasa
st.subheader()      # Sub judul
st.dataframe()      # Tampilkan tabel interaktif
st.success()        # Pesan sukses (warna hijau)
st.file_uploader()  # Komponen upload file
st.download_button() # Tombol download file
```

### Deteksi Tipe File
```python
if uploaded_file.name.endswith(".csv"):
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
```
Otomatis deteksi apakah file CSV atau Excel berdasarkan ekstensinya.

### Export ke CSV untuk Download
```python
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(label="⬇️ Download", data=csv, ...)
```
Konversi DataFrame ke bytes, lalu tampilkan sebagai tombol download di browser.

---

## 🚀 Cara Menjalankan

### Prasyarat
```bash
pip install streamlit pandas openpyxl
```

### Jalankan
```bash
streamlit run app.py
```

Browser akan terbuka otomatis di `localhost:8501`.

### Format File yang Didukung
- `.csv` — Comma Separated Values
- `.xlsx` — Microsoft Excel

### Struktur Kolom yang Diharapkan
File input sebaiknya memiliki kolom:
```
tanggal | nama_produk | kategori | qty | harga
```

---

## 💡 Contoh Tampilan

**Sebelum Cleaning:**
```
tanggal      nama_produk    kategori   qty    harga
2024-01-01   kemeja putih   pakaian    3      150000
2024/01/02   KEMEJA PUTIH   Pakaian    2      150000
03-01-2024   Celana Jeans   PAKAIAN    None   250000
```

**Setelah Cleaning:**
```
tanggal      nama_produk    kategori   qty    harga
2024-01-01   Kemeja Putih   Pakaian    3      150000
2024-01-04   Celana Jeans   Pakaian    4      250000
```

---

## ⚠️ Catatan & Keterbatasan

- **Kolom hardcoded** — proses cleaning saat ini hanya cocok untuk file dengan kolom `tanggal`, `nama_produk`, `kategori`, `qty`, `harga`. File dengan struktur kolom berbeda perlu penyesuaian
- **Strategi fillna rata-rata** — pendekatan sederhana, bisa dikembangkan dengan opsi lain
- **Berjalan lokal** — untuk diakses publik perlu di-deploy ke Streamlit Cloud

---

## 🔧 Kemungkinan Pengembangan

- [ ] Deploy ke **Streamlit Cloud** agar bisa diakses siapa saja via link
- [ ] Tambahkan deteksi kolom otomatis — tidak hardcoded
- [ ] Tambahkan pilihan strategi cleaning (hapus baris vs isi rata-rata)
- [ ] Tambahkan visualisasi data (grafik sebelum vs sesudah)
- [ ] Support export ke Excel selain CSV
- [ ] Tambahkan preview jumlah baris yang dihapus vs dipertahankan

---

## 🛠️ Library yang Digunakan

| Library | Versi | Fungsi |
|---|---|---|
| `streamlit` | 1.58.0 | Framework web app Python |
| `pandas` | 3.0.0 | Manipulasi dan cleaning data |
| `openpyxl` | 3.1.5 | Baca file Excel (.xlsx) |

---

## 💡 Tentang Streamlit

> Streamlit mengubah script Python biasa menjadi web app interaktif hanya dengan menambahkan beberapa baris kode — tanpa perlu belajar HTML, CSS, atau JavaScript.

---

## 👤 Author

Dibuat sebagai project portfolio Python — implementasi web app Data Cleaning dengan Streamlit.
