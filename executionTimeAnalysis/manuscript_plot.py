import numpy as np
from imageio.v2 import imwrite, imread

from os import listdir
from os.path import isfile, join

from pandas import DataFrame, read_csv, concat

import matplotlib.pyplot as plt

# ================================================================================================
# Recover datas
# ================================================================================================
img_filenames = [f for f in listdir("./images") if f[-3:] == "pgm"]
npixels = []
dims = []
for img_filename in img_filenames:
    f = imread(join("./images/", img_filename))
    npixels.append(f.shape[0] * f.shape[1])
    dims.append(f"{f.shape[1]} x {f.shape[0]}")

idx = np.argsort(npixels).astype(int)

img_filenames = np.array(img_filenames)
npixels = np.array(npixels)
dims = np.array(dims)

# ================================================================================================
# DataFrame
# ================================================================================================
df = DataFrame(
    {"filename": img_filenames[idx],
     "number of pixels": npixels[idx],
     "dimension": dims[idx]})


# ================================================================================================
# Recover runtime data from CSV
# ================================================================================================
time = read_csv("./data/benchmark.csv", sep=";").drop(["filename"], axis=1)
nnodes = read_csv("./data/number_of_nodes.csv", sep=";").drop(["filename"], axis=1)

times_nnodes = time.join(nnodes, lsuffix="_time", rsuffix="_nnodes")

df = df.join(times_nnodes)

# ================================================================================================
# Runtime column names
# ================================================================================================
times_header = ["10_time", "45_time", "80_time", "115_time", "150_time", 
                "185_time", "220_time", "255_time"]

nnodes_header = ["10_nnodes", "45_nnodes", "80_nnodes", "115_nnodes", "150_nnodes",
                 "185_nnodes", "220_nnodes", "255_nnodes"]

# ================================================================================================
# Set up rutime by number of nodes, use average runtime when there is number of nodes repetition.
# ================================================================================================

# Get a list of number of nodes 
lnnodes = df[nnodes_header].values.ravel()  

# Get a list of number of nodes
ltimes = df[times_header].values.ravel() / 1000 # convert millisecods to seconds

# Note that  ltimes[index] is the runtime computed by a image whose maxtree has lnodes[index] nodes.

# compute average time for experiments with the same number of nodes
times_nodes = DataFrame({"nnodes": lnnodes, "times": ltimes})
avg_times_nodes = times_nodes.groupby(by=["nnodes"], as_index=False).mean()

# ================================================================================================
# plot the graph
# ================================================================================================
plt.title("Runtime of encoding step against\n the number of the maxtree nodes"
         f" of the input image")
plt.xlabel("number of nodes")
plt.ylabel("runtime (seconds)")
plt.plot(avg_times_nodes["nnodes"], avg_times_nodes["times"])
plt.savefig("runtime-plot.eps", format="eps")
