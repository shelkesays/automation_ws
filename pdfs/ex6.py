from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

# Add watermark to each page
reader = PdfReader("example.pdf")
writer = PdfWriter()
watermark = PdfReader("table.pdf").pages[0]

for page in reader.pages:
    page.merge_page(watermark)
    writer.add_page(page)

path = Path("watermarked.pdf")
with path.open("wb") as output_file:
    writer.write(output_file)
print("Watermark added to PDF.")