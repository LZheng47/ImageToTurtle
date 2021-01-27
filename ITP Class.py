import turtle
from PIL import Image


class ITP:
    def __init__(self, im):
        self.hz = turtle.Turtle()
        turtle.colormode(255)
        self.hz.speed(0)
        self.hz.ht()
        turtle.tracer(0, 0)
        # turtle.tracer(0, 0) used with turtle.update() to speed up turtle drawing process.

        if (im.width % 2) != 0:
            self.width = im.width - 1
        else:
            self.width = im.width

        if (im.height % 2) != 0:
            self.height = im.height - 1
        else:
            self.height = im.height
        # Ensures that image height and width are even, to avoid problems with effect functions.

        self.x_increase = 0
        self.y_increase = 0
        self.hz.penup()
        self.hz.goto(-self.width / 2, self.y_increase + self.height / 2)
        # Makes turtle go to upper-left coordinates of the image, while ensuring that turtle drawing is centered.
        self.hz.pendown()
        self.rgb_im = im.convert('RGB')

    def processComplete(self):
        turtle.update()
        print("Finished!")
        turtle.exitonclick()

    def reset(self):
        # Resets starting position and coord-increase variables.
        self.x_increase = 0
        self.y_increase = 0
        self.hz.penup()
        self.hz.goto(-self.width / 2, self.y_increase + self.height / 2)
        self.hz.pendown()

    def rgbConversion(self): 
        count = -1
        # count determines every 2 pixels width wise
        index = 0
        # index determines position of pixel in a 2x2 box. When index equals:
        # 0:Top-left, 1:Bottom-left, 2:Top-right, 3:Bottom-right
        for i in range(self.width*self.height):
            index += 1
            
            if index == 4:
                index = 0
                
            if index == 0:
                count += 1
                if count == self.width / 2:
                    self.y_increase += 2
                    count = 0
                    # Resets count when moving to the next row. (Down 2 pixels)
                    self.hz.penup()
                    self.hz.goto(-self.width/2, -self.y_increase + self.height/2)
                    # Positions turtle to the very left and down, depending on what row it is on.
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
        # blurred() places every 2x2 pixels from order of:
        #       top-left, bottom-left, top-right, bottom-right
        # into one row
        self.reset()
        self.hz.width(2)
        # Has width of 2 to cover every 2 rows, which had been "mushed" into 1 row

        for rgb in self.rgbConversion():    
            r, g, b = rgb
            c = (r, g, b)
            self.hz.color(c)
            self.hz.forward(0.5)
            # Moves forward by 0.5 pixels since 4 pixels are "mushed" into 2 pixels
            # print(f"i:{i} index:{index} rgb:{r},{g},{b} count:{count} (x,y):({x},{y})")

        self.processComplete()


    def HD(self):
        # HD() makes a high definition image onto Python w/ Turtle
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
        # Three lists for the rgb values of every pixels, where the pixels, from the order of:
        #       top-left, bottom-left, top-right, bottom-right
        # has the rgb values of (rgb4r[index], rgb4g[index], rgb4b[index])

        for rgb in self.rgbConversion():
            r, g, b = rgb
            
            mix_to_index = mix + 1
            if mix_to_index == 4:
                mix_to_index = 0

            rgb4r[mix_to_index] = r
            rgb4g[mix_to_index] = g
            rgb4b[mix_to_index] = b
            # Appends rgb values into their respective lists for every 4 pixels

            mix += 1
            if mix == 4:
                # Once 4 pixels' rgb values are retrieved, the average of each color value is calculated.
                rmix = sum(rgb4r)//4
                gmix = sum(rgb4g)//4
                bmix = sum(rgb4b)//4
                c = (rmix, gmix, bmix)
                mix = 0
                self.hz.color(c)
                self.hz.forward(2)
                
        self.processComplete()


res = True

picture = input("Enter the source of the image you want to draw:\n")
while(res == True):
    try:
        image = ITP(Image.open(f'{picture}'))
        break
    except FileNotFoundError:
        print("Sorry, the file name you entered was not found. \n"
              "This is case-sensitive and make sure the .png or .jpg is included.\n"
              "Please run the program again.")
        exit()

effect = input("Enter one of the effects listed below for how you want your image to turn out:\n"
               "Note: Type the effects exactly as listed.\n"
               "blurred\n"
               "HD\n"
               "pixelated\n")

while(res == True):
    try:
        exec(f'image.{effect}()')
        break
    except AttributeError:
        print("The effect you typed is invalid!\n"
              "Make sure you type one of the effects listed.\n"
              "Please run the program again.")
        exit()
