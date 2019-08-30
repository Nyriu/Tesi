import cv2
import numpy as np
from matplotlib import pyplot as plt

from my_globals import image_path, image_name, image_dir, dest_dir, image_suffix

#print('Masking ', image_path)

img = cv2.imread(dest_dir + 'GRAY_low_contrast.jpg', 0)

eq_img = cv2.equalizeHist(img)

save_path = dest_dir +  'eqHist_example' + image_suffix
cv2.imwrite(save_path, eq_img)
print('eqHist saved in ', save_path)

# TODO
# automatizzare salvataggio degli hist
# i plot devono avere le stesse dimensioni dell'immagine in input
# Normalizzare rispetto ad y
# aggiungere linea del Cumulative Distribution Function

#plt.hist(img.ravel(),256,[0,256]); plt.show()

#plt.hist(eq_img.ravel(),256,[0,256]); plt.show()

