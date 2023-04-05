import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("seattleWeather_1948-2017.csv", parse_dates=[0])[['DATE', 'PRCP']]
rainfall = df[df['DATE'].dt.year == 2016]['PRCP'].values

plt.hist(rainfall, bins=30)
plt.title('Rainfall')
plt.xlabel('PRCP')
plt.ylabel('Frequency')

x = np.array([1, 2, 3, 4, 5])
print(x == 3)
np.count_nonzero