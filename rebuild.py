import csv
totals = {}
skipped = 0
with open("landings.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            weight = float(row["weight_kg"])
        except ValueError:
            skipped += 1
            continue
        key = row[column]
print(weight)
print(skipped)


