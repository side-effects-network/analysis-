# A Network Approach to Polypharmacy  
_Exploratory Analysis of Drug-to-Drug Side Effects Using Patient-Centered Data_

##  Project Overview

This repository contains the code and data used in the paper:

**“A Network Approach to Polypharmacy: An Exploratory Analysis of Drug-to-Drug Side Effects Using Patient-Centered Data”**

Our work applies network analysis techniques to a large drug interaction graph to explore the **reactivity** and **harmfulness** of various medications, particularly those most commonly prescribed in the United States. We combine structural graph metrics with crowdsourced rankings of side effect severity to offer a patient-centered perspective on polypharmacy risks.

---
## Methods & Metrics

We built an undirected weighted multigraph where:

- **Nodes** represent drugs.
- **Edges** represent documented side effects due to interactions.
- **Edge weights** reflect perceived severity of side effects (fear score), matched from a separate study using MiniLM sentence embeddings.

Key metrics computed:

- **Simple Degree Centrality** – Unique drug interaction count
- **Multi-edge Degree Centrality** – Total number of interaction edges
- **Weighted Degree** – Harmfulness + frequency combined
- **Averaged Weighted Degree** – Mean harmfulness per interaction
- **Edge Multiplicity** – Number of side effects between specific drug pairs
- **Closeness Centrality** – Proxy for interaction predictability

---

## Data Sources

- BioSNAP Polypharmacy Dataset
https://snap.stanford.edu/biodata/datasets/10017/10017-ChChSe-Decagon.html

- SIDER / OFFSIDES / TWOSIDES
https://nsides.io/

- Perceived Harmfulness Rankings
Gottlieb et al., JMIR, 2015

- Top 300 US Prescribed Drugs (2022)
https://clincalc.com/DrugStats/Top300Drugs.aspx

- PubChem API
https://pubchem.ncbi.nlm.nih.gov/
