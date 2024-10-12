akun = [["admin","admin123","ADMIN"]]
menu = [["ayam",100],["bebek",110],["lele",125]]

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

    if pilih1 == "1":
        username_baru = input("\nMasukkan Username Baru: ")
        akun_terdaftar = False
        for user in akun:
            if user[0] == username_baru:
                akun_terdaftar = True
                break

        if akun_terdaftar:
            print("Nama Akun Sudah Terdaftar!")

        else:
            password_baru = input("Masukkan Password Baru: ")
            role_baru = "pengunjung"
            akun.append([username_baru, password_baru, role_baru])
            print("Register Berhasil!")

    elif pilih1 == "2":
        username = input("\nMasukkan Username: ")
        password = input("Masukkan Password: ")
        login = False

        for user in akun:
            if user[0] == username and user[1] == password:
                print(f"Login Berhasil, Selamat Datang {username}")
                login = True
                role = user[2]
                break
        else:
            print("Username Atau Password Anda Salah")

        if login:
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
                if pilih2 == "1":
                    if len(menu) == 0:
                        print("\nMenu Masih Kosong")
                    else:
                        for i in range(len(menu)):
                            print(f"\nMenu ke-{i+1}\nNama Menu : {menu[i][0]}\nHarga Menu : Rp.{menu[i][1]}")
                elif pilih2 == "2" and role == "ADMIN":
                    nama_menu = input("\nMasukkan Nama Menu: ")
                    for i in range(len(menu)):
                        if menu[i][0] == nama_menu:
                            print("Menu Sudah Ada")
                            break
                    else:
                        harga_menu = int(input("Masukkan Harga Menu: Rp."))
                        while harga_menu <= 0:
                            print("Harga Tidak Bisa Lebih Kecil Dari 1")
                            harga_menu = int(input("Masukkan Harga Menu: Rp."))
                        menu.append([nama_menu,harga_menu])
                        print("Menu Berhasil Ditambahkan")
                elif pilih2 == "3" and role == "ADMIN":
                    menu_lama = input("\nMasukkan Menu Yang Ingin Diganti: ")
                    for i in range(len(menu)):
                        if menu[i][0] == menu_lama:
                            menu_baru = input("Masukkan Menu Baru: ")
                            harga_baru = int(input("Masukkan Harga Baru: Rp."))
                            while harga_menu <= 0:
                                print("Harga Tidak Bisa Lebih Kecil Dari 1")
                                harga_baru = int(input("Masukkan Harga Baru: Rp."))
                            menu[i][0] = menu_baru
                            menu[i][1] = harga_baru
                            break
                    else:
                        print("Menu Tidak Ditemukan")
                elif pilih2 == "4" and role == "ADMIN":
                    if len(menu) == 0:
                        print("\nMenu Masih Kosong")
                    else:
                        menu_lama = input("\nMasukkan Menu Yang Ingin Dihapus: ")
                        for i in range(len(menu)):
                            if menu[i][0] == menu_lama:
                                del menu[i]
                                print("Menu Berhasil Dihapus")
                                break
                        else:
                            print("\nNama Tidak Ditemukan")
                elif pilih2 == "5":
                    print("\nKembali Ke Halaman Utama")
                    break
                else:
                    print("\nPilihan Invalid")

    elif pilih1 == "3":
        print("\nTerima Kasih Telah Datang")
        break

    else:
        print("\nPilihan Tidak Valid!")