from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from graph import Rectangle,Circle,Triangle
from point import Point
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
width = 1024
height = 768
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)
# 新建一个矩形
cmd = input('要画什么图形：')
if cmd == 'r':
    for i in range(600):
        center = Point(random.randint(1,1024),random.randint(1,768))
        height = random.randint(10,50)
        width = random.randint(10,50)
        r = Rectangle(center,width,height)
        draw.line(r.toPoints(),fill=rndColor(),width=2)
elif cmd == 't':
    for i in range(500):
        p1 = Point(random.randint(i,i*5),random.randint(i,i*5))
        p2 = Point(random.randint(i,i*5),random.randint(i,i*5))
        p3 = Point(random.randint(i,i*5),random.randint(i,i*5))
        t = Triangle(p1,p2,p3)
        draw.line(t.toPoints(),fill=rndColor(),width=2)
else:
    for i in range(500):
        center = Point(random.randint(1,1024),random.randint(1,768))
        radius = random.randint(10,50)
        c = Circle(center,radius)
        draw.ellipse((c.center.X-radius, c.center.Y-radius, c.center.X+radius, c.center.Y+radius), fill=rndColor())
image.save('graph.jpg', 'jpeg')