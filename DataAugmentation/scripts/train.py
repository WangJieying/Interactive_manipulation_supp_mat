#import imageio as im 
from tabnanny import verbose
import matplotlib.pyplot as plt 

from sklearn import svm, metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import numpy as np 
import pandas as pd
import struct

import os 

import imageio as im

IN_50_MNIST = "mnist-subset-50"

TEST_SAMPLES = "./t10k-images-idx3-ubyte"
TEST_LABELS = "./t10k-labels-idx1-ubyte"

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


DTtrain = DataSetImageLoader()
print("DT initialised")
DTtrain.load(IN_50_MNIST)
print("subset MNIST loaded")

Xtrain = DTtrain.get_samples()
Ytrain = DTtrain.get_labels()

inds = list(range(Ytrain.shape[0]))
np.random.shuffle(inds)

Xtrain[:,:] = Xtrain[inds,:]
Ytrain[:] = Ytrain[inds,]

print("=========== TRAIN ==================")
print(Xtrain.shape, Ytrain.shape)

test = DataSet(TEST_SAMPLES, TEST_LABELS)
Xtest = test.samples
Ytest = test.labels

print("=========== TEST ==================")
print(Xtest.shape, Ytest.shape)

# # Code based on 
# # https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-auto-examples-classification-plot-digits-classification-py

# _, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
# for (ax, image, label) in zip(axes, Xtrain, Ytrain):
#   ax.set_axis_off()
#   ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
#   ax.set_title(f"Training {label}")

# plt.show()

# # flatten the images
nsamples = len(Ytrain)
ntest = len(Ytest)

# Create a classifier: a support vector classifier
clf = make_pipeline(StandardScaler(), svm.SVC(gamma=0.001, verbose=1))

# set train and test dataset
X_train = Xtrain.reshape((nsamples, -1))
X_test = Xtest.reshape((ntest, -1))
y_train = Ytrain.ravel()
y_test = Ytest.ravel()

# Learn the digits on the train subset
clf.fit(X_train, y_train)

print("trained done")

# # Predict the value of the digit on the test subset
predicted = clf.predict(X_test)

print("predicted done")

# _, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
# for ax, image, prediction in zip(axes, X_test, predicted):
#   ax.set_axis_off()
#   image = image.reshape((28, 28))
#   ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
#   ax.set_title(f"Prediction: {prediction}")

print(
  f"Classification report for classifier {clf}: \n"
  f"{metrics.classification_report(y_test, predicted)}\n")


# Confusion matrix
disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()

print("About to perform predict on the train dataset")

train_predicted = clf.predict(X_train)

print("Predict on train dataset performed")

train_missclassified = train_predicted != y_train

print("Collected the missclassified samples")

print(f"y_train := {y_train[train_missclassified].shape}")
print(f"non_zero(train_missclassified) ;= {np.nonzero(train_missclassified)[0].shape}")
print(f"train_predicted[train_missclassified] ;= {train_predicted[train_missclassified].shape}")

df = pd.DataFrame(data=
   {"label": y_train[train_missclassified],
    "predicted_label": train_predicted[train_missclassified],
    "sample": np.nonzero(train_missclassified)[0]})

print("Pandas dataframe generated")

df.to_csv("miss_subset.csv", index=False)

print("csv file written")
