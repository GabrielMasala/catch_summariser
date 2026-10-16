import csv
# 1. Define a function called total_by that takes one parameter: column


def total_by(column):
    # 2. Inside it: create empty totals and set skipped to 0
    totals = {}
    skipped = 0
    total_rows = 0
    good_rows = 0
    # 3. Open the file, make the reader, loop over rows (same as before)
    with open("landings.csv") as file:
        reader = csv.DictReader(file)
        # 4. Try/except for weight (same as before)
        for row in reader:
            total_rows += 1
            try:
                weight = float(row["weight_kg"])
            except ValueError:
                skipped += 1
                continue
            good_rows += 1
            # 5. key = row[column]
            key = row[column]
            # 6. If key not in totals, start it at 0
            if key not in totals:
                totals[key] = 0
            # 7. Add weight to totals[key]
            totals[key] += weight
    # 8. After the with block, still inside the function: return totals,total_rows,good_rows,skipped
    return totals, total_rows, good_rows, skipped
# 9. Outside the function (level 0): call it for species
species_totals, total_rows, good_rows, skipped = total_by("species")
# 10. Print each species total, then skipped
for species, total in species_totals.items():
    print(f"{species}: {total} kg")
print(f"Rows: {total_rows}")
print(f"Good: {good_rows}")
print(f"Skipped: {skipped}")
if  good_rows + skipped == total_rows:
    row_status = "Row check: PASS"
else:
    row_status = "Row check: FAIL"
print(row_status)
# 11. Call it again for landing_site and print those totals
site_totals, total_rows, good_rows, skipped = total_by("landing_site")
for landing_site, total in site_totals.items():
    print(f"{landing_site}: {total} kg")
print(f"Rows: {total_rows}")
print(f"Good: {good_rows}")
print(f"Skipped: {skipped}")

if good_rows + skipped == total_rows:
    row_status = "Row check: PASS"
else:
    row_status = "Row check: FAIL"
print(row_status)

species_sum = sum(species_totals.values())
sites_sum = sum(site_totals.values())
print(f"Total landings by Species: {species_sum}")
print(f"Total landings by Site: {sites_sum}")
if species_sum == sites_sum:
    check_status = "Cross-check: PASS"
else:
    check_status = "Cross-check: FAIL"
print(check_status)

with open("summary.txt", "w") as out:
    out.write("SPECIES\n")
    for species, total in species_totals.items():
        out.write(f"{species}: {total} kg\n")
    out.write("\n")
    out.write("LANDING SITES\n")
    for landing_site, total in site_totals.items():
        out.write(f"{landing_site}: {total} kg\n")
    out.write("\n")
    out.write("CHECKS\n")
    out.write(f"Rows: {total_rows} | Good: {good_rows} | Skipped: {skipped}\n")
    out.write(f"{row_status}\n")
    out.write(f"{check_status}\n")

# define flag_outliers, taking one parameter: threshold
def flag_outliers(threshold):
    # create an empty list for flagged rows
    flagged_rows = []
    # open the file, make the reader, loop over rows (same as total_by)
    with open("landings.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # try/except: convert the weight; skip bad rows with continue
            try:
                weight = float(row["weight_kg"])
            except ValueError:
                continue
        # if the weight is above the threshold: append the whole row to the list
            if weight > threshold:
                flagged_rows.append(row)
    # after the with block: return the list
    return flagged_rows
outliers = flag_outliers(60)
print(f"Flagged: {len(outliers)}")
for row in outliers:
        print(f"{row['date']}|{row['landing_site']}|{row['weight_kg']} kg")
