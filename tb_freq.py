# %%

import pandas as pd

df = pd.read_csv("data/points_tmw - dados origem.csv")
df.head()

# %%

freq_produto = (df.groupby(["descProduto"])[["idTransacao"]]
                .count()) 

freq_produto["Freq. Abs Acum"] = freq_produto["idTransacao"].cumsum()

freq_produto["freq. Rel"] = freq_produto["idTransacao"] / freq_produto["idTransacao"].sum()

freq_produto["freq. Rel Acum"] = freq_produto["freq. Rel"].cumsum()

freq_produto
# %%
