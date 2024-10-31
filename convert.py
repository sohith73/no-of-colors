import cairosvg
from PIL import Image
import io

def convert_svg_to_jpeg(svg_path, jpeg_path):
    # Convert SVG to PNG in memory
    png_data = cairosvg.svg2png(url=svg_path)
    
    # Convert PNG data to JPEG
    image = Image.open(io.BytesIO(png_data))
    jpeg_io = io.BytesIO()
    image.convert("RGB").save(jpeg_io, format="JPEG")
    
    # Save JPEG to local file
    with open(jpeg_path, 'wb') as jpeg_file:
        jpeg_file.write(jpeg_io.getvalue())

# Example usage
svg_file_path = './digital-river-logo-black-blue.svg'
jpeg_file_path = './output'
convert_svg_to_jpeg(svg_file_path, jpeg_file_path)