import gspread

sa = gspread.service_account(filename="credentials.json")
sh = sa.open("Engenharia de Software - Desafio LucasTressoldi")

worksheet = sh.worksheet("engenharia_de_software")
