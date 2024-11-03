# P3.py

from datetime import datetime

# Function to calculate age based on DOB, with error handling
def calculate_age(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%m/%d/%Y")
        today = datetime(2024, 10, 20)  # Fixed date for calculations
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    except ValueError:
        return None  # Ignore invalid dates by returning None

# Initialize lists to store extracted data
names = []
dobs = []
employee_ids = []
rates = []

# Read and parse data from data.txt
with open("data.txt", "r") as file:
    # Skip the header lines
    file.readline()
    file.readline()
    
    # Process each employee record
    for line in file:
        parts = line.split()
        
        # Extract and assign data fields
        name = parts[1] + " " + parts[2]
        dob = parts[3]
        employee_id = parts[4]
        rate_per_hour = float(parts[5])

        # Append extracted data to lists
        names.append(name)
        dobs.append(dob)
        employee_ids.append(employee_id)
        rates.append(rate_per_hour)

# Calculate statistics with only valid ages
ages = [calculate_age(dob) for dob in dobs if calculate_age(dob) is not None]
avg_age = sum(ages) / len(ages) if ages else 0  # Prevent division by zero
max_rate = max(rates)
min_rate = min(rates)
avg_rate = sum(rates) / len(rates)
youngest_dob = dobs[ages.index(min(ages))] if ages else "N/A"  # Avoid indexing errors

# Write statistics to datastats.txt
with open("datastats.txt", "w") as stats_file:
    stats_file.write("Statistic\t\t\t\tValue\n")
    stats_file.write("--------------------------------------------------------------------------\n")
    stats_file.write(f"Average age of employees: {avg_age:.2f} years\n")
    stats_file.write(f"Maximum pay rate: {max_rate}\n")
    stats_file.write(f"Lowest pay rate: {min_rate}\n")
    stats_file.write(f"Average pay rate: {avg_rate:.2f}\n")
    stats_file.write(f"DoB of youngest employee: {youngest_dob}\n")

print("Statistics successfully written to datastats.txt.")
