import turtle
from PIL import Image

hz = turtle.Turtle()
turtle.colormode(255)
hz.speed(0)
hz.ht()
turtle.tracer(0, 0)

im = Image.open('cat.png')

if (im.width % 2) != 0:
    width = im.width - 1
else:
    width = im.width

if (im.height % 2) != 0:
    height = im.height - 1
else:
    height = im.height

if width < 600 or height < 600:
    turtle.setup(width+800, height+600, 0, 0)
    turtle.screensize(width+800, height+600)

rgb_im = im.convert('RGB')
rgb4r = [0, 0, 0, 0]
rgb4g = [0, 0, 0, 0]
rgb4b = [0, 0, 0, 0]
pxl_x = [0, 0, 0, 0]
pxl_y = [0, 0, 0, 0]

count = -1
x_increase = 0
y_increase = 0
hz.penup()
hz.goto(-width/2, y_increase+height/2)
hz.pendown()
hz.width(2)
# cool blurred effect
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
    pxl_x[index] = x
    pxl_y[index] = y

    c = (r, g, b)
    hz.color(c)
    hz.forward(0.5)

    #print(f"i:{i} index:{index} rgb:{r},{g},{b} count:{count} (x,y):({x},{y})")

turtle.update()
print("Finished!")
turtle.exitonclick()
