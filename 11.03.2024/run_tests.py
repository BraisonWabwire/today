import os

# Define test cases for each question
test_cases = {
    "P1.py": ["Q1.Case1", "Q1.Case2", "Q1.Case3"],
    "P3.py": ["Q3.Case1", "Q3.Case2", "Q3.Case3"],
    "P4.py": ["Q4.Case1", "Q4.Case2", "Q4.Case3"],
    "P5.py": ["Q5.Case1", "Q5.Case2", "Q5.Case3"]
}

# Run each script with each of its test cases
for script, cases in test_cases.items():
    for case in cases:
        print(f"\nRunning {script} with {case}")
        os.system(f"python {script} {case}")
