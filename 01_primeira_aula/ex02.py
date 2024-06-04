"""
Converta o seguinte dicionáro para data frame e obtenha:
 Sumário de cada coluna;
 Média da coluna idade;
 Último nome da coluna nome;

dados = {"nome":["Téo","Nah", "Napoleão"], "idade":[31, 32, 14]}
"""
# %%
import pandas as pd

# %%
dados = {"nome":["Téo","Nah", "Napoleão"], "idade":[31, 32, 14]}
df = pd.DataFrame(dados)
df

# %%
sumario_numericas = df.describe()
sumario_numericas

# %%
df["nome"].describe()

# %%
df["idade"].describe()

# %%
media_idade = df["idade"].mean()
media_idade

# %%
df["nome"].iloc[-1]
df["nome"].tail(1)

# %%
