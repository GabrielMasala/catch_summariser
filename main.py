import csv
# 1. Define a function called total_by that takes one parameter: column


def total_by(column):
    # 2. Inside it: create empty totals and set skipped to 0
    totals = {}
    skipped = 0
    # 3. Open the file, make the reader, loop over rows (same as before)
    with open("landings.csv") as file:
        reader = csv.DictReader(file)
        # 4. Try/except for weight (same as before)
        for row in reader:
            try:
                weight = float(row["weight_kg"])
            except ValueError:
                skipped += 1
                continue
            # 5. key = row[column]
            key = row[column]
            # 6. If key not in totals, start it at 0
            if key not in totals:
                totals[key] = 0
            # 7. Add weight to totals[key]
            totals[key] += weight
    # 8. After the with block, still inside the function: return totals, skipped
    return totals, skipped


# 9. Outside the function (level 0): call it for species
species_totals, skipped = total_by("species")
# 10. Print each species total, then skipped
for species, total in species_totals.items():
    print(f"{species}: {total} kg")
print(f"skipped: {skipped}")
# 11. Call it again for landing_site and print those totals
site_totals, skipped = total_by("landing_site")
for landing_site, total in site_totals.items():
    print(f"{landing_site}: {total} kg")
print(f"skipped: {skipped}")

