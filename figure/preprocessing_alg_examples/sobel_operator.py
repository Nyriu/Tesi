import cv2
import numpy as np
from matplotlib import pyplot as plt

from my_globals import image_path, image_name, image_dir, dest_dir, image_suffix

#print('Sobel ', image_path)

img = cv2.imread(dest_dir + 'masked.jpg', 0)

gx = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
gy = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

gx = cv2.convertScaleAbs(gx)
gy = cv2.convertScaleAbs(gy)

save_path = dest_dir +  'gx' + image_suffix
cv2.imwrite(save_path, gx)
print('Gx saved in ', save_path)

save_path = dest_dir +  'gy' + image_suffix
cv2.imwrite(save_path, gy)
print('Gy saved in ', save_path)

abs_gx = cv2.convertScaleAbs(gx)
abs_gy = cv2.convertScaleAbs(gy)

g = cv2.addWeighted(abs_gx, 0.5, abs_gy, 0.5, 0)


save_path = dest_dir +  'g' + image_suffix
cv2.imwrite(save_path, g)
print('G saved in ', save_path)
