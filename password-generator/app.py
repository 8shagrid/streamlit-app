import streamlit as st
import random
import string

# Judul
st.title("Password Generator")

# Penjelasan
st.write("Password Generator adalah sebuah alat yang digunakan untuk membuat password yang aman dan kuat. "
         "Password Generator dapat menghasilkan password yang acak, unik, "
         "dan kompleks yang dapat meningkatkan keamanan akun online Anda. "
         "Password Generator dapat menggunakan berbagai macam karakter, "
         "seperti huruf besar, huruf kecil, angka, dan simbol untuk membuat password yang kompleks.")

st.write("Generate secure password untuk menjaga keamanan data Anda.")
# Menentukan panjang kata sandi
password_length = st.slider(
    "Panjang kata sandi",
    min_value=7,
    max_value=50,
    value=15,
    step=1,
)

# Besar kecil huruf di kata sandi
st.write("Pilih karakter yang ingin anda masukkan:")
include_uppercase = st.checkbox("Huruf besar")
include_lowercase = st.checkbox("Huruf kecil")

# Memasukkan angka di kata sandi
include_numbers = st.checkbox("Angka")

# Memasukkan karakter khusus di kata sandi
include_special_characters = st.checkbox("Karakter spesial")

# Jarak
for i in range(8):
    st.write("")



# Tombol generate
if st.button("Generate"):
    characters = []

    if include_lowercase:
        characters.extend(list(string.ascii_lowercase))  # abcdefghijklmnopqrstuvwxyz
    if include_uppercase:
        characters.extend(list(string.ascii_uppercase))  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    if include_numbers:
        characters.extend(list(string.digits))  # 0123456789
    if include_special_characters:
        characters.extend(list(string.punctuation))  # !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

    

    try:
        # Menampilkan hasil
        st.text("Password Anda adalah:")
         
        # Membuat kata sandi acak
        password = "".join(random.sample(characters, password_length))
         
        # Menampilkan pesan sukses
        st.success(password)
         
    except ValueError:
        # Menampilkan pesan error
        st.error('Pilih salah satu karakter diatas.')
