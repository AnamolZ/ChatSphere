import subprocess
import time

start_time = time.time()

command = ["python", "Problem.py"]

# Test cases
test_cases = {
    "test_case_1": {"input_data": "1 2 3", "expected_output": "6"},
    "test_case_2": {"input_data": "2 4 6", "expected_output": "12"},
    "test_case_3": {"input_data": "3 6 9", "expected_output": "18"}
}

for test_name, test_data in test_cases.items():
    input_data = test_data["input_data"]
    expected_output = test_data["expected_output"]
    
    # Execute program and capture output
    output = subprocess.check_output(command, input=input_data.encode()).decode().strip()

    # Print result of each test case
    if output == expected_output:
        print(f"{test_name} passed!")
    else:
        print(f"{test_name} failed!")
        
# Print time complexity
end_time = time.time()
print("Time complexity: ", end_time - start_time)
