# Function to calculate age based on DOB without datetime module
def calculate_age(dob_str):
    # Check if the date is in the correct format and valid
    if len(dob_str) == 10 and dob_str[2] == '/' and dob_str[5] == '/':
        month, day, year = map(int, dob_str.split('/'))
        if 1 <= month <= 12 and 1 <= day <= 31:  # Basic checks for month and day
            # Calculate the current date as integers
            current_year = 2024
            current_month = 10
            current_day = 20

            # Calculate age
            age = current_year - year
            if (current_month, current_day) < (month, day):
                age -= 1  # Subtract one year if the birthday hasn't occurred yet

            return age
    return None  # Return None for incorrect date formats or invalid dates

# Initialize lists to store extracted data
names = []
dobs = []
employee_ids = []
rates = []

# Open the data file and read data from data.txt or testCase
file = open("data.txt", "r")
# file = open("Q3.Case2", "r")
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

# Close the data file
file.close()

# Calculate statistics with only valid ages
ages = [calculate_age(dob) for dob in dobs if calculate_age(dob) is not None]
avg_age = sum(ages) / len(ages) if ages else 0  # Prevent division by zero
max_rate = max(rates)
min_rate = min(rates)
avg_rate = sum(rates) / len(rates)
youngest_dob = dobs[ages.index(min(ages))] if ages else "N/A"  # Avoid indexing errors

# Write statistics to datastats.txt
stats_file = open("datastats.txt", "w")
stats_file.write("Statistic\t\t\t\tValue\n")
stats_file.write("--------------------------------------------------------------------------\n")
stats_file.write(f"Average age of employees: {avg_age:.2f} years\n")
stats_file.write(f"Maximum pay rate: {max_rate}\n")
stats_file.write(f"Lowest pay rate: {min_rate}\n")
stats_file.write(f"Average pay rate: {avg_rate:.2f}\n")
stats_file.write(f"DoB of youngest employee: {youngest_dob}\n")

# Close the stats file
stats_file.close()

print("Statistics successfully written to datastats.txt.")
