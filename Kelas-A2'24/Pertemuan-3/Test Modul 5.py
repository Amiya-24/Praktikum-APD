# kamu = "malas makan"
# kamu = input("kamu kenyang, lapar, atau malas: ")
# if kamu == "lapar":
#     print("kamu pergi makan")
# elif kamu == "kenyang":
#     print("kamu pergi tidur")
# elif kamu == "malas":
#     print("kamu pemalas")
# else:
#     print("ga jelas lu")


# angka = int(input("Masukkan angka: "))
# result = "Genap" if angka % 2 == 0 else "Ganjil"
# print(angka, "adalah angka",result)


print("""
====================
Kalkulator Sederhana
1.+
2.-
3.*
4./
====================
""")
fitur = int(input("pilih fitur : "))
match fitur :
    case 1:
        a =int(input("Masukkan Angka 1 : "))
        b =int(input("Masukkan Angka 2 : "))
        c = a + b
        print(f"hasil penjumlahan angka 1 dan 2 adalah {c}")
    case 2:
        a =int(input("Masukkan Angka 1 : "))
        b =int(input("Masukkan Angka 2 : "))
        c = a - b
        print(f"hasil pengurangan angka 1 dan 2 adalah {c}")
    case 3:
        a =int(input("Masukkan Angka 1 : "))
        b =int(input("Masukkan Angka 2 : "))
        c = a * b
        print(f"hasil perkalian angka 1 dan 2 adalah {c}")
    case 4:
        a =int(input("Masukkan Angka 1 : "))
        b =int(input("Masukkan Angka 2 : "))
        c = a / b
        print(f"hasil pembagian angka 1 dan 2 adalah {c}")
    case _:
        print("banyak banar")


# nilai = int(input("Masukkan nilai anda : "))

# if nilai > 100 :
#     print("nilai tidak memenuhi syarat")
# elif nilai >= 80 :
#     if nilai >= 90 and nilai <= 100 :
#         print("nilai anda A+")
#     if nilai >=80 and nilai < 90 :
#         print("nilai anda A-")
# elif nilai >=70 :
#     if nilai >=75 and nilai < 80 :
#         print("nilai anda B+")
#     if nilai >= 70 and nilai < 75 :
#         print("nilai anda B-")
# else:
#     print("nilai anda tidak memenuhi syarat")

# no = 10
# if no % 2 == 0:
#     print("Genap")
# else:
#     print("Ganjil")