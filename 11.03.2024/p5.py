# Dictionary to store sales data by temperature ranges
sales_by_temp_range = {}

# Function to determine the temperature range
def get_temp_range(temp):
    if 40 <= temp <= 50:
        return "40-50"
    elif 51 <= temp <= 60:
        return "51-60"
    elif 61 <= temp <= 70:
        return "61-70"
    elif 71 <= temp <= 80:
        return "71-80"
    return None  # Ignore temperatures outside of these ranges

# Open the file and read data from the dataset file
file = open("Data2-Walmart_sales.csv", "r")
# file = open("Q5.Case3", "r")
# Skip the header line
file.readline()

# Processing of each line in the dataset
for line in file:
    parts = line.strip().split(',')
    
    # Extract the Temperature and Weekly Sales
    temperature = float(parts[4])        # Temperature is the 5th column (1-indexed)
    weekly_sales = float(parts[2])       # Weekly_Sales is the 3rd column
    
    # Determine the temperature range
    temp_range = get_temp_range(temperature)
    
    # If the temperature falls within our desired ranges, add the sales data
    if temp_range:
        # Check if the key exists; if not, initialize it with an empty list
        if temp_range not in sales_by_temp_range:
            sales_by_temp_range[temp_range] = []
        sales_by_temp_range[temp_range].append(weekly_sales)

# Close the file
file.close()

# Calculate average sales for each temperature range
print("Temperature Range\tAverage Sales")
print("----------------------------------------")
for temp_range, sales in sales_by_temp_range.items():
    avg_sales = sum(sales) / len(sales) if sales else 0  # Calculate the average sales
    print(f"{temp_range}\t\t{avg_sales:.2f}")
