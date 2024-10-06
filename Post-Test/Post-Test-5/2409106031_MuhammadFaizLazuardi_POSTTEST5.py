account = [
    ["admin","admin123"],
    ["staff","staff123"]
]

makan = [["Ayam","Bebek","Lele"]]
minum = [["Es Teh","Es Jeruk","Air Mineral"]]
paket = [
    [makan[0][0],minum[0][0]],
    [makan[0][1],minum[0][1]],
    [makan[0][2],minum[0][2]]
]





while True:
    print("""
<============================================================>
| SELAMAT DATANG DI SISTEM MANAJEMEN PRODUK WARUNG MAKAN ABL | 
<============================================================>
| 1. Login                                                   |
| 2. Keluar                                                  |
<============================================================>
""")
    pilih1 = input("Masukkan Pilihan Anda: ")
    if pilih1 == "1" :
        print("""
<========== LOGIN ==========>
| 1. Sebagai Admin          |
| 2. Sebagai Staff          |
| 3. Kembali                |
<===========================>
""")
        pilih2 = input("Masukkan Piihan Anda: ")
        # LOGIN ADMIN
        if pilih2 == "1":
            user = input("\nMasukkan Username Anda: ")
            pw = input("Masuhkkan Password Anda: ")
            account_ada =  False
            for i in  range(len(account)):
                if user == account[0][0] and pw == account[0][1]:
                    account_ada = True
                    while True:
                        print("""
<==============================>
|     SELAMAT DATANG ADMIN     |
<==============================>
| 1. Tambahkan Menu Baru       |
| 2. Liat Menu Yang Ada        |                  
| 3. Ubah Menu Yang Ada        |
| 4. Hapus Menu Yang Ada       |
| 5. Kembali                   |
| 6. Keluar                    |
<==============================>
""")
                        pilih3 = input("Masukkan Pilihan Anda: ")
                        if pilih3 == "1":
                            print("""
<=============================>
|     TAMBAHKAN MENU BARU     |
<=============================>
| 1. Makanan                  |                                            
| 2. Minuman                  |         
| 3. Paket Hemat              |             
| 4. Kembali                  | 
| 5. Keluar                   |                                               
<=============================>                                                                
""")
                            pilih4 = input("Menu Apa Yang Ingin Anda Tambahkan: ")
                            if pilih4 == "1":
                                makan_baru = input("Masukkan Nama Makanan Yang Ingin di Tambahkan: ")
                                makan_ada = False
                        elif pilih3 == "2":
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
                        # elif pilih3 == "3":
                        # elif pilih3 == "4":
                        # elif pilih3 == "5":
                        else:
                            exit()
            
                
                else:
                    print("Username atau Password Anda Salah")
                    exit()
        # LOGIN STAFF            
        elif pilih2 == "2":
            user = input("\nMasukkan Username Anda: ")
            pw = input("Masuhkkan Password Anda: ")
            account_ada =  False
            for i in  range(len(account)):
                if user == account[1][0] and pw == account[1][1]:
                    account_ada = True
                    print("d")
                    exit()
        # KEMBALI            
        elif pilih2 == "3":
            continue

        else:
            print("Input Yang Anda Masukkan Salah")
            break

    elif pilih1 == "2" :
        break
    else:
        print("Input Yang Anda Masukkan Salah")
        break