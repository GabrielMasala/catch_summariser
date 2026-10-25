# Drill A: flag_below
import csv
# 1 Define the function and parameter
def flag_below(threshold):
    # 2 Setup list
    rows_below = []
    # Read the file and loop
    with open("landings.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                weight = float(row["weight_kg"])
            except ValueError:
                continue
            # 4 FILTER: ask one question about this row's weight vs threshold
            if weight < threshold:
                #5 ACCUMULATE: if yes, add the WHOLE row to your list
                rows_below.append(row)
    # 6 RETURN: after the loop has finished — which indent level?
    return rows_below
# 7 CALL + CATCH: outside the function, call with 60, store the result
flagged_rows = flag_below(60)
#   print the count (hint: len), then loop and print date | site | weight
print(f"Flagged Below: {len(flagged_rows)}")
for row in flagged_rows:
    print(f"{row['date']}|{row['landing_site']}|{row['weight_kg']} kg")

# Drill B: The count by function
def count_by(column):
    counts = {}
    with open("landings.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                weight = float(row["weight_kg"])
            except ValueError:
                continue
            key = row[column]
            if key not in counts:
                counts[key] = 0
            counts[key] += 1
    return counts

total_species = count_by("species")
print("SPECES")
print(f"Pweza: {total_species['pweza']}, Ngisi: {total_species['ngisi']}, Tasi: {total_species['tasi']}")

total_sites = count_by("landing_site")
print("SITES")
print(total_sites)



