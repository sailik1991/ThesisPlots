import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# EXP_NAME = 'aamas2017_obj_alpha_study{}'
# LEGEND_NAME = 'Strategy'
# Y_LABEL = 'Obj. Function Value'
# X_LABEL = 'Alpha'

# EXP_NAME = 'aamas2017_obj{}'
# LEGEND_NAME = 'Strategy'
# Y_LABEL = 'Obj. Function Value'
# X_LABEL = 'Alpha'

# EXP_NAME = "aamas2017_config_prob_alpha_study{}"
# LEGEND_NAME = "Config"
# Y_LABEL = 'Pr(c)'
# X_LABEL = 'Alpha'

EXP_NAME = 'aamas2017_sensitivity_bsg{}'
LEGEND_NAME = 'Attacker Types'
Y_LABEL = 'NLR (BSG)'
X_LABEL = '% Variation'

# EXP_NAME = 'aamas2017_sensitivity_urs{}'
# LEGEND_NAME = 'Attacker Types'
# Y_LABEL = 'NLR (URS)'
# X_LABEL = '% Variation'

df = pd.read_csv(EXP_NAME.format(".csv"))
df = df.melt(X_LABEL, var_name=LEGEND_NAME, value_name="y")

sns.set()
sns.set_context("paper")  # options: paper, talk, posters
# my_colors = sns.set_palette("deep")
my_colors = sns.xkcd_palette(["denim blue", "pale red", "amber", "faded green"])
sns.set_palette(sns.color_palette(my_colors))

ax = sns.factorplot(
    x=X_LABEL, y="y", hue=LEGEND_NAME, data=df, height=5, aspect=1.4, legend=False
)
ax.set(ylabel=Y_LABEL)
# ax.set_xticklabels(rotation=60)

plt.legend(loc="upper left")
plt.savefig(EXP_NAME.format(".png"))
