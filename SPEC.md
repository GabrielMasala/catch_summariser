# SPEC: Unusual landings in summary.txt

Status: IMPLEMENTED

## 1. Reader
The Head of Programme at the NGO. They open summary.txt and never
see the terminal. They use unusual landings to decide which landing
sites to follow up with (record catch or data-entry error).

## 2. Decision
Yes. Unusual landings go into summary.txt, because the reader only
sees the file, not the screen.

## 3. Format
- A new section, placed LAST in the file, after CHECKS.
- Separated from CHECKS by one blank line, like the other sections. [M]
- Header: UNUSUAL LANDINGS (>60 kg)
- The number in the header is the threshold actually used, so the
  header and the rule can never disagree. [M]
- One line per unusual landing (row), not per site or per day. [M]
- Line format, no spaces: date|landing_site|weight kg
- Weight is the raw value from the CSV (69, not 69.0). [M]
- Landings appear in file order.
- Rule: a landing is unusual if weight > threshold (strictly
  greater). Exactly 60 is NOT unusual.

## 4. Expected lines (landings.csv, threshold 60)
The file must end with:

    UNUSUAL LANDINGS (>60 kg)
    22.09.2026|malindi|69 kg
    24.09.2026|kikadini|90.5 kg
    28.09.2026|kilindi|300 kg
    29.09.2026|kiongwe|82 kg

## 5. Edge case: zero unusual landings
The header still appears, with the line None under it:

    UNUSUAL LANDINGS (>400 kg)
    None

## 6. Acceptance tests
a) Normal case: run main.py, then `cat summary.txt`. Copy-paste the
   output and compare it line by line with section 4. Every line
   must match exactly.
b) Edge case: temporarily change the threshold to 400 (any value of
   300 or more gives zero). Run, then `cat summary.txt`. The ending
   must match section 5. Revert to 60. NEVER commit the test value. [M]
c) Regression: everything above the new section (species, sites,
   checks) is unchanged from the current summary.txt. [M]

## Notebook version (catch_summary.ipynb)

Same input (landings.csv), same validation rule and same THRESHOLD as
main.py. Output: notebook_summary.txt (not tracked by Git).

Intended differences from main.py:
- A landing site whose weights are ALL invalid is listed as `nan kg`
  (unknown), not 0 and not hidden. In landings.csv: mshembe.
  Reason: the landing happened; only its weight is unknown.
- Species and site totals are listed alphabetically
  (main.py: order of first appearance in the file).
- Weights in UNUSUAL LANDINGS are shown as decimals: `69.0 kg`
  (main.py: `69 kg`).

Tests:
- Matches the answer key, except the three differences above.
- THRESHOLD = 300 → UNUSUAL LANDINGS shows `None`.
- Cross-check: species sum = site sum = 677.5.