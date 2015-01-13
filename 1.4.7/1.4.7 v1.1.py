import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw            

def add_border(image):
    width, height = image.size
    width += 100
    height += 100
    new_image = image.resize(width, height)
    directory = os.getcwd()
    new_image_filename = os.path.join(directory, filename + '2' + '.png')
    new_image.save(new_image_filename) 
'''    PIL.ImageDraw.Draw(fill= 0, 0, 0)
    image_with_border = image.paste(new_image, image)'''
def add_border_all_images(directory=None):
    images = []
    for image in images:
        add_border
    if directory == None:
        directory = os.getcwd()
    new_directory = os.path.join(directory, 'modified')