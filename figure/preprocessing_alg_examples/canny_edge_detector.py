import cv2
import numpy as np
from matplotlib import pyplot as plt

from my_globals import image_path, image_name, image_dir, dest_dir, image_suffix

#print('Sobel ', image_path)

img = cv2.imread(dest_dir+'masked.jpg', 0)

img = cv2.GaussianBlur(img, (3,3), 1)
img = cv2.equalizeHist(img)

c_edgs = cv2.Canny(img, threshold1=160, threshold2=320, apertureSize=3)

save_path = dest_dir +  'canny_example' + image_suffix
cv2.imwrite(save_path, c_edgs)
print('Canny saved in ', save_path)
