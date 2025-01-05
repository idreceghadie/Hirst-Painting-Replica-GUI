from turtle import Turtle, Screen
import colorgram, random

colors = colorgram.extract('image.jpg', 40)

color_list = []
for i in range(len(colors)):
    rgb = colors[i].rgb
    rgb_tuple = (rgb.r, rgb.g, rgb.b)
    color_list.append(rgb_tuple)

print(color_list)


screen = Screen()
screen.colormode(255)

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]
t = Turtle()

t.hideturtle()
t.teleport(-300,-300)
j = 0
for _ in range(10):
    t.teleport(x = -300,y = (70*j) - 300)
    dot_color = random.choice(color_list)
    t.dot(20,dot_color)
    j += 1
    i = 0
    for _ in range(10):
        dot_color = random.choice(color_list)
        t.teleport(70*i - 300)
        t.dot(20, dot_color)
        i += 1

screen.exitonclick()