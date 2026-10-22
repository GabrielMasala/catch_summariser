import csv


def totals_by(column):
    totals = {}
    total_rows = 0
    good_rows = 0
    skipped = 0
    with open("landings.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_rows += 1
            try:
                weight = float(row["weight_kg"])
            except ValueError:
                skipped += 1
                continue
            good_rows += 1
            key = row[column]
            if key not in totals:
                totals[key] = 0
            totals[key] += weight
    return totals,total_rows,good_rows,skipped
species_totals,total_rows,good_rows,skipped = totals_by("species")
for species, total in species_totals.items():
    print(f"{species}: {total} kg")
print(f"Rows: {total_rows}")
print(f"Good: {good_rows}")
print(f"Skipped: {skipped}")
if good_rows + skipped == total_rows:
    print(f"Row Check: PASS")
else:
    print(f"Row Check: FAIL")
site_totals,total_rows,good_rows,skipped = totals_by("landing_site")
for landing_site, total in site_totals.items():
    print(f"{landing_site}: {total} kg")
print(f"Rows: {total_rows}")
print(f"Good: {good_rows}")
print(f"Skipped: {skipped}")
if good_rows + skipped == total_rows:
    row_status = "Row Check: PASS"
    print(row_status)
else:
    row_status = "Row Check: FAIL"
    print(row_status)
species_sum = sum(species_totals.values())
site_sum = sum(site_totals.values())
print(f"Total Landings by Species: {species_sum} kg")
print(f"Total Landings by Site: {site_sum} kg")
if species_sum == site_sum:
    cross_status = "Cross-check: PASS"
    print(cross_status)
else:
    cross_status = "Cross-check: FAIL"
    print(cross_status)

with open("rebuild_summary.txt", "w") as out:
    out.write("SPECIES \n")
    for species, total in species_totals.items():
        out.write(f"{species}: {total} kg \n")
    out.write("\n")
    out.write("SITES \n")
    for sites, total in site_totals.items():
        out.write(f"{sites}: {total} kg \n")
    out.write("\n")
    out.write("CHECKS \n")
    out.write(f"Rows: {total_rows} | Good: {good_rows} | Skipped: {skipped} \n")
    out.write(f"{row_status} \n")
    out.write(f"{cross_status} \n")

def flag_outliers(threshold):
    flagged_rows = []
    with open("landings.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                weight = float(row["weight_kg"])
            except ValueError:
                continue
            if weight > threshold:
                flagged_rows.append(row)
    return flagged_rows
outliers = flag_outliers(60)
print(f"Flagged: {len(outliers)}")
for row in outliers:
    print(f"{row['date']}|{row['landing_site']}|{row['weight_kg']} kg")



