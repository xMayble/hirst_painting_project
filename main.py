# import colorgram

# colors = colorgram.extract('hirst_img.jpg', 30)


# color_list = []

# # for i in range(0, len(colors)):
# #     x = (colors[i].rgb[0], colors[i].rgb[1], colors[i].rgb[2])
# #     my_list.append(x)

# # print(my_list)


# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     color_list.append(new_color)

# print(color_list)

#PART 2: DRAWING OUT THE ART

import turtle as t
import random
color_list = [(249, 248, 244), (250, 245, 248), (243, 250, 246), (236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
t.colormode(255)

# # Set up the turtle
# t.speed("fastest")
# t.hideturtle()
# t.pensize(10)

# # Draw circles with different colors
# for i in range(10):
#     for j in range(10):
#         t.dot(20, random.choice(color_list))
#         t.penup()
#         t.forward(50)
#         t.pendown()
#      # Move to the next row
#     t.penup()
#     t.goto(0, (i+1)*60)  # Adjust the spacing between rows
#     t.pendown()

tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100


for dot_count in range(1, num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
     


screen = t.Screen()
screen.exitonclick()


