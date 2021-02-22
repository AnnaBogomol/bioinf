import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("TCGA-COAD.tsv", sep="\t")

TCGA_A6_2675_11A = []
TCGA_A6_2671_11A = []

gene_crossing = []

for i in df.nlargest(100, "TCGA-A6-2675-11A")["Gene"]:
    TCGA_A6_2675_11A.append(i)
for i in df.nlargest(100, "TCGA-A6-2671-11A")["Gene"]:
    TCGA_A6_2671_11A.append(i)

for i in TCGA_A6_2675_11A:
    if i in TCGA_A6_2671_11A:
        gene_crossing.append(i)

df = pd.read_csv("TCGA-COAD.tsv", sep="\t", index_col=0) # снова считываем файл и присваиваем первому столбцу значение 0
df2 = df[["TCGA-A6-2671-11A", "TCGA-A6-2675-11A"]]  # Создаем новый датафрейм от двух образцов
df2 = df2.nlargest(100, "TCGA-A6-2671-11A")  # Выделили топ-100 генов
df2 = df2.loc[gene_crossing]
sns.scatterplot(x="TCGA-A6-2671-11A", y="TCGA-A6-2675-11A", data=df2)  # обозначили оси и указали, откуда брать данные
plt.tight_layout()
plt.savefig("scatterplot.pdf") # сохранили результат в формате пдф
plt.close()
