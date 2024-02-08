# TuntsRocksChallenge 💻

🎯 **O objetivo deste projeto é editar uma planilha no Google Spreadsheet com a API do Google Sheets e do Google Drive por meio do Python.**

### ⚙️ Requisitos

Caso queira utilizar o código na sua máquina com suas planilhas será necessário:  
1. Entrar no Google Cloud Console e ativar as APIs do Google Drive e Google Sheets
2. Criar um projeto
3. Criar uma credencial do tipo Service Accounts
4. Criar uma chave para API
5. Fazer o download do json gerado após a criação da credencial
6. Após esses passos, no seu editor de código ou IDE rode o comando: ```pip install gspread```
7. Depois nomeie o seu arquivo json já baixado anteriormente de credentials.json
8. Insira-o no mesmo diretório do seu código
9. Em sa.open adicione o nome do arquivo da planilha desejada
10. Em sh.worksheet adicione o nome da planilha desejada

✅ Pronto, tudo certo para poder editar sua planilha por meio do Python.

⚠️ O arquivo de credentials.json NÃO está presente nesse repositório pois se trata de um arquivo privado e sensível. Por isso, não pode ser compartilhado.
