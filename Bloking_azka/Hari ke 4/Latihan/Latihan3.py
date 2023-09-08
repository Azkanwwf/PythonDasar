import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Program Data Siswa")
window.geometry("500x500")

canvas=tk.Canvas(window,bg="blue")
canvas.pack(fill="both",expand=True)

judulFont=("Consolas",20,"bold")
judul=tk.Label(canvas, text="DATA SISWA PPLG",font=judulFont,bg="light blue")
judul.grid(row=0,column=0,columnspan=5,pady=10)

inputFrame=ttk.Frame(canvas)
inputFrame.grid(row=1,column=0,columnspan=5,padx=10,pady=10)

namaLengkapLabel=ttk.Label(inputFrame, text="Nama Lengkap")
namaLengkapLabel.grid(row=0,column=0,sticky="W")
namaLengkapEntry=ttk.Entry(inputFrame, width=75)
namaLengkapEntry.grid(row=1,column=0)

tanggalLahirLabel=ttk.Label(inputFrame, text="Tanggal Lahir")
tanggalLahirLabel.grid(row=2,column=0,sticky="W")
tanggalLahirEntry=ttk.Entry(inputFrame, width=75)
tanggalLahirEntry.grid(row=3,column=0)

asalSekolahLabel=ttk.Label(inputFrame, text="Asal Sekolah")
asalSekolahLabel.grid(row=4,column=0,sticky="W")
asalSekolahEntry=ttk.Entry(inputFrame, width=75)
asalSekolahEntry.grid(row=5,column=0)

nisnLabel=ttk.Label(inputFrame, text="NISN")
nisnLabel.grid(row=6,column=0,sticky="W")
nisnEntry=ttk.Entry(inputFrame, width=75)
nisnEntry.grid(row=7,column=0)

namaAyahLabel=ttk.Label(inputFrame, text="Nama Ayah")
namaAyahLabel.grid(row=8,column=0,sticky="W")
namaAyahEntry=ttk.Entry(inputFrame, width=75)
namaAyahEntry.grid(row=9,column=0)

namaIbuLabel=ttk.Label(inputFrame, text="Nama Ibu")
namaIbuLabel.grid(row=10,column=0,sticky="W")
namaIbuEntry=ttk.Entry(inputFrame, width=75)
namaIbuEntry.grid(row=11,column=0)

noTelpLabel=ttk.Label(inputFrame, text="No Telepon")
noTelpLabel.grid(row=12,column=0,sticky="W")
noTelpEntry=ttk.Entry(inputFrame, width=75)
noTelpEntry.grid(row=13,column=0)

alamatLabel=ttk.Label(inputFrame, text="Alamat Rumah")
alamatLabel.grid(row=14,column=0,sticky="W")
alamatEntry=ttk.Entry(inputFrame, width=75)
alamatEntry.grid(row=15,column=0)

hapus=tk.Button(canvas, text="Hapus",bg="cyan")
hapus.grid(row=2,column=0,padx=115,sticky="W")

simpan=tk.Button(canvas, text="Simpan",bg="cyan")
simpan.grid(row=2,column=1,sticky="W")

window.mainloop()