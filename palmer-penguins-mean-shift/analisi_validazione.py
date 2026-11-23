
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import adjusted_rand_score
from sklearn.decomposition import PCA # Importiamo la PCA, che useremo per ridurre le 4 caratteristiche dei pinguini a 2 dimensioni e visualizzare i dati in un grafico

# Leggiamo i file del progetto (tre tabelle), ed è proprio il comando read_csv ad aprire i file
specie = pd.read_csv("dati/penguins_metadata_eval.csv")
cluster = pd.read_csv("dati/penguins_cluster_assignments.csv")
bandwidth = pd.read_csv("dati/riepilogo_bandwidth.csv")

# Mostriamo le dimensioni dei file, e shape ci dice quante righe e colonne ci sono
print("Dimensioni del file delle specie:", specie.shape)
print("Dimensioni del file dei cluster:", cluster.shape)

# Mostriamo le prime righe
print("\nPrime righe del file delle specie:")
print(specie.head())

print("\nPrime righe del file dei cluster:")
print(cluster.head())

# Dobbiamo conoscere le colonne, e facciamo questo perchè dobbiamo individuare la colonna che contiene le specie reali, e quelle che contengono le assegnazioni dei cluster
print("\nColonne del file delle specie:")
print(specie.columns.tolist())

print("\nColonne del file dei cluster:")
print(cluster.columns.tolist())


# Controlliamo che i file contengano lo stesso numero di pinguini
print("\nNumero di pinguini nel file delle specie:", len(specie))
print("Numero di pinguini nel file dei cluster:", len(cluster))

# Controlliamo che gli indici dei pinguini corrispondano
indici_corrispondenti = (
    specie["Original_Row_Index"].equals(
        cluster["Original_Row_Index"]
    )
)

print("\nGli indici corrispondono?", indici_corrispondenti)

# Visualizziamo le specie presenti
print("\nSpecie presenti nel dataset:")
print(specie["Species"].value_counts())

# Confrontiamo le specie reali con i cluster ottenuti, e da qui iniziamo la validazione esterna

print("\nConfronto specie e cluster con bandwidth 2.0:")
tabella_h2 = pd.crosstab(
    specie["Species"],
    cluster["cluster_h2_0"]
)
print(tabella_h2)

print("\nConfronto specie e cluster con bandwidth 1.4:")
tabella_h1 = pd.crosstab(
    specie["Species"],
    cluster["cluster_h1_4"]
)
print(tabella_h1)

# Calcoliamo l'Adjusted Rand Index (ARI)

ari_h2 = adjusted_rand_score(
    specie["Species"],
    cluster["cluster_h2_0"]
)

ari_h1 = adjusted_rand_score(
    specie["Species"],
    cluster["cluster_h1_4"]
)

print("\nAdjusted Rand Index:")
print("ARI con bandwidth 2.0:", round(ari_h2, 4))
print("ARI con bandwidth 1.4:", round(ari_h1, 4))

# Leggiamo le variabili standardizzate
dati_std = pd.read_csv("dati/penguins_meanshift_X_std.csv")

print("\nDimensioni dei dati standardizzati:")
print(dati_std.shape)

print("\nPrime righe dei dati standardizzati:")
print(dati_std.head())

# Riduciamo le 4 variabili a 2 componenti principali
pca = PCA(n_components=2)

dati_pca = pca.fit_transform(dati_std)

print("\nDimensioni dei dati dopo la PCA:")
print(dati_pca.shape)

print("\nVarianza spiegata dalle due componenti:")
print(pca.explained_variance_ratio_)

print(
    "Varianza totale spiegata:",
    round(sum(pca.explained_variance_ratio_) * 100, 2),
    "%"
)

# Creiamo il grafico PCA per confrontare i cluster

plt.figure(figsize=(12, 5))

# Grafico con bandwidth 1.4
plt.subplot(1, 2, 1)

plt.scatter(
    dati_pca[:, 0],
    dati_pca[:, 1],
    c=cluster["cluster_h1_4"],
    cmap="viridis",
    s=25
)

plt.title("Mean-Shift - Bandwidth 1.4")
plt.xlabel("Prima componente principale")
plt.ylabel("Seconda componente principale")

# Grafico con bandwidth 2.0
plt.subplot(1, 2, 2)

plt.scatter(
    dati_pca[:, 0],
    dati_pca[:, 1],
    c=cluster["cluster_h2_0"],
    cmap="viridis",
    s=25
)

plt.title("Mean-Shift - Bandwidth 2.0")
plt.xlabel("Prima componente principale")
plt.ylabel("Seconda componente principale")

plt.tight_layout()
plt.show()