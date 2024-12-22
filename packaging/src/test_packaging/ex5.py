from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("example.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as output_file:
        writer.write(output_file)
print("PDF split into individual pages.")
