import os,math
from PIL import Image

input_file_path="input"
output_file_path="output"

file_names=os.listdir(input_file_path)

spritesheet_width=3

input_file_array=[]
x_size_array=[]
y_size_array=[]

for image_name in file_names:
    image=Image.open(os.path.join(input_file_path,image_name))
    size=image.size
    input_file_array.append(image)
    x_size_array.append(size[0])
    y_size_array.append(size[1])

cell_size=(max(x_size_array),max(y_size_array))
sprite_number=len(input_file_array)

x=(spritesheet_width)*cell_size[0]
y=(math.ceil(sprite_number/spritesheet_width))*cell_size[1]

output=Image.new("RGBA",(x,y),(0,0,0,0))

pointer_x=0
pointer_y=0
for image in input_file_array:
    if pointer_x==spritesheet_width:
        pointer_x=0
        pointer_y+=1
    image_y_offset=cell_size[1]-image.size[1]  #so the image is placed at the bottom right of each cell
    output.paste(image,(pointer_x*cell_size[0],pointer_y*cell_size[1]+image_y_offset))
    pointer_x+=1

output.save(os.path.join(output_file_path,"output.png"))