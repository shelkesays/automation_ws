from pathlib import Path
from PyPDF2 import PdfReader

# Load a PDF
path = Path("example.pdf")
reader = PdfReader(path)
text = ""

# Extract text from all pages
i = 0
for page in reader.pages:
    extracted_text = page.extract_text()
    if "HOW TO MEASURE THIGH" in extracted_text:
        text += "This is extra line\n"
    text += extracted_text
    

print("Extracted Text:")
print(text)
