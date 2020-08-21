import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# EXP_NAME = 'gs2019_mtdeep_participation{}'
# LEGEND_NAME = 'Alpha'
# Y_LABEL = 'Expected Accuracy ->'
# X_LABEL = '# Networks ->'

# EXP_NAME = 'gs2019_mtdeep_imagenet{}'
# LEGEND_NAME = 'Networks'
# Y_LABEL = 'Expected Accuracy ->'
# X_LABEL = 'Alpha ->'

# EXP_NAME = 'gs2019_mtdeep_mnist{}'
# LEGEND_NAME = 'Networks'
# Y_LABEL = 'Expected Accuracy ->'
# X_LABEL = 'Alpha ->'

# EXP_NAME = 'gs2019_mtdeep_fmnist{}'
# LEGEND_NAME = 'Networks'
# Y_LABEL = 'Expected Accuracy ->'
# X_LABEL = 'Alpha ->'

# EXP_NAME = 'gs2019_mtdeep_at_mnist{}'
# LEGEND_NAME = 'Networks'
# Y_LABEL = 'Expected Accuracy ->'
# X_LABEL = 'Alpha ->'

EXP_NAME = 'gs2019_mtdeep_attacker_robustness{}'
LEGEND_NAME = 'Networks'
Y_LABEL = 'Loss in Accuracy'
X_LABEL = 'Alpha ->'

df = pd.read_csv(EXP_NAME.format(".csv"))
df = df.melt(X_LABEL, var_name=LEGEND_NAME, value_name="y")

sns.set()
sns.set_context("paper")  # options: paper, talk, posters
# my_colors = sns.set_palette("deep")
my_colors = sns.xkcd_palette(["pale red", "denim blue", "amber", "faded green", 'brown grey'])
sns.set_palette(sns.color_palette(my_colors))

ax = sns.factorplot(
    x=X_LABEL, y="y", hue=LEGEND_NAME, data=df, height=4, aspect=1.4, linestyles=['-', "--", ":", "-", ":", '--', '-'], legend=False
)
ax.set(ylabel=Y_LABEL)
# ax.set_xticklabels(rotation=60)

plt.legend(loc="right")
plt.savefig(EXP_NAME.format(".png"))
