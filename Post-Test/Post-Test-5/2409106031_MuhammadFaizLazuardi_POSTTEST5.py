account = [
    ["admin","admin123"],
    ["staff","staff123"]
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
        # LOGIN ADMIN
        pilih2 = input("Masukkan Piihan Anda: ")
        if pilih2 == "1":
            user = input("\nMasukkan Username Anda: ")
            pw = input("Masuhkkan Password Anda: ")
            accountada =  False
            for i in  range(len(account)):
                if user == account[0][0] and pw == account[0][1]:
                    accountada = True
                    while True:
                        print("")
                else:
                    print("Username atau Password Anda Salah")
                    exit()

    elif pilih1 == "2" :
        break
    else:
        print("Input Yang Anda Masukkan Salah")
        break