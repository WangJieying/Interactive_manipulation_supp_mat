import os.path 
import os
import shutil
from string import digits
from more_itertools import sample

import numpy as np 
import imageio as im

OUT_PATH = "./mnist-subset-50"
IN_PATH = "../images"

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SEEDS = {
  "0": 0, 
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9}

NUM_SAMPLES = 50

# ========================
# CLEAN OUT DIRECTORY
# ========================
if os.path.isdir(OUT_PATH):
  print(f"Removing {OUT_PATH} and all files")
  shutil.rmtree(OUT_PATH)

# ==========================
# CREATE DIRECTORY TREE
# ==========================

os.mkdir(OUT_PATH)
for d in DIGITS:
  digit_dir = os.path.join(OUT_PATH, d)
  os.mkdir(digit_dir)
  print(f"Directory {digit_dir} created.")

# =========================
# DATASET LOADER CLASS 
# =========================
class DataSetImageLoader:
  def __init__(self):    
    self.samples = {}

  def load(self, dir_dataset):
    for d in DIGITS:
      self._load_digit(dir_dataset, d)

  def _load_digit(self, dir_dataset, digit):
    digit_dir = os.path.join(dir_dataset, digit)
    digit_files = os.listdir(digit_dir)
    self.samples[digit] = []
    print(f"loading images of digit {digit}.")
    for f in digit_files:      
      self.samples[digit].append(f)


# =================================================
# LOAD DATASET 
# =================================================
ds = DataSetImageLoader()
ds.load(IN_PATH)
samples = ds.samples


# ==================================================
# SET UP SAMPLES INDEXES 
# ==================================================
idx_samples = {}

for d in digits:
  seed = SEEDS[d]
  idx_digit = np.arange(len(samples[d]))
  
  if seed is not None:
    np.random.seed(seed)

  np.random.shuffle(idx_digit)  
  idx_samples[d] = idx_digit[:NUM_SAMPLES]

# ==================================================
# SAVE CHOSEN SAMPLES INTO FILE
# ==================================================
for d in digits:
  for idx in idx_samples[d]:
    in_filepath = os.path.join(IN_PATH, d, samples[d][idx])
    out_filepath = os.path.join(OUT_PATH, d, samples[d][idx])
    shutil.copyfile(in_filepath, out_filepath)
    print(f"{in_filepath} copied to {out_filepath}.")