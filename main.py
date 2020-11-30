import math, PIL
from PIL import Image


# Global Vars
height_data = []
RGB_values = []
file_path = 'Exaple_terrain_height_data.txt'
side_res = 0

# Reads data from TXT file
def read_txt():
    my_file = open(file_path)
    read_lines = my_file.readlines()
    lines_str = []
    for i in read_lines:
        lines_str.append(i)
    read_without_n = [x[:-1] for x in read_lines]
    lines_str = []
    for i in read_without_n:
        height_data.append(math.floor(float(i)))
    converted_height_data = []
    read_without_n = []

# Converts to RGB values
class convert_RBG:
    adjusted_data = []
    def eliminate_neg():
        temp_list = []
        for x in height_data:
            temp_list.append(x)

        temp_list.sort()
        lowest_value = temp_list[0]
        if lowest_value < 0:
            lowest_value_con = -lowest_value

        if lowest_value < 0:
            add_value = lowest_value_con
        else:
            add_value = lowest_value

        for x in height_data:
            convert_RBG.adjusted_data.append(x + add_value)
        temp_list = []


    def RGB_conversion():
        # Finds highest_value
        temp_list = []
        for x in convert_RBG.adjusted_data:
            temp_list.append(x)
        temp_list.sort()
        temp_list.reverse()
        highest_value = temp_list[0]
        temp_list = []

        # Finds the number to devide by to find the RGB value
        dev_factor = highest_value / 255
        for x in convert_RBG.adjusted_data:
            RGB_values.append(math.floor(x / dev_factor))

# Makes the Image
def create_image():
    im = PIL.Image.new(mode = "RGB", size = (side_res, side_res))

    y_current = 0
    x_current = 0

    for i in RGB_values:
        placepixel = True
        im.putpixel((x_current, y_current), (i, i, i, 255))
        if x_current >= side_res-1:
            y_current += 1
            x_current = 0
            placepixel = False
        if y_current == side_res:
            im.save("Image.png")
        if placepixel == True:
            x_current += 1

# All the code that will be run on start
read_txt()

# Finds the side resolutions
side_res = math.floor(math.sqrt(len(height_data)))

convert_RBG.eliminate_neg()
convert_RBG.RGB_conversion()
create_image()
