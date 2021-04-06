# carregue o conjunto de dados chamado kc_house_data.csv do HD para a memória

# funcao - read_csv()
# biblioteca - pandas

import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

# mostre na tela as 5 primeiras linhas do conjunto de dados
print(data.head())

# mostre na tela o numero de linhas e o numero de colunas do conjunto de dados
print(data.shape)

# mostre na tela o nome das colunas do conjunto de dados
print(data.columns)

# mostre na tela o conjunto de dados ordenados pela colune price
print(data[['id','price']].sort_values('price'))

# mostre na tela o conjunto de dados ordenados pela coluna price do maior para o menor
print(data[['id','price']].sort_values('price', ascending=False))

# exercícios
# 01. Quantas casas estão disponíveis para compra?
print(data.bedrooms.count())

# 02. Quantos atributos as casas possuem?
print(data.shape)

# 03. Quais são os atributos das casas?
print(data.columns)

# 04. Qual a casa mais cara ( casa com o maior valor de venda )?
print(data[['id','price']].sort_values('price', ascending=False))

# 05. Qual a casa com o maior número de quartos?
print(data[['id','bedrooms']].sort_values('bedrooms', ascending=False))

# 06. Qual a soma total de quartos do conjunto de dados?
print(data.bedrooms.sum())

# 07. Quantas casas possuem 2 banheiros?
print(data[data['bathrooms'] == 2])

# 08. Qual o preço médio de todas as casas no conjunto de dados?
print(data.price.mean())

# 09. Qual o preço médio de casas com 2 banheiros?
print(data[data['bathrooms'] == 2].price.mean())

# 10. Qual o preço mínimo entre as casas com 3 quartos?
print(data[data['bedrooms'] == 3].price.min())

# 11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
data['m2_living'] = data['sqft_living'] * 0.092
print(data[data['m2_living'] > 300].shape)

# 12. Quantas casas tem mais de 2 andares?
print(data[data['floors'] > 2].floors.count())

# 13. Quantas casas tem vista para o mar?
print(data[data['waterfront'] == 1].waterfront.count())

# 14. Das casas com vista para o mar, quantas tem 3 quartos?
print(data[(data['waterfront'] == 1) & (data['bedrooms'] == 3)].bedrooms.count())

# 15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?
print(data[(data['m2_living'] > 300) & (data['bathrooms'] > 2)].shape)