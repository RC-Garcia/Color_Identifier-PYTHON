# color_identifier.py

from PIL import Image
import webcolors

def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_hex_code(rgb_color):
    return webcolors.rgb_to_hex(rgb_color)

def identify_color(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    colors = image.getcolors(image.size[0] * image.size[1])
    most_frequent_color = max(colors, key=lambda item: item[0])[1]
    return most_frequent_color

def main():
    print("Color Identifier")
    
    image_path = input("Enter the path to the image file: ")
    rgb_color = identify_color(image_path)
    hex_color = get_hex_code(rgb_color)
    
    print(f"Identified Color in RGB: {rgb_color}")
    print(f"Hexadecimal Code: {hex_color}")
    print(f"Closest Web Color Name: {closest_color(rgb_color)}")

if __name__ == "__main__":
    main()
