import PIL
import matplotlib.pyplot as plt
import os.path
import PIL.ImageDraw            

def add_border_all_images(directory=None):
    images = []  #list of images  
    if directory == None:
        directory = os.getcwd()   
    new_directory = os.path.join(directory, 'modified')
    directory_list = os.listdir(directory)
    for entry in directory_list: 
        absolute_filename = os.path.join(new_directory, entry) # opens image and adds it to the list
        try:
            image = PIL.Image.open(absolute_filename)
            images += [image]
        except IOError:
            pass
    try:
        os.mkdir(new_directory)  # creates new directory if it doesn't already exist
    except OSError:
        pass 
    for image in images: # adds a border to the images and saves it
        new_image_filename = os.path.join(absolute_filename + '2' + '.png')
        image.save(new_image_filename)
        