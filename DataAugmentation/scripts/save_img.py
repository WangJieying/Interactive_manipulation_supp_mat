#from matplotlib import pyplot as plt 
import imageio as im
import numpy as np
import struct

import os.path 

from tqdm import tqdm

mnist = None 
labels = None 

IN_TRAIN_IMAGES = "train-images.idx3-ubyte"
IN_TRAIN_LABELS = "train-labels.idx1-ubyte"
OUT_DIR = "images/"

# https://www.kaggle.com/code/hojjatk/read-mnist-dataset/notebook
with open(IN_TRAIN_IMAGES, "rb") as f:     
  magic, size, nrows, ncols = struct.unpack(">IIII", f.read(16))
  mnist_raw = np.fromfile(f, dtype=np.uint8)
  mnist = mnist_raw.reshape((size, nrows, ncols))

with open(IN_TRAIN_LABELS, "rb") as f:
  magic, size = struct.unpack(">II", f.read(8))
  labels_raw = np.fromfile(f, dtype=np.uint8)
  labels = labels_raw.reshape((size,))

for i in tqdm(range(mnist.shape[0])):
  img = mnist[i,:,:]
  label = labels[i]
  out_filepath = os.path.join(OUT_DIR, f"{label}", f"{i}.png")
  im.imwrite(out_filepath, img)