# Noah Robinson

import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a variable 
df = pd.read_csv("best_selling_albums.csv")

# Display the first few rows in the dataset
print(df.head(10))

# Put the Sales_Millions column into a variable
sales = df["Sales_Millions"]
print()
# Display largest sales number
# print(sales.max())

largest_sales = df[df["Sales_Millions"] == df['Sales_Millions'].max()]
print("Largest Number of Recorded Sales")
print()
print(largest_sales)

# Display smallest sales number
# print(sales.min())

# Plot album and genre

plt.plot(df["Album"], df["Genre"])
plt.xlabel("Top Selling Albums")
plt.ylabel("Genres")
plt.title("Top Selling Albums and their Genres")
plt.show()