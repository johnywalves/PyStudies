
# coding: utf-8

# ### Carregar os dados
# 

# In[1]:


#import os
#os.getcwd()

focoDias = 100
focoPeso = 85

import pandas as pd
import numpy as np

def LerJSON(data):
    import json
    if (data == ''):
        return json.loads('[]')
    else:
        return json.loads(data)

df_dados = pd.read_csv('./dados.csv', quotechar='\'', converters={'AtividadeFisica':LerJSON, 'AlimentacaoTipo':LerJSON}, header=0)

# Cálculo do limite de peso
# In[2]:

count = df_dados['Peso'].count()
max = df_dados['Peso'].max()
df_dados['Peso'] = df_dados['Peso'].interpolate()

linha_limite = pd.Series(range(0, focoDias))
linha_limite = max - (linha_limite * ((max - focoPeso) / focoDias))
df_dados['Limite'] = linha_limite

# Nível de atividades físicas
# In[3]:

def scoreAtividade(data):
    score = 0
    for atividade in data:
        if (atividade['Tipo'] == 'Corrida'):
            score = score + atividade['Distancia'] * atividade['Velocidade']
        elif (atividade['Tipo'] == 'Caminhada'):
            score = score + atividade['Distancia'] * atividade['Velocidade'] * 0.5
        elif (atividade['Tipo'] == 'Funcional'):            
            score = score + 30
        elif (atividade['Tipo'] == 'Musculação'):
            score = score + 15
    return score

df_dados['ScoreAtividade'] = df_dados['AtividadeFisica'].apply(scoreAtividade)
df_dados['ScoreAtividade'] = 25 * df_dados['ScoreAtividade']

def tipoAtividade(data):
    tipo = 0
    for atividade in data:
        if (atividade['Tipo'] == 'Corrida'):
            tipo = tipo + 1
        elif (atividade['Tipo'] == 'Musculação'):
            tipo = tipo + 2
        elif (atividade['Tipo'] == 'Funcional'):            
            tipo = tipo + 4
        elif (atividade['Tipo'] == 'Musculação'):
            tipo = tipo + 8
    return tipo

df_dados['Tipo'] = df_dados['AtividadeFisica'].apply(tipoAtividade)


# Nível de alimentação
# In[4]:

def tipoAlimentacao(data):
    tipo = 0        
    for alimentacao in data:
        tipo = tipo + {
            'Raízes': lambda: 1,
            'Legumes': lambda: 2,
            'Frutas': lambda: 4,
            'Laticínios': lambda: 8,
            'Farinários': lambda: 16,
            'Proteína Animal': lambda: 32,
            'Açúcar': lambda: 64
        }.get(alimentacao, lambda: 0)()
    return tipo

def nivelAlimentacao(data):
    return {
        'Baixa': lambda: 1,
        'Moderada': lambda: 2,
        'Alta': lambda: 4,
        'Exagerada': lambda: 8,
    }.get(data, lambda: 0)()

alimentacaoTipo = df_dados['AlimentacaoTipo'].apply(tipoAlimentacao)
alimentacaoVolume = df_dados['AlimentacaoNivel'].apply(nivelAlimentacao)
df_dados["ScoreAlimentacao"] = 0.025 * np.sqrt(alimentacaoTipo * alimentacaoVolume)

# Número de dias
# In[5]:


df_dados["NumeroDias"] = df_dados.index + 1


# Geração do gráfico

# In[8]:


import matplotlib.pyplot as plt

plt.plot(df_dados["NumeroDias"], df_dados["Peso"])
plt.plot(df_dados["NumeroDias"], df_dados["Limite"])
plt.scatter(df_dados["NumeroDias"], df_dados["Peso"], s=df_dados["ScoreAtividade"], c=df_dados["Tipo"], alpha=0.5)
plt.errorbar(df_dados["NumeroDias"], df_dados["Peso"], yerr=df_dados['ScoreAlimentacao'], c="grey", alpha=0.75)
plt.xlabel("Dias")
plt.ylabel("Medida")

plt.savefig('evolution.png', dpi=300)
plt.show()


# Visualização da Tabela

# In[7]:

tabela = df_dados[['Data', 'NumeroDias', 'Peso', 'Limite', 'ScoreAtividade', 'ScoreAlimentacao']]
tabela

