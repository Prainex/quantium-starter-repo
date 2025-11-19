import pandas as pd

combined_data = []

for i in range(0, 3):
    file_path = f"data/daily_sales_data_{i}.csv"
    read = pd.read_csv(file_path)

    # Filter rows and create a copy to avoid SettingWithCopyWarning
    filter_data = read.loc[read['product'] == 'pink morsel'].copy()

    # Calculate sales
    filter_data['sales'] = filter_data['price'].str.replace('$', '').astype(float) * filter_data['quantity']

    # Select relevant columns
    processed_data = filter_data[['sales', 'date', 'region']]

    # Append to the list
    combined_data.append(processed_data)

# Combine all DataFrames into one
overall_data = pd.concat(combined_data)

# Save to a new CSV file
overall_data.to_csv("data/combined_sales_data.csv", index=False)
