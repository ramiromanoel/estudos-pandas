# %%
import pandas as pd

# %%
df_customers = pd.read_csv("../00_dados/customers.csv", sep=";")
df_customers

 # %%
df_customers.shape

# %%
df_customers.info(memory_usage="deep")

# %%
df_customers["Points"].describe()

# %%
df_customers

# %%
notas = [4.5, 6, 7, 3.5]
for i in notas:
    if i > 5:
        print(i)

# %%
notas_novas = []
for i in notas:
    notas_novas.append(i+1)

notas_novas

# %%
