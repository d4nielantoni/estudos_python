import pandas as pd

arquivo_excel = r"C:\Users\Daniel Antoni\Downloads\Metas 2024.xlsx" #aqui copiar caminho do arquivo excel

xls = pd.ExcelFile(arquivo_excel)
print(xls.sheet_names) 

planilha = 'Sheet1'
df = pd.read_excel(arquivo_excel, sheet_name=planilha)

arquivo_csv = r"C:\Users\Daniel Antoni\Downloads\Metas_2024.csv" #aqui copiar caminho onde ficará arquivo csv
df.to_csv(arquivo_csv, index=False)

print("Planilha convertida para CSV com sucesso!")
