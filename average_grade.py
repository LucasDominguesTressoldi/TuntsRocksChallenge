def average_grade_calc(worksheet, row):
  p1 = int(worksheet.acell(f"D{row}").value)
  p2 = int(worksheet.acell(f"E{row}").value)
  p3 = int(worksheet.acell(f"F{row}").value)

  return (p1 + p2 + p3) / 3
