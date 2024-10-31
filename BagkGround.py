from rembg import remove 
from PIL import Image 

input_path =  'E:\programming\Python\BUSIBUD\output1.png' 
output_path = 'E:\programming\Python\BUSIBUD\output100.png' 

input = Image.open(input_path) 
output = remove(input) 
output.save(output_path) 