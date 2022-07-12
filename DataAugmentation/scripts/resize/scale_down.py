from unicodedata import digit
import numpy as np
import imageio as im
from skimage.transform import resize
from tqdm import tqdm
import os 

import shutil

# =========== SETUP FILES PATH ========================================
OUT_DIR = "./data_aug_50_downscale"
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

IN_DATASET = "data-augumentation-subset-50-param-03"

if os.path.isdir(OUT_DIR):
  print(f"removing {OUT_DIR} and all files")
  shutil.rmtree(OUT_DIR)

os.mkdir(OUT_DIR)
for d in tqdm(DIGITS):
  digit_dir = os.path.join(OUT_DIR, d)
  os.mkdir(digit_dir)


# ============= SCALE IMAGE DOWN ========================================
print("SCALED DOWN")

for d in DIGITS:
  in_digit_dir = os.path.join(IN_DATASET, d)
  out_digit_dir = os.path.join(OUT_DIR, d)

  onlyfiles = [f for f in os.listdir(in_digit_dir) 
    if os.path.isfile(os.path.join(in_digit_dir, f))]
  
  print(f"Scaling images of digit {d}:")
  for filename in tqdm(onlyfiles):    
    in_digit_filename = os.path.join(in_digit_dir, filename)
    out_digit_filename = os.path.join(out_digit_dir, filename)
    img = im.imread(in_digit_filename)
    img = (resize(img, (28, 28))*255).astype(np.uint8)
    im.imwrite(out_digit_filename, img)
    
