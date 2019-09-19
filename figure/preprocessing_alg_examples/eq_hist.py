
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

hist_save_path    = dest_dir + 'pre_eq_hist.png'
eq_hist_save_path = dest_dir + 'post_eq_hist.png'
# TODO
# automatizzare salvataggio degli hist
# i plot devono avere le stesse dimensioni dell'immagine in input
# Normalizzare rispetto ad y
# aggiungere linea del Cumulative Distribution Function

#plt.hist(img.ravel(),256,[0,256]); plt.show()
#plt.hist(eq_img.ravel(),256,[0,256]); plt.show()

#https://matplotlib.org/3.1.1/gallery/statistics/histogram_cumulative.html
fig, ax = plt.subplots(figsize=(8, 4))
b = 256
hist, bins = np.histogram(img.ravel(), bins=b)
ax.plot( bins[:-1], np.cumsum(hist) )
n, bins, patches = ax.hist(img.ravel(),256,[0,256])
fig.savefig(hist_save_path)

fig, ax = plt.subplots(figsize=(8, 4))
b = 256
hist, bins = np.histogram(eq_img.ravel(), bins=b)
ax.plot( bins[:-1], np.cumsum(hist) )
n, bins, patches = ax.hist(eq_img.ravel(),256,[0,256])
fig.savefig(eq_hist_save_path)
