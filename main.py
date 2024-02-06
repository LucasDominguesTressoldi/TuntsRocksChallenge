import gspread
from situation import situation_calc
from average_grade import average_grade_calc

sa = gspread.service_account(filename="credentials.json")
sh = sa.open("Engenharia de Software - Desafio LucasTressoldi")

worksheet = sh.worksheet("engenharia_de_software")

total_classes = int(worksheet.acell("A2").value[-2:]) * 0.25
sheet_size = len(worksheet.col_values(1)) + 1
default_naf = 0

for row in range(4, sheet_size):
  print(f"Updating row: {row}")
  missed_classes = int(worksheet.acell(f"C{row}").value)

  if not total_classes >= missed_classes:
    worksheet.update(range_name=f"G{row}:H{row}", values=[["Reprovado por Falta", f"{default_naf}"]])
    continue

  situation_calc(worksheet, row, average_grade_calc(worksheet, row), default_naf)
