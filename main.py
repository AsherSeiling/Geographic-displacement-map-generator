import math
import PIL
from PIL import Image
import time


# Global Vars
height_data = []
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
    def eliminate_neg():
        pass



# All the code that will be run on start
read_txt()
print(len(height_data))
# Finds the side resolutions
side_res = math.floor(math.sqrt(len(height_data)))
print(side_res)
