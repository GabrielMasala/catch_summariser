# Catch Log Summariser

## What it does
Reads a fish landings log, skips rows with invalid weights, totals the catch
by species and by landing site, checks its own results, writes a summary file,
and flags unusually heavy landings.

## Input
A CSV file named `landings.csv` in the project folder, with these columns:
`date`, `species`, `landing_site`, `weight_kg`.
Tested on a 10-row sample and a 150-row real dataset.

## How to run
From the project folder, with the virtual environment active:

    python main.py

## Output
On screen:
- Total weight by species and by landing site
- Row counts (total, good, skipped) and both checks
- Rows flagged as outliers (date | site | weight)

In `summary.txt` (overwritten on each run):
- Totals by species and by site
- Row counts and check results
- Outliers are NOT written to the file yet

## Checks
- **Row check:** good rows + skipped rows = total rows, so no row is lost.
- **Cross-check:** species total = site total, so no weight is lost or
  double-counted between the two groupings.

## Rules and assumptions
- A row is **bad** if `weight_kg` cannot be converted to a number (for
  example, blank or text). Bad rows are skipped and counted, not totalled.
- A row is an **outlier** if its weight is greater than 60 kg. The 60 kg
  threshold is arbitrary and set in the code at `flag_outliers(60)`.
- A row of exactly 60 kg is **not** flagged (the rule is strictly greater than).

## Known limits
- File name is assigned at the beginning, threshold is fixed in the code.
- One threshold is used for every species.
- Blank species or landing site values are not checked.
- Negative weights are accepted.
- Totals can show float noise (e.g. 371.0000003 on larger datasets).