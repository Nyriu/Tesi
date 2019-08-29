import cv2

from my_globals import image_path, image_name, image_dir, dest_dir, image_suffix

#print('RGB to GrayScale on ', image_path)

img = cv2.imread(image_path)
save_path = dest_dir + 'RGB' + image_suffix
cv2.imwrite(save_path, img)

img = cv2.imread(image_path)
#img[:,:,0] = 0
#img[:,:,1] = 0
#img[:,:,2] = 0
save_path = dest_dir + 'R' + image_suffix
cv2.imwrite(save_path, img[:,:,2])

img = cv2.imread(image_path)
save_path = dest_dir + 'G' + image_suffix
cv2.imwrite(save_path, img[:,:,1])

img = cv2.imread(image_path)
save_path = dest_dir + 'B' + image_suffix
cv2.imwrite(save_path, img[:,:,0])


img = cv2.imread(image_path)
bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
save_path = dest_dir +  'RGBtoGRAY' + image_suffix
cv2.imwrite(save_path, bw_img)
print('GrayScale saved in ', save_path)
