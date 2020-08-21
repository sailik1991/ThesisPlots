import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

EXP_NAME = 'gs2019_realworld_values{}'
LEGEND_NAME = 'State and Agent'
Y_LABEL = 'Values V(s) ->'
X_LABEL = 'Gamma ->'

df = pd.read_csv(EXP_NAME.format(".csv"))
df = df.drop(columns=['V1_ur', 'V2_ur', 'V4_ur', 'V5_ur', 'V7_ur',
                      'V1_sse', 'V2_sse', 'V4_sse', 'V5_sse', 'V7_sse'])
df = df.reindex(sorted(df.columns), axis=1)
df = df.melt(X_LABEL, var_name=LEGEND_NAME, value_name="y")

sns.set()
sns.set_context("paper")  # options: paper, talk, posters
sns.set_palette(sns.color_palette("Paired"))

ax = sns.factorplot(
    x=X_LABEL, y="y", hue=LEGEND_NAME, data=df, height=5, aspect=1.4, legend=False
)
ax.set(ylabel=Y_LABEL)
# ax.set_xticklabels(rotation=60)

plt.legend(loc="upper left")
plt.savefig(EXP_NAME.format(".png"))
