import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('TeddyBallgame.csv')
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index('Year', inplace=True)
df.plot()
plt.show()
''' 
The code above reads the data from the TeddyBallgame.csv file and creates a time series plot of the data.
'''