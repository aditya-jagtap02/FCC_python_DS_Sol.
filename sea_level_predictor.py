import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create first line of best fit
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series([i for i in range(1880, 2051)])
plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Best Fit Line (1880-2050)')

# Create second line of best fit
recent_df = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
years_recent_extended = pd.Series([i for i in range(2000, 2051)])
plt.plot(years_recent_extended, intercept_recent + slope_recent * years_recent_extended, 'g', label='Best Fit Line (2000-2050)')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Save plot and return data
plt.savefig('sea_level_plot.png')
plt.show()
