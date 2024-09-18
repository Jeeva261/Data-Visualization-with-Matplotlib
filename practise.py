# Create a line plot for time series data
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("timedata.csv")
plt.plot(df["Date"],df["Temperature (°C)"], color='blue', marker='o', linestyle='-', linewidth=2, markersize=4)
plt.show()

# Plot a scatter plot to visualize the relationship between two variables

df=pd.read_csv("timedata.csv")
plt.scatter(df["Date"],df["Temperature (°C)"])
plt.show()
