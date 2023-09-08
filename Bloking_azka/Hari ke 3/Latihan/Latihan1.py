import turtle

pen=turtle.Turtle()

def persegiPanjang(panjang, lebar, xpp, ypp):
    panjang=120
    lebar=80
    xpp=-550
    ypp=100
    pen.penup()
    pen.goto(xpp,ypp)
    pen.pendown()
    pen.forward(panjang)
    pen.right(90)
    pen.forward(lebar)
    pen.right(90)
    pen.forward(panjang)
    pen.right(90)
    pen.forward(lebar)
    pen.right(90)

def segitiga(sisit,sisim,xst,yst):
    sisit=75
    sisim=107
    xst=-350
    yst=100
    pen.penup()
    pen.goto(xst,yst)
    pen.pendown()
    pen.forward(sisit)
    pen.right(90)
    pen.forward(sisit)
    pen.right(135)
    pen.forward(sisim)
    pen.right(135)

def trapesium(sisi1, sisi2, tinggi,xtp,ytp):
    sisi1=100
    sisi2=168
    tinggi=80
    xtp=-150
    ytp=100
    pen.penup()
    pen.goto(xtp,ytp)
    pen.pendown()
    pen.forward(sisi1)
    pen.right(65)
    pen.forward(tinggi)
    pen.right(115)
    pen.forward(sisi2)
    pen.right(115)
    pen.forward(tinggi)
    pen.right(65)

def jajargenjang(sisi, tinggi,xjg,yjg):
    sisi=120
    tinggi=100
    xjg=125
    yjg=100
    pen.penup()
    pen.goto(xjg,yjg)
    pen.pendown()
    pen.forward(sisi)
    pen.right(135)
    pen.forward(tinggi)
    pen.right(45)
    pen.forward(sisi)
    pen.right(135)
    pen.forward(tinggi)
    pen.right(45)

def belahKetupat(sisi,xbt,ybt):
    sisi=60
    xbt=350
    ybt=100
    pen.penup()
    pen.goto(xbt,ybt)
    pen.pendown()
    pen.right(65)
    pen.forward(sisi)
    pen.right(50)
    pen.forward(sisi)
    pen.right(130)
    pen.forward(sisi)
    pen.right(50)
    pen.forward(sisi)


persegiPanjang(120, 80, -250, 200)
segitiga(75, 107, 0, 200)
trapesium(100, 125, 100, 250, 200)
jajargenjang(120, 100, 200, 0)
belahKetupat(65, 65, 65)

turtle.done()