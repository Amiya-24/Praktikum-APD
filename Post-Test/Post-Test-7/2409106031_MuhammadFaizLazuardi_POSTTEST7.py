import os

def clean():
    os.system("cls")

clean()

akun = {
    "admin" : {"pw" : "admin123", "role" : "ADMIN"}
}

menu = {
    "ayam" : 100,
    "bebek" : 110,
    "lele" : 125
}

jumlah_menu = 1
log_stat = False

def login(username, password):
    global log_stat
    if username in akun and akun[username]["pw"] == password:
        print(f"Login Berhasil, Selamat Datang {username}")
        log_stat = True
        return akun[username]["role"]

    else:
        print("Username Atau Password Anda Salah")
        return None

def keluar_dari_program():
    print("\nTerima Kasih Telah Datang")
    exit()

def liat_menu():
    global jumlah_menu
    if len(menu) == 0:
        print("\nMenu Masih Kosong")

    else:
        for nama, harga in menu.items():
            print(f"\nMenu Ke-{jumlah_menu}\nNama Menu : {nama}\nHarga Menu : RP.{harga}")
            jumlah_menu += 1
        jumlah_menu = 1

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
    global log_stat
    print("\nKembali Ke Halaman Utama")
    log_stat = False

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
        clean()
        print("<========== REGISTER ==========>")
        username_baru = input("Masukkan Username Baru: ")
        if username_baru in akun:
            print("Nama Akun Sudah Terdaftar!")

        else:
            role_baru = "pengunjung"
            password_baru = input("Masukkan Password Baru: ")
            akun[username_baru] = {"pw" : password_baru, "role" : role_baru}
            print("Register Berhasil!")
        print("<==============================>")

    elif pilih1 == "2":
        clean()
        print("<=============== LOGIN ===============>")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        role = login(username,password)
        print("<=====================================>")
        while log_stat is False:
            ulangi = input("Apakah Anda Ingin Mencoba Ulang (Y/N): ")
            if ulangi == "Y":
                clean()
                print("<=============== LOGIN ===============>")
                username = input("Masukkan Username: ")
                password = input("Masukkan Password: ")
                role = login(username, password)
                print("<=====================================>")
            elif ulangi == "N":
                clean()
                print("Kembali Ke Menu Utama")
                break
            else:
                clean()
                print("Input Salah, Pilihan Hanya (Y/N): ")

        if role:
            while True:
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

                pilih2 = input("\nMasukkan Pilihan Anda: ")
                clean()
                if pilih2 == "1":
                    print("<========== DAFTAR MENU ==========>")
                    liat_menu()
                    print("\n<=================================>")

                elif pilih2 == "2" and role == "ADMIN":
                    print("<========== MENAMBAHKAN MENU ==========>")
                    tambah_menu()
                    print("\n<======================================>")

                elif pilih2 == "3" and role == "ADMIN":
                    print("<========== MENGUBAH MENU ==========>")
                    ubah_menu()
                    print("\n<===================================>")

                elif pilih2 == "4" and role == "ADMIN":
                    print("<========== MENGHAPUS MENU ==========>")
                    hapus_menu()
                    print("\n<====================================>")

                elif pilih2 == "5":
                    kembali_ke_menu()
                    break

                else:
                    print("\nPilihan Invalid")

    elif pilih1 == "3":
        clean()
        keluar_dari_program()

    else:
        print("\nPilihan Tidak Valid!")

while (True):
    program()