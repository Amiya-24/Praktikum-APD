akun = {
    "admin" : {"pw" : "admin123", "role" : "ADMIN"}
}

menu = {
    "ayam" : 100,
    "bebek" : 110,
    "lele" : 125
}

while True:
    print("""
<============================================================>
|             SELAMAT DATANG DI WARUNG MAKAN ABL             | 
<============================================================>
| 1. Register                                                |
| 2. Login                                                   |
| 3. Keluar                                                  |
<============================================================>
""")
    pilih1 = input("\nMasukkan Pilihan Anda: ")

    # REGISTER
    if pilih1 == "1":
        username_baru = input("\nMasukkan Username Baru: ")

        if username_baru in akun:
            print("Nama Akun Sudah Terdaftar!")

        else:
            password_baru = input("Masukkan Password Baru: ")
            role_baru = "pengunjung"
            akun[username_baru] = {"pw" : password_baru, "role" : role_baru}
            print("Register Berhasil!")
    # LOGIN
    elif pilih1 == "2":
        username = input("\nMasukkan Username: ")
        password = input("Masukkan Password: ")

        if username in akun and akun[username]["pw"] == password:
            print(f"Login Berhasil, Selamat Datang {username}")
            role = akun[username]["role"]

            print("\n<==============================>")
            print("|        SELAMAT DATANG        |")
            print("<==============================>")
            print("| 1. Liat Menu                 |")
            if role == "ADMIN":
                print("| 2. Tambah Menu               |")
                print("| 3. Ubah Menu                 |")
                print("| 4. Hapus Menu                |")
            print("| 5. Keluar                    |")
            print("<==============================>")

            while True:
                pilih2 = input("\nMasukkan Pilihan Anda: ")

                # READ
                if pilih2 == "1":
                    if len(menu) == 0:
                        print("\nMenu Masih Kosong")

                    else:
                        for key, value in menu.items():
                            print(f"\nNama Menu : {key}")
                            print(f"Harga Menu : Rp.{value}")

                # CREATE
                elif pilih2 == "2" and role == "ADMIN":
                    nama_menu = input("\nMasukkan Nama Menu: ")
                    if nama_menu in menu:
                        print("Menu Sudah Ada")

                    else:
                        harga_menu = int(input("Masukkan Harga Menu: Rp."))

                        while harga_menu <= 0:
                            print("Harga Tidak Bisa Lebih Kecil Dari 1")
                            harga_menu = int(input("Masukkan Harga Menu: Rp."))
                        menu[nama_menu] = {harga_menu}
                        print("Menu Berhasil Ditambahkan")

                # UPDATE
                elif pilih2 == "3" and role == "ADMIN":
                    menu_lama = input("\nMasukkan Menu Yang Ingin Diganti: ")
                    if menu_lama in menu:
                        menu_baru = input("Masukkan Menu Baru: ")
                        harga_baru = int(input("Masukkan Harga Baru: Rp."))

                        while harga_menu <= 0:
                            print("Harga Tidak Bisa Lebih Kecil Dari 1")
                            harga_baru = int(input("Masukkan Harga Baru: Rp."))
                        menu[menu_baru] = {harga_baru}
                        if menu_lama != menu_baru:
                            del menu[menu_lama]

                    else:
                        print("Menu Tidak Ditemukan")

                # DELETE
                elif pilih2 == "4" and role == "ADMIN":
                    if len(menu) == 0:
                        print("\nMenu Masih Kosong")

                    else:
                        menu_lama = input("\nMasukkan Menu Yang Ingin Dihapus: ")
                        if menu_lama in menu:
                            del menu[menu_lama]
                            print("Menu Berhasil Dihapus")

                        else:
                            print("\nNama Tidak Ditemukan")

                # KEMBALI
                elif pilih2 == "5":
                    print("\nKembali Ke Halaman Utama")
                    break

                else:
                    print("\nPilihan Invalid")

        else:
            print("Username Atau Password Anda Salah")

    # KELUAR
    elif pilih1 == "3":
        print("\nTerima Kasih Telah Datang")
        break

    else:
        print("\nPilihan Tidak Valid!")