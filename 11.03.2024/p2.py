def get_valid_age():
    while True:
        age = input("Enter Age: ")
        if age.isdigit() and 0 < int(age) <= 120:
            return int(age)
        print("Invalid age. Please enter a valid age.")

def get_valid_years_of_service():
    while True:
        service = input("Enter Years of Service: ")
        if service.replace('.', '', 1).isdigit():
            years, months = map(float, service.split('.')) if '.' in service else (float(service), 0)
            if 0 <= years <= 40 and 0 <= months < 12:
                return f"{int(years)} years, {int(months)} months"
        print("Invalid years of service. Please enter in format years.months, e.g., 8.2 for 8 years and 2 months.")

def main():
    file = open("employeedb.txt", "w")  # Open file for writing
    num_records = int(input("Enter the number of records to insert: "))
    for i in range(1, num_records + 1):
        print(f"\nEntering Record {i}")
        name = input("Enter Name: ")
        age = get_valid_age()
        emp_id = input("Enter Employee ID: ")
        years_of_service = get_valid_years_of_service()
        
        # Write to file
        file.write(f"{i}\t{name}\t{age}\t{emp_id}\t{years_of_service}\n")
        print(f"Record {i} Entry successful")

    file.close()  # Close the file after writing all records

if __name__ == "__main__":
    main()
