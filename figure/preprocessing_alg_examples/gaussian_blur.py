import cv2
import numpy as np
from matplotlib import pyplot as plt

from my_globals import image_path, image_name, image_dir, dest_dir, image_suffix

#print('GaussianBlur ', image_path)

img = cv2.imread(image_path, 0)

save_path = dest_dir +  'GRAY' + image_suffix
cv2.imwrite(save_path, img)


blurred_img = cv2.GaussianBlur(img, (7,7), 2)

save_path = dest_dir +  'gaussian_blur_example' + image_suffix
cv2.imwrite(save_path, blurred_img)
print('GaussianBlur saved in ', save_path)

