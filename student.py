import sys

# Check if both name and roll number are provided
if len(sys.argv) < 3:
    print("usage: python student.py <name> <roll_no>")
    sys.exit(1)

script_name = sys.argv[0]
name = sys.argv[1]
roll_no = sys.argv[2]

# Display student information
print(f"Student Name: {name}")
print(f"Roll Number: {roll_no}")
