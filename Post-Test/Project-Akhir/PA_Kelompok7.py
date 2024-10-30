import os
import csv

def clean():
    os.system("cls")

clean()

def register(username, password, role):
    try:
        with open("./Post-Test/Project-Akhir/akun.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, role])

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def login(username, password):
    try:
        with open("./Post-Test/Project-Akhir/akun.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Login Berhasil")
                    return row[2]

            print("Username atau Password Salah")
            return None
        
    except FileNotFoundError:
        print("File Tidak Ditemukan")
        return None

def keluar_dari_program():
    print("\nTerima Kasih Telah Datang")
    exit()

def liat_menu():
    try:
        with open("./Post-Test/Project-Akhir/menu.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)
            if lines:
                for index, line in enumerate(lines):
                    print(f"""
Menu ke-{index+1}
Nama Menu : {line[0]}
Harga Menu : {line[1]}
""")
            else:
                print("Menu Masih Kosong")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def tambah_menu(nama_menu, harga_menu):
    with open("./Post-Test/Project-Akhir/menu.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama_menu, harga_menu])

def ubah_menu(index, menu_baru, harga_baru):
    with open("./Post-Test/Project-Akhir/menu.csv", "r") as file:
        lines = list(csv.reader(file))

    if index >= 0 and index < len(lines):
        lines[index][0] = menu_baru
        lines[index][1] = harga_baru
        with open("./Post-Test/Project-Akhir/menu.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)

def hapus_menu(index):
    with open("./Post-Test/Project-Akhir/menu.csv", "r") as file:
        lines = list(csv.reader(file))

    if index >= 0 and index < len(lines):
        del lines[index]
        with open("./Post-Test/Project-Akhir/menu.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)

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
        clean()
        print("<========== REGISTER ==========>")
        username_baru = input("Masukkan Username Baru: ")
        password_baru = input("Masukkan Password Baru: ")
        role_baru = "pengunjung"
        register(username_baru,password_baru,role_baru)        
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
                    nama_menu = input("Masukkan Nama Menu: ")
                    harga_menu = int(input("Masukkan Harga Menu: Rp."))
                    tambah_menu(nama_menu,harga_menu)
                    print("Menu Berhasil Ditambahkan")
                    print("\n<======================================>")

                elif pilih2 == "3" and role == "ADMIN":
                    print("<========== MENGUBAH MENU ==========>")
                    liat_menu()
                    index_baru = int(input("Masukkan Nomor Menu Yang Ingin Diubah: ")) - 1
                    menu_baru = input("Masukkan Menu Baru: ")
                    harga_baru = int(input("Masukkan Harga Baru: Rp."))
                    ubah_menu(index_baru, menu_baru, harga_baru)
                    print("Menu Berhasil Diubah")
                    print("\n<===================================>")

                elif pilih2 == "4" and role == "ADMIN":
                    print("<========== MENGHAPUS MENU ==========>")
                    liat_menu()
                    index_hapus = int(input("Masukkan Nomor Menu Yang Ingin Dihapus: ")) - 1
                    hapus_menu(index_hapus)
                    print("Menu Berhasil Dihapus")
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