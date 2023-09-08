import turtle as t

# Atur awal
t.speed(5)  # Kecepatan menggambar rendah
t.bgcolor("grey")  # Latar belakang putih
t.penup()
t.goto(-150, 100)  # Pindahkan kursor ke posisi awal garis merah
t.pendown()

# Gambar garis merah pertama
t.color("red")  # Warna merah
t.begin_fill()
t.forward(300)  # Panjang garis merah
t.right(90)  # Putar 90 derajat
t.forward(40)  # Lebar garis merah
t.right(90)  # Putar 90 derajat
t.forward(300)  # Panjang garis merah
t.right(90)  # Putar 90 derajat
t.forward(40)  # Lebar garis merah
t.end_fill()

# Pindahkan kursor ke posisi garis putih
t.penup()
t.goto(-150, 60)
t.pendown()

# Gambar garis putih
t.color("white")  # Warna putih
t.begin_fill()
t.forward(-40)  # Panjang garis putih
t.right(90)  # Putar 90 derajat
t.forward(300)  # Lebar garis putih
t.left(90)  # Putar 90 derajat
t.forward(40)  # Panjang garis putih
t.end_fill()

# Tunggu sampai pengguna menutup jendela
t.hideturtle()
t.done()
