from pathlib import Path
from openpyxl import Workbook
from PyPDF2 import PdfReader

# Extract text from PDF
path = Path("table.pdf")
reader = PdfReader(path)
text = [page.extract_text() for page in reader.pages]

# Write the text into an Excel file
wb = Workbook()
sheet = wb.active
for i, page_text in enumerate(text, start=1):
    sheet[f"A{i}"] = page_text  # Write each page's text to a new row

wb.save("pdf_to_excel.xlsx")
print("PDF data written to Excel.")
