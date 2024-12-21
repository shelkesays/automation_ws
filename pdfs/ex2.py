from pathlib import Path
import pdfplumber

# Open the PDF file
path = Path("table.pdf")
with pdfplumber.open(path) as pdf:
    for page in pdf.pages:
        # Extract tables from the page
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                print(row)  # Print each row of the tableclear
