nama = input("Masukkan Nama Lengkap Anda: ")
nim = input("Masukkan Nim Anda: ")
harga_beras = int(input("Masukkan Harga Beras: "))

# diskonan
f = 11/100 
g = 14/100
h = 17/100

# menghitung diskon
dm = harga_beras * f
ds = harga_beras * g
dmks = harga_beras * h

# menghitung harga beras setelah diskon
hsdm =int(harga_beras - dm)
hsds = int(harga_beras - ds)
hsdmks = int(harga_beras - dmks)

print(nama,"dengan NIM",nim,"ingin membeli beras seharga RP",harga_beras,".",
      "\nJika dia membeli beras Mawar ia harus membayar RP",hsdm,"Setelah mendapat diskon 11%.",
      "\nJika dia membeli beras Sania ia harus membayar RP",hsds,"Setelah mendapat diskon 14%.",
      "\nJika dia membeli beras Maknyus ia harus membayar RP",hsdmks,"Setelah mendapat diskon 17%.")