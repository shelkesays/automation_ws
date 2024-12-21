from pathlib import Path
from openpyxl.styles import Font, Alignment
from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
sheet["A1"] = "Item"
sheet["B1"] = "Quantity"
sheet["C1"] = "Price"
sheet["D1"] = "Total"

# Add data
data = [("Apple", 10, 0.5), ("Banana", 5, 0.3), ("Cherry", 15, 0.2)]
for row in data:
    sheet.append(row)

# Add a formula for totals
for i in range(2, len(data) + 2):
    sheet[f"D{i}"] = f"=B{i}*C{i}"

# Formatting headers
for cell in sheet[1]:
    if cell.col_idx == 1 and cell.row == 1:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center")

# Save the file
path = Path(__file__).parent.joinpath("formatted.xlsx")
wb.save(path)
print("Excel file formatted with formulas.")
