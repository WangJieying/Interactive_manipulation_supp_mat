import imageio as im 
from skimage.transform import resize
import numpy as np
import os 
import os.path
import shutil

# =====================================================
# DEFINE SCRIPT MAIN CONSTANTS 
# ======================================================

# original dataset contains 28x28 images 
UP_DIM = 280

ORIGINAL_DATASET = "../mnist-subset-50"
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

RESIZED_DIR = "mnist_50_param_03"

# ==========================================================
# CLEAN DIRECTORY TRY AND RECREATE IT EMPTY
# =========================================================
if os.path.isdir(RESIZED_DIR):
  print(f"removing {RESIZED_DIR} and all files.")
  shutil.rmtree(RESIZED_DIR)

os.mkdir(RESIZED_DIR)
for d in DIGITS:
  digit_dir = os.path.join(RESIZED_DIR, d)
  os.mkdir(digit_dir)
  print(f"Directory {digit_dir} created.")

# ================================================================
# RESCALE IMAGES
#=================================================================
for d in DIGITS:
  in_digit_dir = os.path.join(ORIGINAL_DATASET, d)
  out_digit_dir = os.path.join(RESIZED_DIR, d)

  onlyfiles = [f for f in os.listdir(in_digit_dir) 
    if os.path.isfile(os.path.join(in_digit_dir, f))]
  
  for filename in onlyfiles:
    filename_pgm = os.path.splitext(filename)[0] + ".pgm"
    in_digit_filename = os.path.join(in_digit_dir, filename)
    out_digit_filename = os.path.join(out_digit_dir, filename_pgm)
    img = im.imread(in_digit_filename)
    img = (resize(img, (UP_DIM, UP_DIM))*255).astype(np.uint8)
    im.imwrite(out_digit_filename, img)
    print(f"Image {out_digit_filename} has rescaled.")
