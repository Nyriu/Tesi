import cv2
import numpy as np
from matplotlib import pyplot as plt

from my_globals import image_path, image_name, image_dir, dest_dir, image_suffix

#print('Sobel ', image_path)

img = cv2.imread(image_path, 0)


circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=1, minDist=10, param1=250, param2=30, minRadius=5, maxRadius=30)


img = cv2.imread(image_path)
if circles is not None:
    print(len(circles[0,:]))
    for n, i in enumerate(circles[0,:]):
        cx = i[0]
        cy = i[1]
        r = i[2]
        center = (cx, cy)
        cv2.circle(img, center, r, (0,0,255))


save_path = dest_dir +  'hough_circles_example' + image_suffix
cv2.imwrite(save_path, img)
print('Hough Circles saved in ', save_path)
