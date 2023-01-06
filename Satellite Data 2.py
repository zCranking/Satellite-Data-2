# %%
print("Name : Arav Gupta")
print("We will continue learning about data visualization, and sort the data")
print("Plot bar graphs for the countries who has the heaviest satellites in space")
print("Plot bar graphs for the countries whose satellites consumes the least power in space")

# %%
#Activity-1
#Q - Sort the data and find out the which Countries has the heaviest satellites, and plot a bar graph out of it
import pandas as pd
from matplotlib import pyplot as plt

dataframe = pd.read_csv('C191_satellite_data.csv')

dataframe


# %%
df = pd.DataFrame(dataframe, columns =['Dry Mass (Kilograms)','Official Name of Satellite'])
df.replace(" ", float("NaN"), inplace=True)

df = df.dropna()

sorted_df = df.sort_values(by=['Dry Mass (Kilograms)'])
sorted_df



# %%
heavy_satellite_5 = sorted_df.head(5)
print(heavy_satellite_5)

name = heavy_satellite_5['Official Name of Satellite']
weight = heavy_satellite_5['Dry Mass (Kilograms)']

plt.xlabel("Official Name of Satellite")
plt.xticks(rotation='vertical')
plt.ylabel("Mass (Kilograms)")


label = name
value = weight 
plt.bar(label, value,width=0.4, color=('red','yellow','green','pink','blue')) #bar-grap


# %%
#Activity-2
#Q - Sort the data and find out 5 Countries whose satellites consume the least power, and plot a bar graph out of it
df2 = pd.DataFrame(dataframe, columns=["Power (Watts)", "Official Name of Satellite"])
df2.replace(" ", float("NaN"), inplace=True)

df2 = df2.dropna()

sorted_df2 = df2.sort_values(by=["Power (Watts)"])
sorted_df2

power_hungry_top5 = sorted_df2.head(5)
print(power_hungry_top5)

name = power_hungry_top5["Official Name of Satellite"]
power = power_hungry_top5["Power (Watts)"]

plt.xlabel("Official Name of Satellite")
plt.xticks(rotation="vertical")
plt.ylabel("Power Consumption (Watts)")

label = name
value = power

plt.bar(label, value, width=0.4, color=('red', 'blue', 'pink', 'green', 'yellow'))

# %%


# %%



