# Palmer Penguins — Clustering con Mean-Shift

**Progetto universitario — Modelli e principi della percezione**
Università degli Studi di Milano

## Obiettivo del progetto

Il progetto si propone di analizzare il dataset *Palmer Penguins* mediante l'algoritmo di clustering non supervisionato **Mean-Shift**, con l'obiettivo di individuare gruppi di pinguini caratterizzati da proprietà morfologiche simili.

La domanda di ricerca è:

**È possibile individuare spontaneamente gruppi corrispondenti alle specie di pinguini, senza conoscere preventivamente il numero di specie presenti?**

L'algoritmo viene applicato senza utilizzare le etichette biologiche. Queste vengono conservate esclusivamente per la successiva fase di validazione esterna.

## Dataset

Il dataset Palmer Penguins contiene inizialmente **344 osservazioni**, appartenenti a tre specie:

- Adélie (*Pygoscelis adeliae*)
- Chinstrap (*Pygoscelis antarcticus*)
- Gentoo (*Pygoscelis papua*)

Dopo la pulizia sono state conservate **342 osservazioni complete**.

Per il clustering vengono utilizzate quattro caratteristiche fisiche:

| Caratteristica | Descrizione           |
| -------------- | --------------------- |
| Culmen Length  | Lunghezza del becco   |
| Culmen Depth   | Profondità del becco  |
| Flipper Length | Lunghezza della pinna |
| Body Mass      | Massa corporea        |

Le variabili sono state standardizzate mediante **Z-score**, per renderle confrontabili indipendentemente dalle unità di misura originali.

## Metodologia

Il progetto è suddiviso in tre fasi principali.

### 1. Analisi e preprocessing

Analisi esplorativa del dataset, gestione dei valori mancanti, selezione delle caratteristiche e standardizzazione.

### 2. Applicazione di Mean-Shift

Implementazione dell'algoritmo mediante Python e la libreria `scikit-learn`.

L'implementazione utilizza un **flat kernel**, che assegna lo stesso peso alle osservazioni comprese nel bandwidth ed esclude quelle esterne.

Sono stati condotti esperimenti con differenti valori di bandwidth, analizzando:

- Numero e dimensioni dei cluster individuati.
- Coordinate dei mode.
- Silhouette Score.
- Variazioni nelle assegnazioni dei pinguini.
- Comportamento di un'osservazione isolata.
- Visualizzazione bidimensionale mediante PCA.

### 3. Validazione e interpretazione

La fase conclusiva prevede il confronto tra i cluster ottenuti e le specie biologiche reali, utilizzando metriche di validazione esterna e discutendo il significato dei risultati.

## Risultati preliminari

Gli esperimenti mostrano che il numero di cluster individuati varia in funzione del bandwidth.

| Bandwidth | Cluster | Silhouette Score |
| --------- | ------: | ---------------: |
| 1,3705    |       4 |           0,4259 |
| 1,40      |       3 |           0,4441 |
| 1,50      |       2 |           0,5203 |
| 2,00      |       2 |           0,5303 |

La configurazione con **h = 2,0** è stata selezionata per la validazione principale, avendo ottenuto la Silhouette Score più elevata tra i valori sperimentati.

La configurazione con **h = 1,40** è stata conservata come alternativa per approfondire il confronto tra differenti raggruppamenti.

La PCA utilizzata per la visualizzazione conserva complessivamente circa **l'88,16% della varianza**. Il clustering viene comunque eseguito nello spazio originale delle quattro caratteristiche standardizzate.

I risultati mostrano una transizione da quattro a tre e infine a due cluster all'aumentare del bandwidth. La corrispondenza con le specie reali resta oggetto della validazione finale.

## Organizzazione dei file

Il repository contiene attualmente:

- **`palmer-penguins-mean-shift/data_processed/`** — Dataset puliti e standardizzati.
- **`palmer-penguins-mean-shift/notebook/02_mean_shift.ipynb`** — Implementazione Mean-Shift, esperimenti e grafici.
- **`palmer-penguins-mean-shift/results/`** — Assegnazioni dei cluster per la validazione.
- **`palmer-penguins-mean-shift/figures/`** — Grafici PCA, analisi del bandwidth e silhouette, in PNG e SVG.

Saranno aggiunti i notebook relativi al preprocessing e alla validazione, oltre alla presentazione finale.

## Tecnologie utilizzate

- **Python** — Linguaggio di programmazione.
- **Pandas** — Gestione e analisi dei dati.
- **NumPy** — Operazioni numeriche e calcolo delle distanze.
- **scikit-learn** — Mean-Shift, PCA, standardizzazione e silhouette.
- **Matplotlib** — Realizzazione dei grafici.
- **Google Colab / Jupyter Notebook** — Ambiente di sviluppo ed esecuzione.

## Esecuzione del progetto

Il notebook principale è disponibile in `palmer-penguins-mean-shift/notebook/02_mean_shift.ipynb`.

Per eseguirlo in Google Colab è necessario rendere disponibili nella sessione i due file `penguins_meanshift_X_std.csv` e `penguins_metadata_eval.csv`, quindi eseguire le celle nell'ordine previsto.

Il notebook produce le assegnazioni dei cluster e le visualizzazioni degli esperimenti.

## Componenti del progetto

Il lavoro è suddiviso in tre attività:

1. **Analisi esplorativa e preparazione del dataset.**
2. **Implementazione di Mean-Shift, sperimentazione e visualizzazione.**
3. **Validazione esterna, interpretazione e conclusioni.**

## Fonti e riferimenti

- [Palmer Penguins Dataset — Kaggle](https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data)
- [Documentazione MeanShift — scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html)
- Gorman, K. B., Williams, T. D. & Fraser, W. R. (2014). *Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins*. PLOS ONE, 9(3), e90081.

---

*Progetto realizzato a scopo didattico per l'insegnamento di Principi e modelli della percezione presso l'Università degli Studi di Milano.*
