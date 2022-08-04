from etherscan import Etherscan
import json
import csv
import time
import glob
import pandas as pd

path = "C:/Stuff/School/S2022/RA/RAUniswap/TC Data/ERC20 Transactions/CSV/*.csv"
data = []

for fname in glob.glob(path):
    df2 = pd.read_csv(fname)
    try:
        new_fname = fname.split("_")[1].replace(".csv","")
    except:
        print("skip")
    data.append([len(df2), new_fname])

df = pd.DataFrame(data)
df.to_csv("test.csv")

