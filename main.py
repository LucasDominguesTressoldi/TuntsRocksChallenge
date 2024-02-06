import gspread
from situation import situation_calc
from average_grade import average_grade_calc

sa = gspread.service_account(filename="credentials.json")
sh = sa.open("Engenharia de Software - Desafio LucasTressoldi")

worksheet = sh.worksheet("engenharia_de_software")
