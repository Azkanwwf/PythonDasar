import turtle as t
import math

# Fungsi untuk menggambar teks pada sudut tertentu
def draw_text_at_angle(text, radius, angle):
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    t.penup()
    t.goto(x, y)
    t.setheading(-angle)
    t.pendown()
    t.write(text, align="center", font=("Arial", 12, "normal"))
    t.penup()
    t.goto(0, -150)  # Kembali ke pusat lingkaran
    t.setheading(0)  # Atur arah kursor ke awal

# Atur awal
t.speed(4)  # Kecepatan menggambar rendah
t.bgcolor("grey")  # Latar belakang abu-abu
t.color("white")  # Warna tinta putih
t.penup()
t.goto(0, -150)  # Pindahkan kursor ke tengah layar
t.pendown()

# Gambar lingkaran luar
t.begin_fill()
t.circle(150)
t.end_fill()

# Gambar lingkaran putih yang lebih besar
t.penup()
t.goto(0, -30)  # Pindahkan kursor ke posisi lingkaran putih
t.pendown()
t.color("white")  # Warna lingkaran putih
t.begin_fill()
t.circle(30)
t.end_fill()

# Menggambar garis lingkaran hitam
t.penup()
t.goto(0, -150)  # Pindahkan kursor ke pusat lingkaran
t.pendown()
t.color("black")  # Warna garis hitam
t.circle(150)

# Menggambar teks "SEKOLAH" pada sudut-sudut di sekitar lingkaran putih
text = "SEKOLAH"
num_chars = len(text)
angle_increment = 360 / num_chars

for i in range(num_chars):
    draw_text_at_angle(text[i], 50, i * angle_increment)

# Tunggu sampai pengguna menutup jendela
t.hideturtle()
t.done()
