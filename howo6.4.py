import pandas as pd

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
cross = len(gene_crossing)
print(TCGA_A6_2675_11A)  # Топ-100 генов в образце TCGA-A6-2675-11A
print(TCGA_A6_2671_11A)  # Топ-100 генов в образце TCGA-A6-2671-11A
print(gene_crossing)  # Гены, в пересечении множеств этих образцов
print(cross)  # Количество генов в пересечении
