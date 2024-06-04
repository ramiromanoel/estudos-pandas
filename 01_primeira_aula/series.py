# %%
import pandas as pd

# %%

idades = [30, 42, 90, 34]
idades

# %%

media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media -i)**2

variancia = total / (len(idades) - 1)
variancia

# %%
series_idades = pd.Series(idades)

# %%
print(series_idades.mean())
print(series_idades.std())
print(series_idades.var())
print(series_idades.median())
print(series_idades.quantile(0.75))

# %%
series_idades.describe()

# %%
series_idades.shape
series_idades.shape[0]

# %%
idades[0]

# %%
series_idades

# %%
series_idades.index

# %%
