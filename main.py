import csv


def total_by(column):
    totals = {}
    skipped = 0
    total_rows = 0
    good_rows = 0
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
    return totals, total_rows, good_rows, skipped

species_totals, total_rows, good_rows, skipped = total_by("species")
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
print(f"Total landings by Species: {species_sum} kg")
print(f"Total landings by Site: {sites_sum} kg")
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
if  good_rows + skipped == total_rows:
    row_status = "Row check: PASS"
else:
    row_status = "Row check: FAIL"
print(row_status)

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
print(f"Total landings by Species: {species_sum} kg")
print(f"Total landings by Site: {sites_sum} kg")
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

