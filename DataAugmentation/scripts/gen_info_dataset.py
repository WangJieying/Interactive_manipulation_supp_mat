import numpy as np
import pandas as pd
import struct 

import os
import imageio as im

from tqdm import tqdm

# Dataset loader for image (augmented MNIST)
class DataSetImageLoader:
  def __init__(self):
    self.labels = []
    self.samples = []    

  def load(self, dir_dataset):
    for d in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      self._load_digit(dir_dataset, d)

  def _load_digit(self, dir_dataset, digit):
    digit_dir = os.path.join(dir_dataset, digit)
    digit_files = os.listdir(digit_dir)
    for f in digit_files:
      digit_file = os.path.join(digit_dir, f)
      self.labels.append(int(digit))
      self.samples.append(im.imread(digit_file))

  def get_samples(self):
    return np.array(self.samples)
  
  def get_labels(self):
    return np.array(self.labels)

# Dataset loader for binary image (original MNIST)
class DataSet:
  def __init__(self, samples_filepath, label_filepath):
    self.samples = None
    self.labels = None 
    self._load(samples_filepath, label_filepath)


  def _load(self, samples_filepath, labels_filepath):
    with open(samples_filepath, "rb") as f:
      magic, sz, nx, ny = struct.unpack(">IIII", f.read(16))
      raw = np.fromfile(f, dtype=np.uint8)
      self.samples = raw.reshape((sz, ny, nx))

    with open(labels_filepath, "rb") as f:
      magic, sz = struct.unpack(">II", f.read(8))
      raw = np.fromfile(f, dtype=np.uint8)
      self.labels = raw.reshape((sz,))


train = DataSetImageLoader()
train.load("mnist-subset-50")
train.load("resize-dataset/data_aug_50_downscale")

data_train = train.get_samples()
target_train = train.get_labels()

dataset_info_label = []
dataset_info_sample = []

i = 0
for label in tqdm(target_train):
  dataset_info_label.append(label)  
  dataset_info_sample.append(i)
  i += 1

df = pd.DataFrame(data={
  "label": dataset_info_label,
  "sample": dataset_info_sample})

df.to_csv("subset-50-param-03.csv", index=False)
