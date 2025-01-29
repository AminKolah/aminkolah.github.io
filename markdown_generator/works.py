import bibtexparser
import csv

# Define the input BibTeX file and output TSV file
bibtex_file = "publications.bib"
tsv_file = "publications.tsv"

# Read the BibTeX file
with open(bibtex_file, "r", encoding="utf-8") as bib_file:
    bib_database = bibtexparser.load(bib_file)

# Extract relevant fields
entries = bib_database.entries

# Define the headers (adjust based on your BibTeX fields)
headers = ["title", "author", "year", "journal", "doi"]

# Write to TSV file
with open(tsv_file, "w", newline="", encoding="utf-8") as tsv_output:
    writer = csv.DictWriter(tsv_output, fieldnames=headers, delimiter='\t')
    writer.writeheader()
    
    for entry in entries:
        # Ensure all fields exist in entry
        row = {key: entry.get(key, "") for key in headers}
        writer.writerow(row)

print(f"TSV file '{tsv_file}' generated successfully.")
