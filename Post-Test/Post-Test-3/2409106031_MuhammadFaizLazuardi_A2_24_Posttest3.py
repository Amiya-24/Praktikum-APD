nama = input("Masukkan Nama Lengkap Anda: ")
nim = input("Masukkan Nim Anda: ")
d = int(input("Masukkan Jumlah Pinjaman Anda: "))

print("""
==========================
Pilih Lama Cicilan
1. 1 Tahun
2. 2 Tahun
3. 3 Tahun
==========================
""")
f = int(input("Masukkan Pilihan Anda (1/2/3): "))

v = 0
j = 0

if f == 1:
    v = 0.07
    j = f * 12
elif f == 2:
    v = 0.13
    j = f * 12
elif f == 3:
    v = 0.19
    j = f * 12
else:
    print("Pilihan Tidak Valid")
    exit()

g = (v / 12) * d
h = (d + g) / j

print(f"""
==========Rincian Pinjaman==========
Nama : {nama}
Nim : {nim}
Jumlah Pinjaman : Rp. {d}
Lama Cicilan : {f} Tahun
Bunga/Tahun : {v}
Bunga/Bulan : {g}
Cicilan/Bulan : Rp. {h}
====================================
""")