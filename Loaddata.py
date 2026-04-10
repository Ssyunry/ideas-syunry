import numpy as np
import pickle
import pandas as pd
filename = "load.csv"
cols = None
data = []
with open(filename) as f:
    for line in f.readlines():
        vals = line.replace("\n","").split(",")
        if cols is None:
            cols = vals
        else:
            data.append([float(x) for x in vals])
d0 = pd.DataFrame(data, columns=cols)
print(d0.dtypes)
print(d0.head())
d1 = np.loadtxt(filename, skiprows=1, delimiter=",")
print(d1.dtype)
print(d1[:5, :])
d2 = np.genfromtxt(filename, delimiter=",", names=True, dtype=None)
print(d2.dtype)
print(d2[:5])
d3 = pd.read_csv(filename)
print(d3.dtypes)
print(d3.head())
with open(filename, "rb") as f:
    d4 = pickle.load(f)
print(d4.dtype)
print(d4.head())




        
    