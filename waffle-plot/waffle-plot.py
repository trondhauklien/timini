##################################
#                 __  __ _       #
#                / _|/ _| |      #
# __      ____ _| |_| |_| | ___  #
# \ \ /\ / / _` |  _|  _| |/ _ \ #
#  \ V  V / (_| | | | | | |  __/ #
#   \_/\_/ \__,_|_| |_| |_|\___| #
#                                #
##################################

# Plot an image of a waffle using a waffle diagram
# provided by the pywaffle module for matplotlib

# pip3 install matplotlib
# pip3 install pywaffle
# pip3 install Pillow

import matplotlib.pyplot as plt
from pywaffle import Waffle
from PIL import Image

# IMAGE
color_list = []
pixel_list = []

with Image.open("waffle.png") as img:
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            y = 24 - y
            r, g, b = pixels[x, y]
            p = f"#{r:02x}{g:02x}{b:02x}"
            pixel_list.append(1)
            color_list.append(p)

fig = plt.figure(
    FigureClass=Waffle, 
    rows=25, 
    columns=25, 
    values=pixel_list,
    colors=color_list
    #figsize=(5, 3)
)

plt.show()