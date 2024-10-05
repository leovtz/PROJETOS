import sqlite3
import pandas as pd


conn = sqlite3.connect('dados_vendas.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT,
    quantidade INTEGER,
    valor_unitario REAL
)
''')


vendas_data = [
    ('Produto A', 10, 20.0),
    ('Produto B', 15, 30.0),
    ('Produto C', 7, 15.0),
    ('Produto A', 12, 20.0),
    ('Produto B', 9, 30.0),
    ('Produto C', 14, 15.0),
]

cursor.executemany('INSERT INTO vendas (produto, quantidade, valor_unitario) VALUES (?, ?, ?)', vendas_data)
conn.commit()


df = pd.read_sql_query("SELECT * FROM vendas", conn)


print(df)


df['valor_total'] = df['quantidade'] * df['valor_unitario']
total_vendas = df['valor_total'].sum()
media_vendas = df['valor_total'].mean()
produto_mais_vendido = df.groupby('produto')['quantidade'].sum().idxmax()

print(f"Total de vendas: R${total_vendas:.2f}")
print(f"Média de vendas: R${media_vendas:.2f}")
print(f"Produto mais vendido: {produto_mais_vendido}")


df.to_csv('relatorio_vendas.csv', index=False)
print("Relatório gerado com sucesso!")


conn.close()
