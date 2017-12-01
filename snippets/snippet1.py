import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv/ckpt-10342.csv', sep=',', header=None)
# print(df.values)
# print(type(df.values))
df_cm = pd.DataFrame(df.values, index=list(range(0, 37)),
                     columns=list(range(0, 37)))
plt.figure(figsize=(10, 8))
# sns.heatmap(df_cm, annot=True, cmap="YlGnBu")
sns.heatmap(df_cm, annot=True, cmap=sns.color_palette("Greens"))
# plt.matshow()
plt.savefig('figures/ckpt-10342.svg', format='svg', dpi=1200)
plt.show()
