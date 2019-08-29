import cv2

from my_globals import image_path, image_name, image_dir, dest_dir, image_suffix

#print('Masking ', image_path)

img = cv2.imread(image_path)
mask = cv2.imread(dest_dir + 'mask.png')

masked = cv2.bitwise_and(img, mask)
save_path = dest_dir +  'masked' + image_suffix
cv2.imwrite(save_path, masked)
print('Masked saved in ', save_path)
