import csv
with open("landings.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
         print(row)
