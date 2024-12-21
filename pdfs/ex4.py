from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("table.pdf")
merger.append("table_1.pdf")
merger.append("example.pdf")
merger.write("merged.pdf")
merger.close()
print("PDFs merged.")
