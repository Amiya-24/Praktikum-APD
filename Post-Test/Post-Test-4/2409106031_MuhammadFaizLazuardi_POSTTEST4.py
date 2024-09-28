import os

def clean():
    os.system("cls") # dipakai untuk membersihkan tampilan terminal

clean()
user = "faiz"
pw = 31

percobaan = 3
while percobaan > 0:
    print("<========== Login ==========>")
    log_user = str(input("Masukkan Username Anda: "))
    log_pw = int(input("Masukkan Password Anda: "))
    if log_user == user and log_pw == pw:
        print("Anda Berhasil Login ")

        clean()
        while True:
            print("<========== Masukkan Data ==========>")
            nama = input("Masukkan Nama Lengkap Anda: ")
            nim = input("Masukkan Nim Anda: ")
            jml_pinjaman = int(input("Masukkan Jumlah Pinjaman: "))
            print("<===================================>")

            clean()
            print("""
<========== Lama Cicilan ==========>
Pilih Lama Cicilan
1. 1 Tahun
2. 2 Tahun
3. 3 Tahun
<==================================>
            """)
            lama_ccl = int(input("Masukkan Pilihan Anda (1/2/3): "))

            bunga_tahun = 0
            jlm_bln = 0

            if lama_ccl == 1:
                bunga_tahun = 0.07
                jlm_bln = lama_ccl * 12
            elif lama_ccl == 2:
                bunga_tahun = 0.13
                jlm_bln = lama_ccl * 12
            elif lama_ccl == 3:
                bunga_tahun = 0.19
                jlm_bln = lama_ccl * 12
            else:
                print("Pilihan Tidak Valid")

            bunga_bulan = (bunga_tahun / 12) * jml_pinjaman
            ccl_bulan = (jml_pinjaman + bunga_bulan) / jlm_bln
            
            clean()
            print(f"""
<========== Rincian Pinjaman ===========>
Nama : {nama}                        
Nim : {nim}                          
Jumlah Pinjaman : Rp. {jml_pinjaman}            
Lama Cicilan : {lama_ccl} Tahun             
Bunga/Tahun : {bunga_tahun}                    
Bunga/Bulan : {bunga_bulan}                      
Cicilan/Bulan : Rp. {ccl_bulan}
<=======================================>
            """)

            
            ulang = input("Apakah Anda Ingin Mengulang? ketik '1' untuk mengulang atau '2' untuk keluar: ")
            clean()
            if ulang == "2":
                print("Program Dihentikan")
                break
            
    else:
        percobaan -= 1
        print("Username Atau Password Anda Salah")
        print("Masukkan Username Atau Password Yang Benar\n")
    break

if percobaan == 0:
    print("\nMohon Tunggu Beberapa Saat Sebelum Mencoba Login Lagi")