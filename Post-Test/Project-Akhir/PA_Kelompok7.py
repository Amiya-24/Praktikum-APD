import os
import csv

def clean():
    os.system("cls")

clean()

def cek_username(username):
    try:
        with open("./Post-Test/Project-Akhir/akun.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == username:
                    print("Username Sudah Terdaftar")
                    return True
            return False
                
    except FileNotFoundError:
        print("File Tidak Ditemukan")
        return False

def register(username, password, role = "Pengunjung"):
    try:
        with open("./Post-Test/Project-Akhir/akun.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, role])
            print("Register Berhasil")
    
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

def lihat_pesanan():
    try:
        with open("./Post-Test/Project-Akhir/pesanan.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)

            if lines:
                for index, line in lines:
                    print(f"""
Pesanan Ke-{index + 1}
Nama Menu: {line[0]} 
Jumlah Pesanan: {line[1]}
""")
            else:
                print("Tidak Ada Pesanan")
    except FileNotFoundError:
        print("File Tidak Ditemukan")

def tambah_pesanan(nama_menu, jumlah_pesanan):
    try:
        with open("./Post-Test/Project-Akhir/pesanan.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nama_menu, jumlah_pesanan])
            print("Pesanan Berhasil Ditambahkan")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def ubah_pesanan(index, nama_menu, jumlah_pesanan):
    try:
        with open("./Post-Test/Project-Akhir/pesanan.csv", "r") as file:
            lines = list(csv.reader(file))

            if 0 <= index < len(lines):
                lines[index][0] = nama_menu
                lines[index][1] = jumlah_pesanan
                with open("./Post-Test/Project-Akhir/pesanan.csv", "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(lines)
                    print("Pesanan Berhasil Diubah")
            else:
                print("Pilihan Tidak Valid")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def hapus_pesanan(index):
    try:
        with open("./Post-Test/Project-Akhir/pesanan.csv", "r") as file:
            lines = list(csv.reader(file))

        if 0 <= index < len(lines):
            del lines[index]
            with open("./Post-Test/Project-Akhir/pesanan.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
                print("Pesanan Berhasil Dihapus")
        else:
            print("Pilihan Tidak Valid")
    
    except FileNotFoundError:
        print("File Tidak Ditemukan")

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
Harga Menu : Rp.{line[1]}
""")
            else:
                print("Menu Masih Kosong")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def tambah_menu(nama_menu, harga_menu):
    try:
        with open("./Post-Test/Project-Akhir/menu.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nama_menu, harga_menu])
            print("Menu Berhasil Ditambahkan")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def ubah_menu(index, menu_baru, harga_baru):
    try:
        with open("./Post-Test/Project-Akhir/menu.csv", "r") as file:
            lines = list(csv.reader(file))

        if 0 <= index < len(lines):
            lines[index][0] = menu_baru
            lines[index][1] = harga_baru
            with open("./Post-Test/Project-Akhir/menu.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
                print("Menu Berhasil Diubah")

        else:
            print("Pilihan Tidak Valid")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

def hapus_menu(index):
    try:
        with open("./Post-Test/Project-Akhir/menu.csv", "r") as file:
            lines = list(csv.reader(file))

        if 0 <= index < len(lines):
            del lines[index]
            with open("./Post-Test/Project-Akhir/menu.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
            print("Menu Berhasil Dihapus")

        else:
            print("Pilihan Tidak Valid")

    except FileNotFoundError:
        print("File Tidak Ditemukan")

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

def menu_admin():
    print("\n<==============================>")
    print("|        SELAMAT DATANG        |")
    print("<==============================>")
    print("| 1. Liat Menu                 |")
    print("| 2. Tambah Menu               |")
    print("| 3. Ubah Menu                 |")
    print("| 4. Hapus Menu                |")
    print("| 5. Kembali                   |")
    print("<==============================>")

def menu_pengunjung():
    print("\n<==============================>")
    print("|        SELAMAT DATANG        |")
    print("<==============================>")
    print("| 1. Liat Menu                 |")
    print("| 2. Tambah Pesanan            |")
    print("| 3. Ubah Pesanan              |")
    print("| 4. Hapus Pesanan             |")
    print("| 5. Lihat Pesanan             |")
    print("| 6. Kembali                   |")
    print("<==============================>")


def program():
    tampilan_menu_utama()
    pilih1 = input("\nMasukkan Pilihan Anda: ")

    if pilih1 == "1":
        clean()
        print("<========== REGISTER ==========>")
        username_baru = input("Masukkan Username Baru: ")
        if not cek_username(username_baru):
            password_baru = input("Masukkan Password Baru: ")
            register(username_baru, password_baru)
        print("<==============================>")

    elif pilih1 == "2":
        clean()
        print("<=============== LOGIN ===============>")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        role = login(username,password)
        print("<=====================================>")

        if role == "ADMIN":
            while True:
                menu_admin()
                pilih2 = input("\nMasukkan Pilihan Anda: ")
                clean()

                if pilih2 == "1":
                    print("<========== DAFTAR MENU ==========>")
                    liat_menu()
                    print("<=================================>")

                elif pilih2 == "2":
                    print("<========== MENAMBAHKAN MENU ==========>")
                    nama_menu = input("Masukkan Nama Menu: ")
                    harga_menu = input("Masukkan Harga Menu: Rp.")
                    try:
                        harga_menu = int(harga_menu)
                        tambah_menu(nama_menu, harga_menu)
                        print("Menu Berhasil Ditambahkan")

                    except ValueError:
                        print("Harga harus berupa angka")
                    print("\n<======================================>")

                elif pilih2 == "3":
                    print("<========== MENGUBAH MENU ==========>")
                    liat_menu()
                    try:
                        index_baru = int(input("Masukkan Nomor Menu Yang Ingin Diubah: ")) - 1
                        menu_baru = input("Masukkan Menu Baru: ")
                        harga_baru = int(input("Masukkan Harga Baru: Rp."))
                        ubah_menu(index_baru, menu_baru, harga_baru)
                        print("Menu Berhasil Diubah")

                    except ValueError:
                        print("Input tidak valid")
                    print("\n<===================================>")

                elif pilih2 == "4":
                    print("<========== MENGHAPUS MENU ==========>")
                    liat_menu()
                    try:
                        index_hapus = int(input("Masukkan Nomor Menu Yang Ingin Dihapus: ")) - 1
                        hapus_menu(index_hapus)
                        print("Menu Berhasil Dihapus")

                    except ValueError:
                        print("Input tidak valid")
                    print("\n<====================================>")

                elif pilih2 == "5":
                    kembali_ke_menu()
                    break

                else:
                    print("\nPilihan Invalid")

        else:
            while True:
                menu_pengunjung()
                pilih2 = input("\nMasukkan Pilihan Anda: ")
                clean()

                if pilih2 == "1":
                    print("<========== DAFTAR MENU ==========>")
                    liat_menu()
                    print("\n<=================================>")
                
                elif pilih2 == "2":
                    print("<========== MENAMBAHKAN PESANAN ==========>")
                    liat_menu()
                    try:
                        index_pesanan = int(input("Masukkan Nomor Menu Yang Ingin Dipesan: ")) - 1
                        try:
                            jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
                            print("Pesanan Berhasil Ditambahkan")
                            tambah_pesanan(index_pesanan,jumlah_pesanan)

                        except ValueError:
                            print("Jumlah Pesanan harus berupa angka")
                
                    except ValueError:
                        print("Input Tidak Valid")
                
                elif pilih2 == "3":
                    print("<========== MENGUBAH PESANAN ==========>")
                    liat_menu()
                    try:
                        index_pesanan = int(input("Masukkan Nomor Menu Yang Ingin Diubah: ")) - 1
                        index_baru = int(input("Masukkan Nomor Menu Baru: ")) - 1
                        jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))
                        ubah_pesanan(index_pesanan, index_baru, jumlah_pesanan)

                    except ValueError:
                        print("Jumlah Pesanan harus berupa angka")
                
                elif pilih2 == "4":
                    print("<========== MENGHAPUS PESANAN ==========>")
                    liat_menu()
                    try:
                        index_pesanan = int(input("Masukkan Nomor Menu Yang Ingin Dihapus: ")) - 1
                        hapus_pesanan(index_pesanan)
                        

                    except ValueError:
                        print("Input Tidak Valid")

                elif pilih2 == "5":
                    print("<========== LIHAT PESANAN ==========>")
                    lihat_pesanan()
                    print("\n<=================================>")
                
                elif pilih2 == "6":
                    kembali_ke_menu()
                    break
                
                else:
                    print("\nPilihan Invalid")


    elif pilih1 == "3":
        clean()
        keluar_dari_program()

    else:
        clean()
        print("\nPilihan Tidak Valid!")

while (True):
    program()