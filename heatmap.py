import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
#from google.colab import drive
#drive.mount('/content/drive')
abs_path = 'C:\\Users\\lenovo\\Desktop\\ML\\'#C:\\Users\\lenovo\\Desktop\\ML\\
train_identity = pd.read_csv(abs_path+'train_identity.csv')
train_transaction = pd.read_csv(abs_path+'train_transaction.csv')
df.dropna(inplace=True)
df= df.unstack(level=0)
fig, ax = plt.subplots(figsize=(11, 9))
sb.heatmap(df)
plt.show()
