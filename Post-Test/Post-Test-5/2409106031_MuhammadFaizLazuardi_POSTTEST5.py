account = []

while True:
    print("""
<============================================================>
| SELAMAT DATANG DI SISTEM MANAJEMEN PRODUK WARUNG MAKAN ABL | 
<============================================================>
| 1. Register                                                |
| 2. Login                                                   |
| 3. Keluar                                                  |
<============================================================>
""")
    
    pilih1 = input("Masukkan Pilihan Anda: ")
    if pilih1 == "1":
        print("<========== REGISTER ==========>")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        role = input("1.Admin\n2.Staff\nPilih Role Account: ")
        if role == "1":
            role = "admin"
        elif role == "2":
            role = "Staff"
        else:
            print("Input Invalid")

        tambah_akun = [username,password,role]    
        account.append(tambah_akun)
        print("Register Berhasil")

    elif pilih1 == "2":
        while True:
            print("<========== LOGIN ==========>")
            username = input("Masukkan Username Anda: ")
            password = input("Masukkan Password Anda: ")
            for cek_akun in account:
                if cek_akun[0] == username and cek_akun[1] == password:
                    if cek_akun[2] == "admin":
                        print("Selamat Anda Berhasil Login Sebagai Admin")
                        print("""
    <==============================>
    |     SELAMAT DATANG ADMIN     |
    <==============================>
    | 1. Tambahkan Menu Baru       |
    | 2. Liat Menu Yang Ada        |                  
    | 3. Ubah Menu Yang Ada        |
    | 4. Hapus Menu Yang Ada       |
    | 5. Keluar                    |
    <==============================>
    """)
                        pilih2 = input("Masukkan Pilihan Anda: ")
                        
                        # TAMBAH MENU
                        if pilih2 == "1":
                            print("""
    <=============================>
    |     TAMBAHKAN MENU BARU     |
    <=============================>
    | 1. Makanan                  |                                            
    | 2. Minuman                  |                  
    | 3. Kembali                  | 
    | 4. Keluar                   |                                               
    <=============================>                                                                
    """)
                            pilih3 = input("Masukkan Pilihan Anda: ")
                            # MENU MAKANAN
                            if pilih3 == "1":
                                makanan = input("Masukkan Nama Makanan: ")
                            # MENU MINUMAN
                            elif pilih3 == "2":
                                minuman = input("Masukkan Nama Minuman: ")
                            # MENU KEMBALI
                            elif pilih3 == "3":
                                continue
                            # MENU KELUAR
                            elif pilih3 == "4":
                                exit()


                        # LIAT MENU
                        elif pilih2 == "2":
                            print("""
    <============================>
    |     LIST MENU YANG ADA     |
    <============================>
    | 1. Makanan                 |  
    | 2. Minuman                 |  
    | 3. Paket Hemat             |      
    | 4. Kembali                 |  
    | 5. Keluar                  | 
    <============================>                                  
    """)
                        # UBAH MENU
                        elif pilih2 == "3":
                            print("""
    <============================>
    |     UBAH MENU YANG ADA     |
    <============================>
    | 1. Makanan                 |  
    | 2. Minuman                 |  
    | 3. Paket Hemat             |      
    | 4. Kembali                 |  
    | 5. Keluar                  | 
    <============================>                                  
    """)
                        #HAPUS MENU
                        elif pilih2 == "4":
                            print("""
    <============================>
    |    HAPUS MENU YANG ADA     |
    <============================>
    | 1. Makanan                 |  
    | 2. Minuman                 |  
    | 3. Paket Hemat             |      
    | 4. Kembali                 |  
    | 5. Keluar                  | 
    <============================>                                  
    """)
                        #KELUAR
                        else:
                            exit()

                    elif cek_akun[2] == "staff":
                        print("Selamat Anda Berhasil Login Sebagai Staff")
                else:
                    print("Username atau Password Anda Salah, Program Dihentikan")
                    exit()
            print("Belum Ada Akun Yang Terdaftar")
            break
            

    elif pilih1 == "3":
        break
    else:
        print("Input Yang Anda Masukkan Salah")
        break