import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np

style.use('ggplot')
start=dt.datetime(2000,1,1)
end=dt.datetime(2016,12,31)
df= web.DataReader('TSLA', 'google', start, end)

df.to_csv('tsla.csv')
#df = pd.read_csv('tsla.csv')
print(df.head())

df.plot()
plt.show()