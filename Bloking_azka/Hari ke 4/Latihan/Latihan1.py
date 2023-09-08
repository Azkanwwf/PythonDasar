import tkinter as tk

def hitung_total():
    try:
        harga = float(entry_harga.get())
        jumlah = int(entry_jumlah.get())
        total = harga * jumlah
        label_total.config(text=f"Total Harga: Rp {total:.2f}")
    except ValueError:
        label_total.config(text="Masukkan harga dan jumlah yang valid")

def tambahkan_item():
    item = entry_item.get()
    harga = entry_harga.get()
    jumlah = entry_jumlah.get()
    
    if item and harga and jumlah:
        listbox_item.insert(tk.END, f"{item} - Rp {harga} x {jumlah}")
        hitung_total()
    else:
        label_total.config(text="Isi semua kolom terlebih dahulu")

app = tk.Tk()
app.title("Program Kasir")
app.configure(bg="Light Green")

frame_input = tk.Frame(app, bg= "Light Green")
frame_input.pack(pady=10)

label_item = tk.Label(frame_input, text="Item:")
label_item.grid(row=0, column=0, padx=5)

entry_item = tk.Entry(frame_input)
entry_item.grid(row=0, column=1, padx=5)

label_harga = tk.Label(frame_input, text="Harga:")
label_harga.grid(row=1, column=0, padx=5)

entry_harga = tk.Entry(frame_input)
entry_harga.grid(row=1, column=1, padx=5)

label_jumlah = tk.Label(frame_input, text="Jumlah:")
label_jumlah.grid(row=2, column=0, padx=5)

entry_jumlah = tk.Entry(frame_input)
entry_jumlah.grid(row=2, column=1, padx=5)

tombol_tambah = tk.Button(frame_input, text="Tambah Item", command=tambahkan_item)
tombol_tambah.grid(row=3, columnspan=2, pady=10)

listbox_item = tk.Listbox(app)
listbox_item.pack(padx=10, pady=5, fill=tk.BOTH)

frame_total = tk.Frame(app)
frame_total.pack(pady=10)

label_total = tk.Label(frame_total, text="Total Harga: Rp 0.00")
label_total.pack()

app.mainloop()