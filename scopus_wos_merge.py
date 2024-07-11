import pandas as pd
from Levenshtein import distance

levenshtein_tolerance = 3

# Load the Excel files
scopus_file = "scopus_dataset.xlsx"
springerlink_file = "springerlink.xlsx"

try:
    scopus_df = pd.read_excel(scopus_file)
    springerlink_df = pd.read_excel(springerlink_file)
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit(1)

# Print column names to check
print(f"Scopus columns: {scopus_df.columns}")
print(f"SpringerLink columns: {springerlink_df.columns}")

# Ensure column names are correct, adjust if necessary
scopus_title_column = 'Title'
springerlink_title_column = 'Title'

if scopus_title_column not in scopus_df.columns:
    print(f"Error: Column name '{scopus_title_column}' not found in {scopus_file}")
    exit(1)

if springerlink_title_column not in springerlink_df.columns:
    print(f"Error: Column name '{springerlink_title_column}' not found in {springerlink_file}")
    exit(1)

# Normalize titles for comparison (convert to lowercase and strip spaces)
normalize_title = lambda x: x.lower().replace(' ', '')

scopus_df['NormalizedTitle'] = scopus_df[scopus_title_column].dropna().apply(normalize_title)
springerlink_df['NormalizedTitle'] = springerlink_df[springerlink_title_column].dropna().apply(normalize_title)

# Find unique titles in both datasets
unique_scopus_titles = set(scopus_df['NormalizedTitle'])
unique_springerlink_titles = set(springerlink_df['NormalizedTitle'])

# Calculate Levenshtein distances
levenshtein_dists = {w: min(distance(w, o) for o in unique_scopus_titles) for w in unique_springerlink_titles}

# Select WoS titles based on Levenshtein tolerance
selected_unique_wos = [k for k, v in levenshtein_dists.items() if v >= levenshtein_tolerance]

print(f"Unique SpringerLink titles: {len(unique_springerlink_titles)}")
print(f"Selected unique SpringerLink titles (tolerance {levenshtein_tolerance}): {len(selected_unique_wos)}")

# Filter SpringerLink DataFrame for selected unique titles
filtered_wos_df = springerlink_df[springerlink_df['NormalizedTitle'].isin(selected_unique_wos)]

# Combine the Scopus and filtered SpringerLink DataFrames
combined_df = pd.concat([scopus_df, filtered_wos_df], ignore_index=True)

# Remove the NormalizedTitle column
combined_df.drop(columns=['NormalizedTitle'], inplace=True)

# Save the merged result to a new Excel file
output_file = "merged_output_unique.xlsx"
combined_df.to_excel(output_file, index=False)

print(f"Merging complete. The result is saved in '{output_file}'.")
