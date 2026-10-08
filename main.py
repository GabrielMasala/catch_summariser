import csv
# BEFORE the with block:
# 1. Create an empty dictionary called totals
totals = {}
# 2. Create a counter called skipped, starting at 0
skipped = 0
with open("landings.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
# INSIDE the for loop:
# 3. TRY to convert row["weight_kg"] to a float, store it in weight
        try:
            weight = float(row["weight_kg"])
# 4. EXCEPT ValueError: add 1 to skipped, then continue
        except ValueError:
            skipped += 1
            continue
# 5. Store row["species"] in a variable called species
        species = row["species"]
# 6. If species is NOT in totals yet, set totals[species] to 0
        if species not in totals:
            totals[species] = 0
# 7. Add weight to totals[species]
        totals[species] += weight
# AFTER the with block (back at level 0):
# 8. Loop through totals and print each species and total with an f-string
for species, total in totals.items():
    print(f"{species}: {total} kg")
# 9. Print the skipped count
print(f"Rows skipped: {skipped}")

