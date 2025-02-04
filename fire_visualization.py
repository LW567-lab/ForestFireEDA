import matplotlib
matplotlib.use('Agg')  # Fix IntelliJ Matplotlib issue
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset from the local folder
df = pd.read_csv("forestfires_filtered.csv")

# Ensure "area" column is numeric for visualization
df["area"] = pd.to_numeric(df["area"], errors="coerce")

# ----- Visualization 1: Scatter Plot (Temperature vs Fire Area) -----
plt.figure(figsize=(8, 6))
sns.regplot(x=df["temp"], y=df["area"], scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
plt.title("Impact of Temperature on Fire Spread")
plt.xlabel("Temperature (°C)")
plt.ylabel("Burned Area (ha)")
plt.savefig("scatter_plot.png")  # Save the figure instead of showing
print("Scatter plot saved as scatter_plot.png")

# ----- Visualization 2: Box Plot (Humidity vs Fire Area) -----
df["humidity_bins"] = pd.cut(df["RH"], bins=np.linspace(df["RH"].min(), df["RH"].max(), 6))

plt.figure(figsize=(8, 6))
sns.boxplot(x="humidity_bins", y="area", data=df)
plt.xticks(rotation=30)
plt.title("Fire Size Distribution Across Humidity Levels")
plt.xlabel("Relative Humidity (%)")
plt.ylabel("Burned Area (ha)")
plt.savefig("box_plot.png")  # Save the figure instead of showing
print("Box plot saved as box_plot.png")
