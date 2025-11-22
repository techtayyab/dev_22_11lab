import sys

if len(sys.argv) !=3:
  print("usage: python student.py <name>
        sys.exit(1)

script_name = sys.argv[0]
name = sys.argv[1]
rollno = sys.argv[2]

print("script name: ",script_name)
print("student name: ",name)
print("roll number: ",rollno)
