import pandas as pd
import matplotlib.pyplot as plt


dados = {
    'Data': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto B', 'Produto C', 'Produto A'],
    'Quantidade': [10, 15, 7, 12, 9, 14, 10, 13, 6, 8],
    'Valor Unitário': [20.0, 30.0, 15.0, 20.0, 30.0, 15.0, 20.0, 30.0, 15.0, 20.0]
}

df = pd.DataFrame(dados)
df['Valor Total'] = df['Quantidade'] * df['Valor Unitário']


df.to_excel('dados_vendas.xlsx', index=False)


df = pd.read_excel('dados_vendas.xlsx')


total_vendas = df['Valor Total'].sum()
media_vendas = df['Valor Total'].mean()
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()

print(f"Total de vendas: R${total_vendas:.2f}")
print(f"Média de vendas: R${media_vendas:.2f}")
print(f"Produto mais vendido: {produto_mais_vendido}")


vendas_por_produto = df.groupby('Produto')['Valor Total'].sum()
vendas_por_produto.plot(kind='bar', color='skyblue')
plt.title('Total de Vendas por Produto')
plt.ylabel('Valor Total (R$)')
plt.xlabel('Produto')
plt.xticks(rotation=0)
plt.tight_layout()


plt.savefig('vendas_por_produto.png')
plt.show()


with open('relatorio_vendas.txt', 'w') as f:
    f.write(f"Relatório de Vendas\n\n")
    f.write(f"Total de vendas: R${total_vendas:.2f}\n")
    f.write(f"Média de vendas: R${media_vendas:.2f}\n")
    f.write(f"Produto mais vendido: {produto_mais_vendido}\n")

print("Relatório gerado com sucesso!")
