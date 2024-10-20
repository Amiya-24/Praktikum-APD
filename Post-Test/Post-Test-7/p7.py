akun = {
    "admin" : {"pw" : "admin123", "role" : "ADMIN"}
}

menu = {
    "ayam" : 100,
    "bebek" : 110,
    "lele" : 125
}

def login(username, password):
    if username in akun and akun[username]["pw"] == password:
        print(f"Login Berhasil, Selamat Datang {username}")
        return akun[username]["role"]
    
    else:
        print("Username Atau Password Anda Salah")
        return None

def keluar_dari_program():
    print("\nTerima Kasih Telah Datang")
    exit()

def liat_menu():
    if len(menu) == 0:
        print("\nMenu Masih Kosong")

    else:
        for nama, harga in menu.items():
            print(f"\nNama Menu : {nama}")
            print(f"Harga Menu : Rp.{harga}")

def tambah_menu():
    nama_menu = input("\nMasukkan Nama Menu: ")
    if nama_menu in menu:
        print("Menu Sudah Ada")

    else:
        while True:
            try:
                harga_menu = int(input("Masukkan Harga Menu: Rp."))

                while harga_menu <= 0:
                    print("Harga Tidak Bisa Lebih Kecil Dari 1")
                    harga_menu = int(input("Masukkan Harga Menu: Rp."))
                menu[nama_menu] = harga_menu
                print("Menu Berhasil Ditambahkan")
                break

            except ValueError:
                print("Masukkan Angka\n")

def ubah_menu():
    menu_lama = input("\nMasukkan Menu Yang Ingin Diganti: ")
    if menu_lama in menu:
        menu_baru = input("Masukkan Menu Baru: ")
        while True:
            try:
                harga_baru = int(input("Masukkan Harga Baru: Rp."))

                while harga_baru <= 0:
                    print("Harga Tidak Bisa Lebih Kecil Dari 1")
                    harga_baru = int(input("Masukkan Harga Baru: Rp."))
                menu[menu_baru] = harga_baru
                if menu_lama != menu_baru:
                    del menu[menu_lama]
                    print("Menu Berhasil Diganti")
                    break

            except ValueError:
                print("Masukkan Angka\n")

    else:
        print("Menu Tidak Ditemukan")

def hapus_menu():
    if len(menu) == 0:
        print("\nMenu Masih Kosong")

    else:
        menu_lama = input("\nMasukkan Menu Yang Ingin Dihapus: ")
        if menu_lama in menu:
            del menu[menu_lama]
            print("Menu Berhasil Dihapus")

        else:
            print("\nNama Tidak Ditemukan")

def kembali_ke_menu():
    print("\nKembali Ke Halaman Utama")

def tampilan_menu_utama():
     print("""
<============================================================>
|             SELAMAT DATANG DI WARUNG MAKAN ABL             | 
<============================================================>
| 1. Register                                                |
| 2. Login                                                   |
| 3. Keluar                                                  |
<============================================================>
""")
     
def program():
    tampilan_menu_utama()
    pilih1 = input("\nMasukkan Pilihan Anda: ")
    
    if pilih1 == "1":
        username_baru = input("\nMasukkan Username Baru: ")
        if username_baru in akun:
            print("Nama Akun Sudah Terdaftar!")

        else:
            password_baru = input("Masukkan Password Baru: ")
            role_baru = "pengunjung"
            akun[username_baru] = {"pw" : password_baru, "role" : role_baru}
            print("Register Berhasil!")

    elif pilih1 == "2":
        username = input("\nMasukkan Username: ")
        password = input("Masukkan Password")
        role = login(username,password)

        if role:
            print("\n<==============================>")
            print("|        SELAMAT DATANG        |")
            print("<==============================>")
            print("| 1. Liat Menu                 |")
            if role == "ADMIN":
                print("| 2. Tambah Menu               |")
                print("| 3. Ubah Menu                 |")
                print("| 4. Hapus Menu                |")
            print("| 5. Kembali                   |")
            print("<==============================>")

            while True:
                pilih2 = input("\nMasukkan Pilihan Anda: ")
                if pilih2 == "1":
                    liat_menu()

                elif pilih2 == "2":
                    tambah_menu()

                elif pilih2 == "3":
                    ubah_menu()

                elif pilih2 == "4":
                    hapus_menu()

                elif pilih2 == "5":
                    kembali_ke_menu()
                    break

                else:
                    print("\nPilihan Invalid")

    elif pilih1 == "3":
        keluar_dari_program()

    else:
        print("\nPilihan Tidak Valid!")

while (True):
    program()