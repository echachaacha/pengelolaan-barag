import streamlit as st
import pandas as pd

# Judul Aplikasi
st.title("Aplikasi Pengelolaan Barang di Agen")

# Formulir untuk Menambahkan Barang
st.header("Tambah Barang Baru")
nama_barang = st.text_input("Nama Barang")
kategori = st.selectbox("Kategori", ["Elektronik", "Pakaian", "Makanan", "Lainnya"])
jumlah = st.number_input("Jumlah", min_value=1, step=1)
harga = st.number_input("Harga per Unit", min_value=0.0, step=0.01)

# Inisialisasi DataFrame jika tidak ada
if 'data_barang' not in st.session_state:
    st.session_state.data_barang = pd.DataFrame(columns=["Nama Barang", "Kategori", "Jumlah", "Harga per Unit"])

# Tombol untuk menambahkan barang
if st.button("Tambah Barang"):
    if nama_barang and kategori and jumlah and harga:
        # Tambahkan barang ke DataFrame
        new_data = pd.DataFrame({"Nama Barang": [nama_barang], "Kategori": [kategori], "Jumlah": [jumlah], "Harga per Unit": [harga]})
        st.session_state.data_barang = pd.concat([st.session_state.data_barang, new_data], ignore_index=True)
        st.success(f"Barang '{nama_barang}' berhasil ditambahkan!")
    else:
        st.error("Harap mengisi semua bidang input!")

# Menampilkan Data Barang
st.header("Daftar Barang")
st.table(st.session_state.data_barang)

# Menghitung Total Nilai Barang
st.header("Total Nilai Barang")
total_nilai = (st.session_state.data_barang["Jumlah"] * st.session_state.data_barang["Harga per Unit"]).sum()
st.write(f"Total nilai semua barang: Rp{total_nilai:,}")

# Pencarian Barang
st.header("Cari Barang")
search_term = st.text_input("Masukkan nama barang atau kategori")
if search_term:
    search_results = st.session_state.data_barang[st.session_state.data_barang.apply(lambda row: search_term.lower() in row.astype(str).str.lower().tolist(), axis=1)]
    st.table(search_results)
    if search_results.empty:
        st.write("Tidak ada barang yang ditemukan.")
