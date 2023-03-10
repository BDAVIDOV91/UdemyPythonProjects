import turtle as tur
import colorsys as cs

tur.setup(800,800)
tur.speed(0)
tur.width(2)
tur.bgcolor('black')

for j in range (25):
    for i in range (15):
        tur.color(cs.hsv_to_rgb(i/15, j/25, 1))
        tur.right(90)
        tur.circle(200-j*4, 90)
        tur.left(90)
        tur.circle(200-j*4, 90)
        tur.right(180)
        tur.circle(50, 24)
        
# Add text under the flower
tur.penup()
tur.goto(0, -370)
tur.pendown()
tur.color('Red')
tur.write("I Love You, Aleks", align='center', font=('Arial', 20, 'bold'))

tur.hideturtle()
tur.done()