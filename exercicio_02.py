import pandas as pd
import plotly.express as px

data = pd.read_csv('datasets/kc_house_data.csv')
data['date'] = pd.to_datetime(data['date'])

# 01. a - crie uma nova coluna chamada: "house_age"
data['house_age'] = 'house_age'

# 01. b - se o valor da coluna “date” for maior que 2014-01-01 => ‘new_house’
# 01. c - se o valor da coluna "date" for menor que 2014-01-01 => ‘old_house’
data.loc[data['date'] > '2014-01-01', 'house_age'] = 'new_house'
data.loc[data['date'] < '2014-01-01', 'house_age'] = 'old_house'

# 02. a - crie uma nova coluna chamada: "dormitory_type"
data['dormitory_type'] = 'dormitory_type'

# 02. b - se o valor da coluna “bedrooms” for igual à 1 => ‘studio’
data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'

# 02. c - se o valor da coluna “bedrooms” for igual a 2 => ‘apartment’
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartment'

# 02. d - se o valor da coluna “bedrooms” for maior que 2 => ‘house’
data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'

# 03. a - crie uma nova coluna chamada: "condition_type"
data['condition_type'] = 'condition_type'

# 03. b - se o valor da coluna “condition” for menor ou igual à 2 => ‘bad’
data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'

# 03. c - se o valor da coluna “condition” for igual a 3 ou 4 => ‘regular’
data.loc[(data['condition'] == 3) | (data['condition'] == 4), 'condition_type'] = 'regular'
# data.loc[data['condition'] == 3, 'condition_type'] = 'regular'
# data.loc[data['condition'] == 4, 'condition_type'] = 'regular'

# 03. d - se o valor da coluna “condition” for igual a 5 => ‘good’
data.loc[data['condition'] ==5, 'condition_type'] = 'good'

# 04. modifique o tipo da coluna "condition" para string
data['condition'] = data['condition'].astype(str)

# 05. delete as colunas “sqft_living15” e “sqft_lot15”
cols = ['sqft_living15','sqft_lot15']
data = data.drop(cols, axis=1)

# 06. modifique o tipo da coluna “yr_built” para date
data['yr_built'] = pd.to_datetime(data['yr_built'])

# 07. modifique o tipo da coluna “yr_renovated” para date
data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])

# 08. qual a data mais antiga de construção de um imóvel?
# print(data[['id','yr_built']].sort_values('yr_built', ascending=True))
# R: 1970-01-01 00:00:00.000001900 ou 1900.

# 09. qual a data mais antiga de renovação de um imóvel?
# print(data[['id','yr_renovated']].sort_values('yr_renovated', ascending=True))
# R: 1970-01-01 00:00:00.000000000 ou 1934.

# 10. quantos imóveis tem 2 andares?
# print(data[data['floors']==2].shape)
# R: 8.241

# 11. quantos imóveis estao com a condicao igual a "regular"?
# print(data[data['condition_type'] == 'regular'].shape)
# R: 19.710

# 12. quantos imóveis estao com a condicao igual a "bad" e possuem "vista para o mar"?
# print(data[(data['condition_type'] == 'bad') & (data['waterfront'] == 1)].shape)
# R: 2

# 13. quantos imóveis estao com a condicao igual a "good" e sao "new_house"?
# print(data[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house')].shape)
# R: 1701

# 14. qual o valor do imóvel mais caro do tipo "studio"?
# print(data[data['dormitory_type'] == 'studio'].price.max())
# R: $1.247.000

# 15. quantos imóveis do tipo "apartment" foram reformados em 2015?
# print(data[(data['dormitory_type'] == 'apartment') & (data['yr_renovated'] == '2015')].shape)
# R: 0

# 16. qual o maior numero de quartos que um imóvel do tipo "house" possui?
# print(data[data['dormitory_type'] == 'house'].bedrooms.max())
# R: 33

# 17. quantos imóveis "new_house" foram reformados no ano de 2014?
# print(data[(data['house_age'] == 'new_house') & (data['yr_renovated'] == '2014')].shape)
# R: 0

# 18. selecione as colunas: id, date, price, floors, zipcode pelos métodos abaixo:
# 18. a - direto pelo nome das colunas
# print(data[['id', 'date', 'price', 'floors', 'zipcode']])

# 18. b - pelos índices
# print(data.iloc[0:5, [0,1,2,7,16]])

# 18. c - pelos índices das linhas e o nome das colunas
# print(data.loc[0:5, ['id','date','price','floors','zipcode']])

# 18. d - índices booleanos
# cols = [True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False]
# print(data.loc[0:5, cols])

# 19. salve um arquivo .csv com somente as colunas do item 18
# report = data[['id','date','price','floors','zipcode']]
# print(report.head())
# report.to_csv('datasets/report_exercicio_aula02.csv', index=False)

# // csv com todas as colunas tratadas no exercicio
# report = data
# print(report.head())
# report.to_csv('datasets/report_exercicio_aula02b.csv', index=False)

# 20. modifique a cor dos pontos no mapa de "pink" para "verde-escuro"
# color_discrete_sequence=['darkgreen']

# ========================================================================================================

# print(data[['date','price','dormitory_type']].sort_values('price', ascending=False))
# print(data[data[['price',['dormitory_type' == 'studio'].sort_values('price', ascending=False)]]])
# print(data[['id','price']].sort_values('price'))

# print(data.columns)
# print(data.dtypes)
# print(data[['date','condition','condition_type']])
# print(data[data])
# print(data[['date','house_age','condition','bedrooms','dormitory_type','condition_type']].sort_values('condition',ascending=True))
# print(data[['date','house_age','condition','bedrooms','dormitory_type','condition_type']])
# print(data.sort_values('date', ascending=True))