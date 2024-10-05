import pandas as pd
import numpy as np


dados = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto B', 'Produto C'],
    'Quantidade': [10, 15, 7, 12, 9, 14],
    'Valor Unitário': [20.0, 30.0, 15.0, 20.0, 30.0, 15.0]
}

df = pd.DataFrame(dados)
df['Valor Total'] = df['Quantidade'] * df['Valor Unitário']


with pd.ExcelWriter('dashboard_interativo.xlsx') as writer:
    
    df.to_excel(writer, sheet_name='Dados de Vendas', index=False)

    
    pivot_table = df.pivot_table(values='Valor Total', index='Produto', aggfunc=np.sum)
    pivot_table.to_excel(writer, sheet_name='Resumo por Produto')

    
print("Dashboard interativo criado com sucesso!")
