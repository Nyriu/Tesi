import cv2
import numpy as np

image_path = './peacock_spider_mask.png'

img = cv2.imread(image_path, 0)

kernel = np.ones((5,5), np.uint8)
img = cv2.erode(img, kernel, iterations=2)
img = cv2.dilate(img, kernel, iterations=2)

save_path = './mask.png'
cv2.imwrite(save_path, img)
