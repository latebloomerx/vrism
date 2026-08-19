import streamlit as st

# Mengatur tampilan tab web
st.set_page_config(page_title="Ada Pesan Buat Kamu 💌", page_icon="💖")

# Judul Halaman
st.title("Hai! Prisma💖")
st.write("Aku ada sesuatu nih buat kamu, coba dibuka deh...")

# Memakai expander untuk memberikan sensasi 'membuka amplop/surat'
with st.expander("Buka pesannya di sini ya"):
    st.write("Makasih ya udah selalu jadi alasan aku buat senyum setiap hari.")
    st.write("Cuma mau ngingetin, jangan lupa istirahat yang cukup dan makan yang enak!")
    
    st.write("Btw, seneng gak dapet kejutan ini?")
    
    # Membuat tombol pilihan berdampingan
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Seneng banget! ❤️"):
            # Mengeluarkan animasi balon
            st.balloons()
            st.success("Yeay! Nanti weekend kita jalan yuk! 🍕")
            
    with col2:
        if st.button("Biasa aja tuh 😜"):
            # Mengeluarkan efek salju
            st.snow()
            st.error("Yahhh, gapapa deh, yang penting kamu tetep manis! ✨")