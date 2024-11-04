import subprocess
import os

# Define the directory containing the test cases
test_cases_dir = ""  # Update this to the correct path

# Define test cases for each question
test_cases = {
    "P1.py": ["Q1.Case1", "Q1.Case2", "Q1.Case3"],
    "P3.py": ["Q3.Case1", "Q3.Case2", "Q3.Case3"],
    "P4.py": ["Q4.Case1", "Q4.Case2", "Q4.Case3"],
    "P5.py": ["Q5.Case1", "Q5.Case2", "Q5.Case3"]
}

# Run each script with each of its test cases
for script, cases in test_cases.items():
    # Construct the full path to the script in the testCases directory
    script_path = os.path.join(test_cases_dir, script)
    
    for case in cases:
        print(f"\nRunning {script_path} with test case: {case}")
        try:
            # Construct the full path for the test case file
            case_path = os.path.join(test_cases_dir, case)
            result = subprocess.run(
                ["python", script_path, case_path],  # Pass the case path as an argument
                check=True,   # Raises CalledProcessError if the command fails
                capture_output=True,  # Captures stdout and stderr
                text=True      # Returns the output as string
            )
            print("Output:", result.stdout)  # Prints the standard output
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running {script_path} with {case}:\n{e.stderr}")

