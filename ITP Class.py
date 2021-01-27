import turtle
from PIL import Image
import math

class ITP:
    def __init__(self, im):
        self.hz = turtle.Turtle()
        turtle.colormode(255)
        self.hz.speed(0)
        self.hz.ht()
        turtle.tracer(0, 0)

        if (im.width % 2) != 0:
            self.width = im.width - 1
        else:
            self.width = im.width

        if (im.height % 2) != 0:
            self.height = im.height - 1
        else:
            self.height = im.height

        self.x_increase = 0
        self.y_increase = 0
        self.hz.penup()
        self.hz.goto(-self.width / 2, self.y_increase + self.height / 2)
        self.hz.pendown()

        self.rgb_im = im.convert('RGB')

    def processComplete(self):
        turtle.update()
        print("Finished!")
        turtle.exitonclick()

    def reset(self):
        self.x_increase = 0
        self.y_increase = 0
        self.hz.penup()
        self.hz.goto(-self.width / 2, self.y_increase + self.height / 2)
        self.hz.pendown()

    def rgbConversion(self): 
        count = -1
        index = 0
        for i in range(self.width*self.height):
            index += 1
            
            if index == 4:
                index = 0
                
            if index == 0:
                count += 1
                if count == self.width / 2:
                    self.y_increase += 2
                    count = 0
                    self.hz.penup()
                    self.hz.goto(-self.width/2, -self.y_increase + self.height/2)
                    self.hz.pendown()
                    print(f'Loading... {round(i/(self.width*self.height) * 100, 2)}%')

                self.x_increase = 2 * count

                x = 0 + self.x_increase
                y = 0 + self.y_increase
            elif index == 1:
                x = 0 + self.x_increase
                y = 1 + self.y_increase
            elif index == 2:
                x = 1 + self.x_increase
                y = 0 + self.y_increase
            elif index == 3:
                x = 1 + self.x_increase
                y = 1 + self.y_increase

            yield self.rgb_im.getpixel((x, y))
        

    def blurred(self):
        self.reset()
        self.hz.width(2)
      
        for rgb in self.rgbConversion():    
            r, g, b = rgb
            c = (r, g, b)
            self.hz.color(c)
            self.hz.forward(0.5)
            #print(f"i:{i} index:{index} rgb:{r},{g},{b} count:{count} (x,y):({x},{y})")

        self.processComplete()


    def HD(self):
        self.reset()
        self.hz.width(1)

        count = -1
        for i in range(self.width*self.height):
            count += 1
            
            if count == self.width:
                self.y_increase += 1
                count = 0
                self.hz.penup()
                self.hz.goto(-self.width / 2, -self.y_increase + self.height / 2)
                self.hz.pendown()
                print(f'Loading... {round(self.y_increase / self.height * 100, 2)}%')
                self.x_increase = count
                
            x = self.x_increase
            y = self.y_increase
            r, g, b = self.rgb_im.getpixel((x, y))
            c = (r, g, b)
            self.hz.color(c)
            self.hz.forward(1)
            self.x_increase += 1
            
        self.processComplete()

    def pixelated(self):
        self.reset()
        self.hz.width(2)

        mix = 0
        rgb4r = [0, 0, 0, 0]
        rgb4g = [0, 0, 0, 0]
        rgb4b = [0, 0, 0, 0]

        for rgb in self.rgbConversion():
            r, g, b = rgb
            
            mix_to_index = mix + 1
            if mix_to_index == 4:
                mix_to_index = 0

            rgb4r[mix_to_index] = r
            rgb4g[mix_to_index] = g
            rgb4b[mix_to_index] = b
            
            mix += 1
            if mix == 4:
                rmix = sum(rgb4r)//4
                gmix = sum(rgb4g)//4
                bmix = sum(rgb4b)//4
                c = (rmix, gmix, bmix)
                mix = 0
                self.hz.color(c)
                self.hz.forward(2)
                
        self.processComplete()

image = ITP(Image.open("cat.png"))
image.pixelated()
