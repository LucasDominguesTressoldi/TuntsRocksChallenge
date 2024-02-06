def situation_calc(worksheet, row, m, default_naf = 0):
  if m < 50:
    worksheet.update(f"G{row}:H{row}", [["Reprovado por Nota", f"{default_naf}"]])
  elif m < 70:
    worksheet.update(f"G{row}:H{row}", [["Exame Final", f"{100 - m}"]])
  else:
    worksheet.update(f"G{row}:H{row}", [["Aprovado", f"{default_naf}"]])
