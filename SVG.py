from PIL import Image
from wand.image import Image as WandImage
# from wand.image import Image as WandImage
from wand.color import Color
import io

# def convert_svg_to_webp(svg_path, webp_path):
#     with WandImage(filename=svg_path) as img:
#         img.format = 'png'
#         png_data = img.make_blob()
#     with Image.open(io.BytesIO(png_data)) as image:
#         image.save(webp_path, format="WEBP")

# Example usage

# from PIL import Image
# from wand.image import Image as WandImage
# import io

# def convert_svg_to_png(svg_path, png_path):
#     with WandImage(filename=svg_path, format='png') as img:
#         img.background_color = Color('transparent')
#         img.alpha_channel = 'activate'
#         png_data = img.make_blob()
#     with Image.open(io.BytesIO(png_data)) as image:
#         image.save(png_path, format="PNG")

def convert_svg_to_png(svg_path, png_path):
    with WandImage(filename=svg_path) as img:
        img.background_color = Color('transparent')
        img.alpha_channel = 'activate'
        img.format = 'png'
        png_data = img.make_blob(format='png')
    
    with Image.open(io.BytesIO(png_data)) as image:
        image = image.convert("RGBA")
        image.save(png_path, format="PNG")
        
convert_svg_to_png("T.svg", "output1.png")

# convert_svg_to_webp("T.svg", "output.webp")
