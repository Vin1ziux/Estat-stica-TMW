# %%

import pandas as pd
import sqlalchemy

df = pd.read_csv("data/points_tmw - dados origem.csv")
df.head()

engine = sqlalchemy.create_engine("sqlite:///data/tmw.db")
df.to_sql("points", engine, if_exists="replace", index=False)
# %%

freq_prod = (df.groupby(["descCategoriaProduto"])[["idTransacao"]].count())
freq_prod["Freq Abs Acum"] = freq_prod["idTransacao"].cumsum()
freq_prod["Freq Rel"] = freq_prod["idTransacao"] / freq_prod["idTransacao"].sum()
freq_prod["Freq Rel Acum"] = freq_prod["Freq Rel"].cumsum()
freq_prod
   # %%
