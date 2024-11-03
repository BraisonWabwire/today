# P4.py

from datetime import datetime
from collections import defaultdict

# Dictionary to store sales data, grouped by Month/Year and Transmission type
sales_data = defaultdict(lambda: {"manual": 0, "automatic": 0})

# Read and parse data from carsalesdata.csv
with open("Data1-Car Sales.xlsx - car_data.csv", "r") as file:
    # Skip the header line
    file.readline()
    
    # Process each car sales record
    for line in file:
        parts = line.strip().split(',')
        
        # Extract Date and Transmission
        date_str = parts[1]       # Date is the 2nd column (1-indexed)
        transmission = parts[8].strip().lower()  # Transmission is the 9th column
        
        # Parse month and year from the date
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        month_year_key = date_obj.strftime("%B/%Y")  # Format as "Month/Year", e.g., "January/2022"
        
        # Increment count based on transmission type
        if transmission == "manual":
            sales_data[month_year_key]["manual"] += 1
        elif transmission == "auto":
            sales_data[month_year_key]["automatic"] += 1

# Display results
print("Month/Year\t\t# of Manual Cars Sold\t# of Automatic Cars Sold")
print("-------------------------------------------------------------")
for period, counts in sorted(sales_data.items()):
    print(f"{period}\t{counts['manual']}\t\t\t{counts['automatic']}")
