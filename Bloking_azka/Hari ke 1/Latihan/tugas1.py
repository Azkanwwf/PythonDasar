bangunDatar=int(input(" 1 = persegi\n2 = persegi panjang\n3 = trapesium\npilihlah :  "))

if bangunDatar==1:
    print("\nAnda memilih persegi.")
    sisi=float(input("Masukkan sisi : "))
    luas=sisi*sisi
    keliling=sisi*4
    print(f"Luas dari persegi adalah {luas} dan kelilingnya adalah {keliling}.")
elif bangunDatar==2:
    print("\nAnda memilih persegi panjang.")
    panjang=float(input("masukkan panjang : "))
    lebar=float(input("masukkan lebar : "))
    luas=panjang*lebar
    keliling=(2*panjang)+(2*lebar)
    print(f"Luas dari persegi panjang adalah {luas} dan kelilingnya adalah {keliling}.")
elif bangunDatar==3:
    print("\nAnda memilih trapesium")
    sisi1=float(input("masukkan sisi 1 : "))
    sisi2=float(input("masukkan sisi 2 :"))
    sisi3=float(input("masukkan sisi 3 :"))
    sisi4=float(input("masukkan sisi 4 : "))
    tinggi=float(input("masukkan tinggi"))
    luas=0.5*(sisi1+sisi2)*tinggi
    keliling=sisi1+sisi2+sisi3+sisi4
    print(f"Luas dari trapesium adalah {luas} dan kelilingnya adalah {keliling}.")
else:
    print("EE HOOH LAHH")
