import pandas as pd

input_file = "data/dados.csv"
output_file = "output/clean_data.xlsx"

# Ler CSV
df = pd.read_csv(input_file)

# Remover duplicados
df = df.drop_duplicates()

# Remover linhas com valores vazios
df = df.dropna()

# Ordenar por nome
df = df.sort_values(by="nome")

# Exportar para Excel
df.to_excel(output_file, index=False)

print("Arquivo limpo gerado com sucesso!")
