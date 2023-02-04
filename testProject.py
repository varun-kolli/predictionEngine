import pandas as pd

data_dir = "http://dlsun.github.io/pods/data/names/"

df = pd.read_csv(data_dir + "yob1995.txt",
                        header=None, names=["Name", "Sex", "Count"])
print(df.head())