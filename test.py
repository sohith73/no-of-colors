# import cairosvg  # not working 
from PIL import Image
from collections import Counter
import webcolors
import io
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

'''
problem statement 
          we will take a image's path as input and give the colors in the image
          how? 
          main
          step 1) Image Library (PIL) to handle image processing
          step 2) count colors lets use list or Counter to do the storing work 
          side 
          step 1) webcolors library to map RGB values to human-readable color names
          format of code 
          - it should be modular.
          - ot should handle errors too.
          bugs 
          1 - man they are many blues dark blue "https://stackoverflow.com/questions/26720195/how-to-calculate-a-number-of-shades-and-tints-using-a-rgb-value-in-python"
          didn't help that much but got an idea
          2- 100% problem
          3- some small colors problem 
          optimization
          - we know that resizing , 
          - we can count how many times it occurs(lets leave it for now)
          - we can sort them and display the greatest-
          - and i am ignoring small colors with no conurbation 

'''
'''
this function shoud Tries to match an RGB color (which is made up of red, green, and blue values)
to a known color name ,It looks through a list of CSS colors and calculates the "distance"
between each CSS color and the color we provided.
simply Which known color looks closest to the color we have?
'''
def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def convert_svg_to_png(image_path):
    # Convert SVG to PNG in memory
    drawing = svg2rlg(image_path)
    png_data = io.BytesIO()
    renderPM.drawToFile(drawing, png_data, fmt="PNG")
    png_data.seek(0)
    return Image.open(png_data).convert("RGB")

'''
half done 
now we need its names of them we can use css for thsi i think if found we will
give ist mane else just normal name
'''

def get_color_name(rgb_color):
    try:
        return webcolors.rgb_to_name(rgb_color, spec='css3')
    except ValueError:
        return closest_color(rgb_color)
    
'''
main task starts now we need
Opens an image and tells us what colors are in it, along with their percentages,
but skips any colors that don’t make up enough of the image (like those under 0.1%) big fix.
we will resize for optimization ,
and try sorting too.
'''

def get_colors(image_path, resize_factor=0.5, min_percentage=0.1):
    try:
        if image_path.lower().endswith('.svg'):
            image = convert_svg_to_png(image_path)
        else:
            image = Image.open(image_path).convert('RGB')
        
        if resize_factor < 1:
            image = image.resize(
                (int(image.width * resize_factor), int(image.height * resize_factor))
            )
        
        colors = image.getdata()
        color_count = Counter(colors)
        total_colors = sum(color_count.values())
        
        color_percentage = {color: (count / total_colors) * 100 for color, count in color_count.items()}
        filtered_colors = {color: perc for color, perc in color_percentage.items() if perc >= min_percentage}
        sorted_colors = sorted(filtered_colors.items(), key=lambda x: x[1], reverse=True)
        
        # Dictionary to aggregate percentages for each unique color name
        color_name_percentage = {}
        
        for color, percentage in sorted_colors:
            color_name = get_color_name(color)
            if color_name in color_name_percentage:
                color_name_percentage[color_name] += percentage
            else:
                color_name_percentage[color_name] = percentage
        sorted_color_name_percentage = sorted(color_name_percentage.items(), key=lambda x: x[1], reverse=True)
        
        return sorted_color_name_percentage
    
    except Exception as e:
        print(f"Error: {e}")
        return []

# Main function to get the image path and display the color analysis
if __name__ == "__main__":
    image_path = input("Please enter the path to your logo/image file: ")

    colors = get_colors(image_path, resize_factor=0.5, min_percentage=0.1)
    if colors:
        print("\nColors in the image (sorted by usage percentage):")
        for color_name, percentage in colors:
            print(f"Color: {color_name.capitalize()}, Percentage: {percentage:.2f}%")
    else:
        print("No colors found or image could not be processed.")
