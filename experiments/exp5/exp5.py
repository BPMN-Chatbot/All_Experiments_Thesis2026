import pandas as pd
import matplotlib.pyplot as plt

# 📘 Step 1: Load Excel file
file_path = "exp5-autofix-success-rate.xlsx"  # <-- change this to your actual file path
df = pd.read_excel(file_path)

# 📘 Step 1.1: Clean up text columns
for col in ['Checker', 'Classification', 'Description', 'More Notes']:
    df[col] = df[col].astype(str).str.strip()

# 📘 Step 1.2: Count "No issues found" per Checker (before filtering)
no_issues = (
    df[df['Classification'].str.lower().str.contains('no issues found')]
    .groupby('Checker')
    .size()
    .reset_index(name='No Issues Found')
)

# 📘 Step 1.9: Count warnings and calculate percentage for each warning type for Collaboration Checker
collab_df = df[df['Checker'] == 'Collaboration Checker']  # only Collaboration Checker rows
total_collab = len(collab_df)  # total rows for this checker

# Identify warnings for Collaboration Checker
warning_mask = collab_df['Classification'].str.upper() == 'WARNING'
collab_warnings = collab_df[warning_mask].copy()
warning_count = len(collab_warnings)  # total warnings

# Now, find warning types from "More Notes"
# Assuming that the "More Notes" column specifies the warning types
warning_type_counts = collab_warnings['More Notes'].value_counts()
warning_type_percentages = (warning_type_counts / total_collab * 100).round(2)

# Print output for each warning type, and show which rows matched for each warning type
print(f"Collaboration Checker warnings:")
if not warning_type_counts.empty:
    for wt, count in warning_type_counts.items():
        perc = warning_type_percentages[wt]
        # Find the indices/rows for this warning type
        wt_rows = collab_warnings[collab_warnings['More Notes'] == wt].copy()
        print(f"  - {wt}: {count} ({perc:.2f}%)")
else:
    print("  - No warnings found.")

warning_percentage = (warning_count / total_collab * 100) if total_collab else 0
print(f"Total warning entries: {warning_count} ({warning_percentage:.2f}% of Collaboration Checker rows)\n")

# 📘 Step 1.3: Dataset–Case level analysis
# Count how many unique dataset–case pairs there are
total_cases = df[['Dataset', 'Case']].drop_duplicates().shape[0]

# Identify dataset–case pairs where all entries are "No issues found" (for both checkers)
no_issue_cases = (
    df.groupby(['Dataset', 'Case'])['Classification']
    .apply(lambda x: all(x.str.lower().str.contains('no issues found')))
    .reset_index(name='All_No_Issues')
)
no_issue_count = no_issue_cases['All_No_Issues'].sum()

print("=== Cases Summary ===")
print(f"Total cases: {total_cases}")
print(f"Cases with no issues in either checker: {int(no_issue_count)}")
print(f"Percentage with no issues: {no_issue_count / total_cases * 100:.2f}%\n")

# Total unique cases overall
total_cases = df[['Dataset', 'Case']].drop_duplicates().shape[0]

# Count "No issues found" per checker (case level)
unique_checker_cases = df[['Checker', 'Dataset', 'Case', 'Classification']].drop_duplicates()
unique_checker_cases['No_Issues'] = unique_checker_cases['Classification'].str.lower().str.contains('no issues found')

# Count per checker
no_issues_per_checker = (
    unique_checker_cases.groupby('Checker')['No_Issues']
    .sum()
    .reset_index(name='No_Issues')
)

# Calculate percentage over total unique cases
no_issues_per_checker['Percentage_No_Issues'] = (no_issues_per_checker['No_Issues'] / total_cases) * 100

print("=== No Issues Found per Checker (over total cases) ===")
print(no_issues_per_checker)
print("\n")



# 📘 Step 2: Keep only rows where isResolved is 0 or 1
df = df[df['isResolved'].isin([0, 1])]

# Clean up text: normalize case
for col in ['Checker', 'Classification']:
    df[col] = df[col].astype(str).str.strip().str.title()  # e.g. "Error" or "Warning"

# 📘 Step 3: Calculate overall resolution rate
total = len(df)
resolved = df['isResolved'].sum()
overall_rate = (resolved / total) * 100 if total else 0

print("=== Overall Summary ===")
print(f"Overall Resolution Rate: {overall_rate:.2f}%\n")

# 📘 Step 4: Resolution by Checker
checker_summary = (
    df.groupby('Checker')['isResolved']
    .agg(['count', 'sum'])
    .rename(columns={'count': 'Total', 'sum': 'Resolved'})
)
checker_summary['Resolution Rate (%)'] = (checker_summary['Resolved'] / checker_summary['Total']) * 100


print("=== Resolution Rate by Checker ===")
print(checker_summary, "\n")

# 📘 Step 5: Resolution by Checker + Classification
class_summary = (
    df.groupby(['Checker', 'Classification'])['isResolved']
    .agg(['count', 'sum'])
    .rename(columns={'count': 'Total', 'sum': 'Resolved'})
)
class_summary['Resolution Rate (%)'] = (class_summary['Resolved'] / class_summary['Total']) * 100

print("=== Resolution Rate by Checker + Classification ===")
print(class_summary, "\n")

