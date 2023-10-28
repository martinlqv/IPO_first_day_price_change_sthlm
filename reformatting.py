import pandas as pd

# Read the data
dataframe = pd.read_csv('data.csv')

# Drop columns
dataframe = dataframe.drop(columns=['High', 'Low', 'Adj Close', 'Volume'])

# Calculate the price change in percentage
dataframe['price_change'] = ((dataframe['Close'] - dataframe['Open']) /
                             dataframe['Open']) * 100

# Drop columns
dataframe = dataframe.drop(columns=['Open', 'Close'])

# Print the data
print(dataframe)

# Save the data
dataframe.to_csv('formatted_data.csv', index=False)
