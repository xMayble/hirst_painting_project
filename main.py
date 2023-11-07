import colorgram

colors = colorgram.extract('hirst_img.jpg', 6)


my_list = []

# for i in range(0, len(colors)):
#     x = (colors[i].rgb[0], colors[i].rgb[1], colors[i].rgb[2])
#     my_list.append(x)

# print(my_list)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    my_list.append(new_color)

print(my_list)