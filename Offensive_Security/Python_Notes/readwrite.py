#!/bin/python3

with open("months.txt", "r") as file:
    content = file.read()
    file.seek(0) #In order to test each function i need to reset to zero because the file has already been read. To see the value, comment the seeks out.
    line = file.readline()
    file.seek(0)
    lines = file.readlines()
    print(content)
    print(line)
    print(lines)

with open("days.txt", "w") as writefile:
    writefile.write("Monday")

with open("days.txt", "a") as appendfile:
    appendfile.write("\nTuesday\nWednesday\nThursday")

print("To view results of writefile, you'll need to cat the days.txt file created in this directory.")
