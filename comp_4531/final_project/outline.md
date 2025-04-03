# Final Project - CNN for Protein Prediction

## Problem Statement

The central dogma of biology describes the flow and lineage of gentic material to functional proteins. In short, it outlines DNA's transcription into RNA and RNA's translation into amino acidsm which eventually form to make up proteins. This is an important process as genetic material is the foundations of life. 

A protein's form or stucture, has a direct relationship with its function. Understanding both form and function not only unlocks so much insight into what proteins literally do and function, but also informs many other applications. Medical research, biotechnology, drug development, genetic testing, etc all can benefit from understanding how proteins are structured, formed, and how they function. Again, proteins are the workhorses for all the functions in biology - whether good or bad. 

Because of this fundamental importance, being able to predict proteins types, their structure, and even the proteins themselves based on DNA, chemical signals, and even structural data, is something that many humans have been trying to solve. 

In this deep learning project, the goal is to use protein data from the CATH database to predict protein secondary stuctures. This emulates and the general work noted above. Again, there are a lot of potential applications here. However, in short, to be able to predict aspects of proteins, based on general characterisits works towards not only understanding the proteins themselves and their evolution better, but also making progress towards understanding novel applications of future protein synthesis, structure, and function.

## Deep Learning 
Unlike classical machine learning problems that is based on making regressions or classifications on tabular data, the data used here is made up of 3D arrays of (x,y,z) coordinates. This is not easily solveable by nominal ML methods line logistic regression, random forests, or even gradient boosted trees. Deep learning, and specifically, convolutional neural networks are a great application for this type of problem.

# CATH Database:

The CATH hierarchy is a classification system for protein domain structures. It organizes protein domains into four main levels:

1. Class (C): Domains are categorized based on their secondary structure content. The main classes are:
   - Mainly Alpha (predominantly α-helices)
   - Mainly Beta (predominantly β-sheets)
   - Mixed Alpha-Beta (significant amount of both α-helices and β-sheets)
   - Few Secondary Structures

2. Architecture (A): This level describes the overall shape and arrangement of secondary structures in three-dimensional space.

3. Topology/fold (T): At this level, domains are grouped based on the connectivity and arrangement of their secondary structure elements.

4. Homologous superfamily (H): Domains are classified into this level if there is strong evidence of evolutionary relatedness. This is based on structural, functional, and sequence similarities.

The CATH database was created in the mid-1990s by Professor Christine Orengo and colleagues at University College London. It uses a combination of automatic methods and manual curation to classify protein domains from experimentally determined structures in the Protein Data Bank. The original goal of this classification was to help in identifying relationships between protein structures. In biology, it is known that stucture informs function. Understanding structure can lead to the understanding of protein evolution and function!
 
 ## cath_3class

For this work, I am focusing on the simplest dataset, `cath_3class.npz`. This dataset focuses soley on the Class level of the hierarchy. 

Key attributes of this data:

1. Class-level focus: The dataset concentrates on three of the four main classes in CATH: Mainly Alpha, Mainly Beta, and Alpha Beta (no "Few secondary structures" class due to its small size and heterogeneity).

2. Balanced representation: The dataset reduces each of the three classes to have an equal number of members.

3. Structural simplification: It contains only Carbon-alpha positions for each protein (each position represents a single atom for each amino acid).

4. Secondary structure detection: The main task facilitated by this dataset is the detection and quantification of protein secondary structures (alpha helices and beta strands).

# Training Data

The data used for training are the (x,y,z) coordinates of single Carbon-alpha positions for each amino acide within a protein. From these (x,y,z), coordiantes, the hope is to be able to predict whether a protein is 'Mainly Alpha', 'Mainly Beta', or 'Alpha-Beta'.

The data itself is of shape (16962, 1202, 3) where:
- 16962 is the number of proteins in the dataset
- 1202 is the number of atoms (each column represents an atom in the protein)
  - The max number of atoms in a single protein in this data is 1202 (therefore, the data itself resembles a sparse matrix where you have an array of (x, y, z) coordinates instead of 1's and 0 otherwise)
- 3 is the dimensions of the protein-atom positions
  - This array has (x, y, z) coordinates of each c-a position of each amino acid in the protein

In more detail, the first protein has shape (1202, 3) with the following values:

```data['positions'][0].shape````

```bash
array([[-0.46251011, 14.0216713 , -0.11604881],
       [ 2.52248955, 14.92267227,  2.01995087],
       [ 0.57148933, 16.07967186,  5.23795128],
       ...,
       [ 0.        ,  0.        ,  0.        ],
       [ 0.        ,  0.        ,  0.        ],
       [ 0.        ,  0.        ,  0.        ]])
```

Each row in the array above is the (x,y,z) coordinate of a single c-a position of a single amino acid in the protein. This protein has 175 atom representations and so the rest of the 1027 rows (1202-175) are arrays with [0, 0, 0] for each coordinate.

# Output Data
