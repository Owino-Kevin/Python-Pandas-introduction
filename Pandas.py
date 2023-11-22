# In this tutorial, we will look at a powerful data analysis tool called PANDAS
import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)  # This is a data frame constructed using Pandas
print(myvar)

import pandas as pd

a = [1, 7, 9, 3]
myva = pd.Series(a)  # This constructs a Pandas Series
print(myva)
print(myvar.loc[[0, 1]])  # This returns the first two rows of the dataframe.

# Pandas Read CSV
import pandas as pd

df = pd.read_csv("C:/Users/VICTOR ORWA/Downloads/data.csv")  # this reads the CSV

print(df.to_string())
print(df)  # Python returns only the first and the last 5 rows if the number is more than 60
pd.options.display.max_rows = 9999  # This is to change the maximum number of rows
print(df)
print(df.head(10))  # This is to view the first ten rows in the data

print(df.info())  # Gives more information about the data
# From the information, there seems to be 5 missing values in the data on the Calories column. We remove the rows.
import pandas as pd

df = pd.read_csv("C:/Users/VICTOR ORWA/Downloads/data.csv")

new_df = df.dropna()  # This removes the whole row with missing value.

print(new_df.to_string())

# Incase you do not wish to remove the whole row just because of a single missing value, you replace with mean
import pandas as pd

df = pd.read_csv("C:/Users/VICTOR ORWA/Downloads/data.csv")

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace=True)  # This can also be done using the median or the mode.
df.corr()
new_df.corr()
print(df.corr())  # This returns the relationship between each column in the data.

# Pandas Plotting.

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/VICTOR ORWA/Downloads/data.csv")

# df.plot()  # To run the code, remove #

# plt.show()  # To run the code, remove #

# For Scatter plot with Pandas

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/VICTOR ORWA/Downloads/data.csv")

# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')  # This returns a scatterplot

# plt.show()

# Histogram

import pandas as pd
import matplotlib.pyplot as plt

df["Duration"].plot(kind = 'hist')

# plt.show()
# This marks the end of Pandas for now.