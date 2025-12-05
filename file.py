# file_handling_all_in_one.py

import os

print("===== 1. CREATE + WRITE FILE =====")
with open("demo.txt", "w") as f:
    f.write("Hello, this is a new file!\n")
    f.write("Python file handling is easy.")
print("File created and written.\n")


print("===== 2. READ FULL CONTENT =====")
with open("demo.txt", "r") as f:
    print(f.read(), "\n")


print("===== 3. READ LINE BY LINE =====")
with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip())
print()


print("===== 4. APPEND TO FILE =====")
with open("demo.txt", "a") as f:
    f.write("\nThis line is appended.")
print("Append done!\n")


print("===== 5. CHECK IF FILE EXISTS =====")
if os.path.exists("demo.txt"):
    print("File exists.\n")
else:
    print("File NOT found.\n")


print("===== 6. READ AS LIST OF LINES =====")
with open("demo.txt", "r") as f:
    print(f.readlines(), "\n")


print("===== 7. COPY FILE CONTENT =====")
with open("demo.txt", "r") as src:
    with open("copy_demo.txt", "w") as dest:
        dest.write(src.read())
print("File copied to copy_demo.txt\n")


print("===== 8. COUNT WORDS / LINES / CHARACTERS =====")
with open("demo.txt", "r") as f:
    data = f.read()

words = data.split()
lines = data.split("\n")
characters = len(data)

print("Words:", len(words))
print("Lines:", len(lines))
print("Characters:", characters, "\n")


print("===== 9. WRITE LIST INTO FILE =====")
items = ["apple", "banana", "mango"]
with open("fruits.txt", "w") as f:
    for item in items:
        f.write(item + "\n")
print("List written to fruits.txt\n")


print("===== 10. READ SPECIFIC NUMBER OF CHARACTERS =====")
with open("demo.txt", "r") as f:
    print(f.read(10), "\n")


print("===== 11. ERROR HANDLING (TRY/EXCEPT) =====")
try:
    with open("not_found.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File does not exist!\n")

print("===== DONE =====")
