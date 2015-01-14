import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw            

def add_border_all_images(directory=None):
    images = []
    files = []     
    if directory == None:
        directory = os.getcwd()   
    directory_list = os.listdir(directory)
    new_directory = os.path.join(directory, 'modified')
    for entry in directory_list:
        absolute_filename = os.path.join(new_directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            files += [entry]
            images += [image]
        except IOError:
            pass
    try:
        os.mkdir(new_directory)
    except OSError:
        pass 
    return images, files
    for image in images:
        new_image_filename = os.path.join(absolute_filename + '2' + '.png')
        new_image.save(new_image_filename) 