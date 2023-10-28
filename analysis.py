import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Read data
dataframe = pd.read_csv('formatted_data.csv')

# Get the mean price change
mean_price_change = dataframe['price_change'].mean()

# Print the mean price change
print(mean_price_change)


# Plot the histogram
plt.hist(dataframe['price_change'], bins=10, edgecolor='black')

# Add labels and title
plt.xlabel('Price Change')
plt.ylabel('Frequency')
plt.suptitle('First day IPO price change')
plt.title('Nasdaq Stockholm 2018-2023', fontsize=10)

# Add line to show mean
plt.axvline(x=mean_price_change,
            color='red',
            linestyle='--',
            label=f'Mean: {mean_price_change:.2f}')

# Save the plot
plt.savefig('IPO_hist.png', dpi=900, bbox_inches='tight')

# Display the plot
plt.show()

# One-sample t-test
t_stat, p_value = stats.ttest_1samp(dataframe['price_change'], 0)

# Print the results
print(f'T-statistic: {t_stat}')
print(f'P-value: {p_value}')

# Monte Carlo time

# Calculate IPO's per year
dataframe['date'] = pd.to_datetime(dataframe['ipo_date'])
dataframe['year'] = dataframe['date'].dt.year
dataframe_filtered = dataframe.loc[dataframe['year'] != 2023]
mean_observations_per_year = dataframe_filtered.groupby('year').size().mean()
print("IPO's per year " + str(mean_observations_per_year))

# Extract the 'price_change' data and convert it to a decimal
price_changes = dataframe['price_change'] / 100

num_simulations = 10000
num_steps = 19

simulation_results = []

for n in range(num_simulations):
    prices = [100]  # Starting price
    for i in range(num_steps):
        random_price_change = np.random.choice(price_changes)
        new_price = prices[-1] * (1 + random_price_change)
        prices.append(new_price)
    simulation_results.append(prices)


# Convert simulation results to a DataFrame
simulation_df = pd.DataFrame(simulation_results).T

# Calculate the mean price at each step
mean_prices = simulation_df.mean(axis=1)

# Plotting the first 100 simulations
simulation_df.plot(legend=False, linewidth=1, alpha=0.1, color='blue')

# Draw a horizontal line at the mean price at each step
plt.plot(mean_prices, color='red', linewidth=2, label='Mean Price')

# Set x-axis labels to show 0 to 19
plt.xticks(ticks=range(0, 20), labels=range(0, 20))

plt.suptitle("Monte Carlo Simulation")
plt.title("Holding IPO's until close on Nasdaq Stockholm (one year)")
plt.xlabel("IPO's")
plt.ylabel("Profits")

# Save the plot
plt.savefig('IPO_montecarlo.png', dpi=900, bbox_inches='tight')

# Show the plot
plt.show()

# Get the final prices from each simulation
final_prices = simulation_df.iloc[-1]

# Summary_statistics
summary_statistics = final_prices.describe()
print(summary_statistics)
