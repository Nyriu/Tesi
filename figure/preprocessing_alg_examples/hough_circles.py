import cv2
import numpy as np
from matplotlib import pyplot as plt

from my_globals import image_path, image_name, image_dir, dest_dir, image_suffix

#print('Sobel ', image_path)

img = cv2.imread(dest_dir+'B.jpg', 0)
mask = cv2.imread(dest_dir + 'mask.jpg', 0)
img = cv2.bitwise_and(img, mask)

img = cv2.GaussianBlur(img, (3,3), 1)
img = cv2.equalizeHist(img)

canny_thr = 200

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=1, minDist=30, param1=canny_thr, param2=18, minRadius=9, maxRadius=18)

canny = cv2.Canny(img, threshold1=canny_thr//2, threshold2=canny_thr, apertureSize=3)
canny = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

img = cv2.imread(image_path)
if circles is not None:
    print(len(circles[0,:]))
    for n, i in enumerate(circles[0,:]):
        cx = i[0]
        cy = i[1]
        r = i[2]
        center = (cx, cy)
        cv2.circle(img, center, r, (0,255,255), thickness=5)
        cv2.circle(canny, center, r, (0,255,255), thickness=5)


cv2.imwrite(dest_dir+'hough_circles_example_wip' + image_suffix, canny)
save_path = dest_dir +  'hough_circles_example' + image_suffix
cv2.imwrite(save_path, img)
print('Hough Circles saved in ', save_path)
