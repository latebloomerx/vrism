import streamlit as st
import time

# 1. Mengatur konfigurasi halaman
st.set_page_config(page_title="Special for You 💖", page_icon="💌", layout="centered")

# 2. Menambahkan sedikit CSS biar font-nya lebih cantik dan berwarna
st.markdown("""
    <style>
    .judul {
        font-size: 35px !important;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .teks-manis {
        font-size: 20px;
        color: #FF748B;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Membuat sistem halaman (Session State)
if 'halaman' not in st.session_state:
    st.session_state.halaman = 1

def lanjut():
    st.session_state.halaman += 1

# ==========================================
# HALAMAN 1: HALAMAN PEMBUKA
# ==========================================
if st.session_state.halaman == 1:
    st.markdown('<p class="judul">Haloooo! 👋</p>', unsafe_allow_html=True)
    
    # Memasukkan GIF Lucu (Bisa diganti URL-nya)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzRzajh6Z3BwY3ZqYnU3aDdnZzZ6bWZ1b3QzbWp3c29vZG1qZzF0dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L1QMTl9ggmYGoCu7oj/giphy.gif", use_column_width=True)
    
    st.markdown('<p class="teks-manis">Aku punya sesuatu nih buat kamu, coba dicek ya...</p>', unsafe_allow_html=True)
    
    # Tombol ditaruh di tengah
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("Buka Suratnya 💌", on_click=lanjut, use_container_width=True)

# ==========================================
# HALAMAN 2: PESAN UTAMA
# ==========================================
elif st.session_state.halaman == 2:
    # Efek dramatis loading sebentar
    with st.spinner("Membuka amplop..."):
        time.sleep(2) # Jeda 2 detik biar deg-degan
        
    st.markdown('<p class="judul">Cuma mau bilang...</p>', unsafe_allow_html=True)
    
    st.success("Makasih yaa udah selalu ada dan jadi alasan aku buat senyum akhir-akhir ini. You make my days so much brighter! ✨")
    st.info("Jangan lupa makan yang teratur, kurang-kurangin begadangnya, dan tetep semangat ya!")
    
    # GIF Berpelukan/Lucu
    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", use_column_width=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("Ada satu lagi nih 👉", on_click=lanjut, use_container_width=True)

# ==========================================
# HALAMAN 3: AJAKAN / CLOSING
# ==========================================
elif st.session_state.halaman == 3:
    st.markdown('<p class="judul">Btw...</p>', unsafe_allow_html=True)
    st.write("Weekend ini sibuk nggak? Jalan yuk? Makan es krim kek, atau nyari angin ajaa.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Ayok gas! 🍦❤️", use_container_width=True):
            st.balloons()
            st.success("Yeayyy! Nanti aku chat buat janjian jamnya ya. See you! 🥰")
            st.image("https://media.giphy.com/media/ibolLe3mO2ZqqsEpOT/giphy.gif", use_column_width=True) # GIF Happy
            
    with col2:
        if st.button("Hmm, lagi sibuk/mager 🥺", use_container_width=True):
            st.snow()
            st.error("Yahh... yaudah deh gapapa, nanti kapan-kapan aja yaa! Tetep semangat! ✨")