
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

df_dados = pd.read_csv('./dados.csv', quotechar='\'',                        converters={'AtividadeFisica':LerJSON, 'AlimentacaoTipo':LerJSON}, header=0)


# Cálculo do limite de peso

# In[2]:


count = df_dados['Peso'].count()
max = df_dados['Peso'].max()

linha_limite = pd.Series(range(0, focoDias))
linha_limite = max - (linha_limite * ((max - focoPeso) / focoDias))
df_dados['Limite'] = linha_limite


# Nível de atividades físicas

# In[12]:


def scoreAtividade(data):
    score = 0
    for atividade in data:
        if (atividade['Tipo'] == 'Corrida'):
            score = score + atividade['Distancia'] * atividade['Velocidade']
        elif (atividade['Tipo'] == 'Musculação'):
            score = 15
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
    return tipo

df_dados['Tipo'] = df_dados['AtividadeFisica'].apply(tipoAtividade)


# Nível de alimentação

# In[4]:


def tipoAlimentacao(data):
    tipo = 0
    for alimentacao in data:
        if (alimentacao == 'Raízes'):
            tipo = tipo + 1
        elif (alimentacao == 'Legumes'):
            tipo = tipo + 2
        elif (alimentacao == 'Frutas'):
            tipo = tipo + 4            
        elif (alimentacao == 'Laticínios'):
            tipo = tipo + 8            
        elif (alimentacao == 'Farinários'):
            tipo = tipo + 16
        elif (alimentacao == 'Proteína Animal'):
            tipo = tipo + 32
        elif (alimentacao == 'Açúcar'):
            tipo = tipo + 64           
    return tipo

def nivelAlimentacao(data):
    if (data == 'Baixa'):
        return 1
    elif (data == 'Moderada'):
        return 2
    elif (data == 'Alta'):
        return 4

alimentacaoTipo = df_dados['AlimentacaoTipo'].apply(tipoAlimentacao)
alimentacaoVolume = df_dados['AlimentacaoNivel'].apply(nivelAlimentacao)
df_dados["ScoreAlimentacao"] = 0.025 * np.sqrt(alimentacaoTipo * alimentacaoVolume)


# Número de dias

# In[5]:


df_dados["NumeroDias"] = df_dados.index + 1


# Geração do gráfico

# In[15]:


import matplotlib.pyplot as plt

plt.plot(df_dados["NumeroDias"], df_dados["Peso"])
plt.plot(df_dados["NumeroDias"], df_dados["Limite"])
plt.scatter(df_dados["NumeroDias"], df_dados["Peso"], s=df_dados["ScoreAtividade"], c=df_dados["Tipo"], alpha=0.5)
plt.errorbar(df_dados["NumeroDias"], df_dados["Peso"], yerr=df_dados['ScoreAlimentacao'], c="grey", alpha=0.75)
plt.xlabel("Data")
plt.ylabel("Medida")
plt.show()


# Visualização da Tabela

# In[7]:


df_dados[['Data', 'NumeroDias', 'Peso', 'Limite', 'ScoreAtividade', 'ScoreAlimentacao']]

