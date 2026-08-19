import streamlit as st

# Mengatur tampilan halaman
st.set_page_config(page_title="Pop It Spesial 🫧", page_icon="💖", layout="centered")

# Sedikit CSS biar rapi
st.markdown("""
    <style>
    .judul {
        font-size: 30px !important;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
    }
    .instruksi {
        text-align: center;
        color: #555555;
        font-size: 18px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="judul">Main Pop It Dulu Yuk! 🫧</p>', unsafe_allow_html=True)
st.markdown('<p class="instruksi">Pecahin semua gelembung di bawah ini buat ngebuka pesan rahasia dari aku ya!</p>', unsafe_allow_html=True)

# Menentukan jumlah gelembung (4 baris x 4 kolom = 16)
total_bubbles = 16

# Inisialisasi state untuk mengingat gelembung mana yang sudah dipencet
if 'popped' not in st.session_state:
    st.session_state.popped = [False] * total_bubbles

# Fungsi untuk memecahkan gelembung
def pop_bubble(index):
    st.session_state.popped[index] = True

# Membuat Grid 4 kolom
cols = st.columns(4)

# Menampilkan tombol-tombol Pop It
for i in range(total_bubbles):
    col = cols[i % 4]
    with col:
        # Jika True (sudah dipencet), tampilkan tombol hati (disabled biar nggak bisa dipencet lagi)
        if st.session_state.popped[i]:
            st.button("💖", key=f"btn_{i}", disabled=True, use_container_width=True)
        # Jika False (belum dipencet), tampilkan gelembung
        else:
            st.button("🫧", key=f"btn_{i}", on_click=pop_bubble, args=(i,), use_container_width=True)

st.write("---")

# === BAGIAN KEJUTAN (MUNCUL KALAU SEMUA SUDAH DIPENCET) ===
# Mengecek apakah semua item di dalam list st.session_state.popped bernilai True
if all(st.session_state.popped):
    st.balloons() # Mengeluarkan animasi balon
    st.success("Yeay! Semua gelembung udah pecah! 🎉")
    
    st.markdown('<p class="judul">Surprise! 💌</p>', unsafe_allow_html=True)
    st.write("Makasih ya udah sabar mencetin gelembungnya satu-satu, hehe. Ini bukti kalau kamu emang sabar banget ngadepin aku.")
    st.write("Cuma mau bilang, *I'm so lucky to have you*. Jangan lupa senyum hari ini dan tetep semangat ya! ✨")
    
    # Tombol opsional kalau mau di-reset
    col_reset1, col_reset2, col_reset3 = st.columns([1, 2, 1])
    with col_reset2:
        if st.button("Tutup Pesan (Reset) 🔄", use_container_width=True):
            st.session_state.popped = [False] * total_bubbles
            st.rerun()
