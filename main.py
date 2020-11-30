import math, PIL, time
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
        height_data.sort()
        lowest_value = height_data[0]
        if lowest_value < 0:
            lowest_value_con = -lowest_value

        if lowest_value < 0:
            add_value = lowest_value_con
        else:
            add_value = lowest_value

        for x in height_data:
            convert_RBG.adjusted_data.append(x + add_value)

        def RGB_conversion():
            pass



# All the code that will be run on start
read_txt()
print(len(height_data))
# Finds the side resolutions
side_res = math.floor(math.sqrt(len(height_data)))
print(side_res)
convert_RBG.eliminate_neg()
