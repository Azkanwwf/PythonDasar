batas_atas = int(input("Masukkan angka: "))

for angka in range(1, batas_atas + 1):
    if angka % 2 == 0:
        print(f"{angka} adalah angka genap")
    else:
        print(f"{angka} adalah angka ganjil")