class Contact:
    def __init__(self, nama, noTelepon, email):
        self.nama=nama
        self.noTelepon=noTelepon
        self.email=email
    def tampilkanInfo(self):
        print(f"Nama : {self.nama}")
        print(f"Nomor Telepon : {self.noTelepon}")
        print(f"Email : {self.email}")
        print()

class AddressBook:
    def __init__(self):
        self.daftarKontak=[]
    def tambahKontak(self,kontak):
        self.daftarKontak.append(kontak)
    def tampilkanSemuaKontak(self):
        print("\nDaftar Kontak :")
        for kontak in self.daftarKontak:
            kontak.tampilkanInfo()

if __name__=="__main__":
    addressBook=AddressBook()
    while True:
        print("Menu :")
        print("1. Tambah Kontak")
        print("2. Tampilkan Semua Kontak")
        print("3. Keluar")
        pilihan=input("Pilih menu (1/2/3) : ")

        if pilihan=="1":
            nama=input("\nNama : ")
            noTelepon=input("Nomor Telepon : ")
            email=input("Email : ")
            kontakBaru=Contact(nama, noTelepon, email)
            addressBook.tambahKontak(kontakBaru)
        elif pilihan=="2":
            addressBook.tampilkanSemuaKontak()
        elif pilihan=="3":
            break
        else:
            print("Yang bener bener ajah")