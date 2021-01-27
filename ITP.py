import turtle
from PIL import Image
import math

#picture = input("Enter the source of the image you want to draw:\n")
#im = Image.open(f'{picture}')
im = Image.open("test.png")
hz = turtle.Turtle()
turtle.colormode(255)
hz.speed(0)
hz.ht()
turtle.tracer(0, 0)

if (im.width % 2) != 0:
    width = im.width - 1
else:
    width = im.width

if (im.height % 2) != 0:
    height = im.height - 1
else:
    height = im.height

'''
if width < 600 or height < 600:
    turtle.setup(width+800, height+600, 0, 0)
    turtle.screensize(width+800, height+600)
'''

rgb_im = im.convert('RGB')

print(height, width)


def processComplete():
    turtle.update()
    print("Finished!")
    turtle.exitonclick()

def blurred():
    x_increase = 0
    y_increase = 0
    hz.penup()
    hz.goto(-width / 2, y_increase + height / 2)
    hz.pendown()
    count = -1
    hz.width(2)
    for i in range(width*height):
        index = i
        while index >= 4:
            index -= 4
        if index == 0:
            count += 1
            if count == width / 2:
                y_increase += 2
                count -= width / 2
                hz.penup()
                hz.goto(-width/2, -y_increase + height/2)
                hz.pendown()
                print(f'Loading... {round(i/(width*height) * 100, 2)}%')
            x_increase = 2 * count
            x = 0 + x_increase
            y = 0 + y_increase
        elif index == 1:
            x = 0 + x_increase
            y = 1 + y_increase
        elif index == 2:
            x = 1 + x_increase
            y = 0 + y_increase
        elif index == 3:
            x = 1 + x_increase
            y = 1 + y_increase
        r, g, b = rgb_im.getpixel((x, y))
        c = (r, g, b)
        hz.color(c)
        hz.forward(0.5)
        # print(f"i:{i} index:{index} rgb:{r},{g},{b} count:{count} (x,y):({x},{y})")
    processComplete()


def HD():
    x_increase = 0
    y_increase = 0
    hz.penup()
    hz.goto(-width / 2, y_increase + height / 2)
    hz.pendown()
    count = -1
    hz.width(1)
    for i in range(width*height):
        count += 1
        if count == width:
            y_increase += 1
            count -= width
            hz.penup()
            hz.goto(-width / 2, -y_increase + height / 2)
            hz.pendown()
            print(f'Loading... {round(y_increase / height * 100, 2)}%')
            x_increase = count
        x = x_increase
        y = y_increase
        r, g, b = rgb_im.getpixel((x, y))
        c = (r, g, b)
        hz.color(c)
        hz.forward(1)
        x_increase += 1
    processComplete()

def pixelated():
    x_increase = 0
    y_increase = 0
    mix = 0
    hz.penup()
    hz.goto(-width / 2, y_increase + height / 2)
    hz.pendown()
    count = -1
    hz.width(2)
    rgb4r = [0, 0, 0, 0]
    rgb4g = [0, 0, 0, 0]
    rgb4b = [0, 0, 0, 0]
    for i in range(width*height):
        index = i
        while index >= 4:
            index -= 4
        if index == 0:
            count += 1
            if count == width / 2:
                y_increase += 2
                count -= width / 2
                hz.penup()
                hz.goto(-width/2, -y_increase + height/2)
                hz.pendown()
                print(f'Loading... {round(i/(width*height) * 100, 2)}%')
            x_increase = 2 * count
            x = 0 + x_increase
            y = 0 + y_increase
        elif index == 1:
            x = 0 + x_increase
            y = 1 + y_increase
        elif index == 2:
            x = 1 + x_increase
            y = 0 + y_increase
        elif index == 3:
            x = 1 + x_increase
            y = 1 + y_increase
        r, g, b = rgb_im.getpixel((x, y))
        rgb4r[index] = r
        rgb4g[index] = g
        rgb4b[index] = b
        mix += 1
        if mix == 4:
            rmix = math.floor(sum(rgb4r)/4)
            gmix = math.floor(sum(rgb4b)/4)
            bmix = math.floor(sum(rgb4g)/4)
            c = (rmix, gmix, bmix)
            mix -= 4
            hz.color(c)
            hz.forward(2)
        #print(f'{rgb4r[index]} {rgb4g[index]} {rgb4b[index]} | {rmix} {gmix} {bmix} | Mix: {mix}')
    processComplete()
'''
effect = input("Enter 'blurred' or 'HD' for the effect you want:\n")

if effect == "blurred":
    blurred()
elif effect == "HD":
    HD()
'''

pixelated()