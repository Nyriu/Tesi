image_dir  = './'
image_name = 'zebra_RGB.jpg'
image_suffix = '.' + image_name.split('.')[1]
image_path = image_dir + image_name

dest_dir = './WIP_processing/'

import os

if not os.path.isdir(dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    print('Generato cartella ', dest_dir)

tesi_dest_dir = '/home/nyriu/Documents/Uni/Tesi/Tesi/figure/preprocessing/'


print('Working on ', image_path)
