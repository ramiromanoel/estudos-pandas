# %%
import pandas as pd

# %%

idades = [30, 42, 90, 34]
idades

# %%
# explicacao sobre funções no detalhe
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media -i)**2

variancia = total / (len(idades) - 1)
variancia

# %%
# transformação de séries pandas
series_idades = pd.Series(idades)

# %%
# estatísticas
print(series_idades.mean())
print(series_idades.std())
print(series_idades.var())
print(series_idades.median())
print(series_idades.quantile(0.75))

# %%
# sumarização
series_idades.describe()

# %%
# dimensão da série
series_idades.shape
series_idades.shape[0]

# %%
# navegando na lista
idades[0]

# %%
series_idades

# %%
series_idades.index

# %%
series_idades = pd.Series(idades, name="idades")
series_idades

# %%
data = {
    "nome":["teo", "nah", "lara", "maria"],
    "sobrenome":["calvo", "ataide", "calvo", "calvo"],
    "idade":[31, 32, 32, 2]

}
# %%
data["idade"][0]

# %%
df = pd.DataFrame(data)
df

# %%
df["idade"].iloc[0]

# %%
df["sobrenome"].iloc[2]

# %%
df.iloc[0]

# %%
df.columns

# %%
df.info()

# %%
df.info(memory_usage="deep")

# %%
df.dtypes

# %%
