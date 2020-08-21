import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# EXP_NAME = 'gs2018_throughput{}'
# LEGEND_NAME = 'None'
# Y_LABEL = 'Throughput (GBPS) ->'
# X_LABEL = '# IDS Placed ->'

EXP_NAME = 'gs2018_obj_num_ids{}'
LEGEND_NAME = 'Alpha'
Y_LABEL = "Defender's Utility ->"
X_LABEL = '# IDS Placed ->'

df = pd.read_csv(EXP_NAME.format(".csv"))
# df = df.reindex(sorted(df.columns), axis=1)
df = df.melt(X_LABEL, var_name=LEGEND_NAME, value_name="y")

sns.set()
sns.set_context("paper")  # options: paper, talk, posters
my_colors = sns.xkcd_palette(["denim blue", "pale red", "amber", "faded green"])
sns.set_palette(sns.color_palette(my_colors))

ax = sns.factorplot(
    x=X_LABEL, y="y", hue=LEGEND_NAME, data=df, height=5, aspect=1.2, legend=False
)
ax.set(ylabel=Y_LABEL)
labels = list(df[df.columns[0]])
new_labels = []
for l in labels:
    new_labels.append(l) if l % 6 == 0 else new_labels.append('')
ax.set_xticklabels(new_labels)

plt.legend(loc="upper left")
plt.savefig(EXP_NAME.format(".png"))
