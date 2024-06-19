import csv

# Creating CSV file
fields = ['Name', 'Branch', 'Year', 'CGPA']
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1']]
filename = "university_records.csv"

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

# Printing CSV file
with open('university_records.csv', 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
