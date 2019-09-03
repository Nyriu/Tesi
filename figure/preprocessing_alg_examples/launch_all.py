import rgb_to_gray
import masking
import affine_trans
import eq_hist
import gaussian_blur
import sobel_operator
import canny_edge_detector
import hough_circles


from my_globals import dest_dir, tesi_dest_dir

import shutil
import os

for img in os.listdir(dest_dir):
    src_path = dest_dir + img
    dst_path = tesi_dest_dir + img
    shutil.copy(src_path, dst_path)

print('DONE!!')
