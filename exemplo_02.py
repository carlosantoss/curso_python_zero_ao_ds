
# carrega um arquivo do disco rigido para a memoria
# funcao: é uma sequencia de comandos
# recebe uma entrada:
# devolve uma saida: (parametros de entrada -> um resultado)
import pandas as pd

# data = pd.read_csv('datasets/kc_house_data.csv')

# # funcao que converte de object (string) para date (ano/mes/dia)
# data['date'] = pd.to_datetime(data['date'])
#
# # mostrar na tela os tipos de variaveis em cada coluna
# print(data.head())
#
# # para verificar os tipos das colunas no dataset
# print(data.dtypes)
#
# ==================================================
# # como converter os tipos de variáveis
# ==================================================

# # inteiro -> float
# data['bedrooms'] = data['bedrooms'].astype(float)
#
# # float -> inteiro
# data['bedrooms'] = data['bedrooms'].astype(int)
#
# # inteiro -> string
# data['bedrooms'] = data['bedrooms'].astype(str)
#
# # string -> inteiro
# data['bedrooms'] = data['bedrooms'].astype(int)
#
# # string -> data
# data['date'] = pd.to_datetime(data['date'])

# ==================================================
# criando variáveis
# ==================================================
# data = pd.read_csv('datasets/kc_house_data.csv')
# data['nome_do_carlos'] = 'carlos'
# data['comunidade_ds'] = 50
# data['data_abertura_comunidade_ds'] = pd.to_datetime('2020-02-28')

# ==================================================
# deletando variáveis
# ==================================================
# print(data.columns)
# cols = ['nome_do_carlos', 'comunidade_ds', 'data_abertura_comunidade_ds']
# data = data.drop(cols, axis=1) # drop -> excluir
# print(data.columns)

# ==================================================
# selecionando variáveis (04 formas)
# ==================================================
# forma 01: direto pelo nome das colunas
# ==================================================
# data = pd.read_csv('datasets/kc_house_data.csv')
# print(data[['price', 'id']]) # quando apenas 1 coluna, 1 par de colchetes,quando mais de 1 coluna, 2 pares de colchetes.

# ==================================================
# forma 02: pelos índices das linhas e colunas
# ==================================================
#DADOS[primeiro linhas, depois colunas]
# print(data.iloc[0:5, 0:3]) # iloc -> localize pelo índice // deixar vazio, retorna todos.

# ==================================================
# forma 03: pelos índices das linhas e NOME das colunas
# ==================================================
# print(data.loc[0:10, 'price']) # loc -> localize pelo nome // deixar vazio tambem retorna todos.

# ==================================================
# forma 04: pelos índices booleanos
# ==================================================
# verificar a quantidade de colunas no dataset, no caso, temos 21.
# inserir True para a coluna que quisermos mostrar e False para as que nao quisermos mostrar.
# cols = [True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
# print(data.loc[0:10, cols])

# ==================================================
# respondendo as perguntas de negocio
# ==================================================
data = pd.read_csv('datasets/kc_house_data.csv') # importar o dataset
data['date'] = pd.to_datetime(data['date']) # transformando string da coluna date para 'ano-mes-dia'

# 01. qual a data do imóvel mais antigo no portfólio?
# data['date'] = pd.to_datetime(data['date']) # tratar o dado
# print(data.sort_values('date', ascending=True)) # data mais antiga: 2014-05-02

# 02. quantos imóveis possuem o número máximo de andares?
# print(data['floors'].unique()) # todos os tipos de andares. o maior: 3.5
# print(data[data['floors'] == 3.5].shape) # conta quantos imóveis tem 3.5 andares

# 03. criar uma classificacao para os imóveis, separando-os em baixo e alto padrão de acordo com os preços
# se 'price' > 540.000 = high_standard na coluna nova standard
# se 'price' < 540.000 = low_standard na coluna nova standard

data['level'] = 'standard' # criando a nova coluna (level) e atribuindo valor standard a ela
#
data.loc[data['price'] > 540000, 'level'] = 'high_standard'
data.loc[data['price'] < 540000, 'level'] = 'low_standard'
# print(data.head())

# 04. relatório ordenado pelo preço (do maior para o menor)
# report = data[['id','date','price','bedrooms','sqft_lot','level']].sort_values('price', ascending=False) # novo relatorio (sort values price para ordenar)
# print(report.head()) # printar o header do novo relatório
# report.to_csv('datasets/report_aula02.csv', index=False) # salvar o novo relatório em csv, index para já salvar no formato escolhido.

# 05. mapa indicando onde as casas estao localizadas
# plotly - biblioteca que armazena uma funcao que desenha mapa
# scatter mapbox - funcao que desenha um mapa

import plotly.express as px # importando a biblioteca

data_mapa = data[['id', 'lat', 'long', 'price']] # criando a variável com os parâmetros

mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', # definindo as colunas
                         hover_name='id', # hover = acao quando passa o mouse / aqui o nome será o id do dataset
                         hover_data=['price'], # aqui terá uma acao de hover com o price do dataset
                         color_discrete_sequence=['darkgreen'],
                         zoom=8,
                         height=300)

mapa.update_layout(mapbox_style='open-street-map') # melhorando o mapa
mapa.update_layout(height=775, margin={'r':0, 't':0, 'l':0, 'b':0}) # definindo as propriedades do mapa

mapa.show() # mostrando o mapa (irá abrir no navegador)

mapa.write_html('datasets/mapa_house_rocket.html') # salvar o mapa em html

