""""
This code in this file grabs data from 'cath_3class_ca.npz' and runs a baseline NN.

Data is sourced from: https://github.com/wouterboomsma/cath_datasets?tab=readme-ov-file

cath_3class_ca data:

The cath_3class.npz dataset is the simplest set. It considers the "class" level of 
the CATH hierarchy, which in the CATH database consists of "Mainly Alpha", "Mainly Beta", "Alpha Beta" and 
"Few secondary structures". Since the latter category is small, and structurally heterogeneous, we omit
it from our set. The three remaining categories are each reduced to have the same number of members 
(see filtering below), thus creating a balanced set. The three classes differ mainly in the relative quantities of 
alpha helices and beta strands (protein secondary structure). The main task in this set is thus to detect 
protein secondary structure in any orientation, and quantify the total amount of the different 
secondary structure elements in the entire image. The dataset contains only Carbon-alpha positions for 
each protein (i.e. only a single atom for each amino acid).

Filtering:

The sets are based on a 40% homology-reduced set of PDB structures downloaded from the CATH server. We then filter 
to obtain balanced categories (equal number of members) at the hierarchy level of interest. For instance, 
for the 3class set, there are about 2500 data points for each class. In reducing the size, we use the structures 
with highest resolution (best experimental quality), with the additional constraint that all included structures with 
within a 50Å sphere centered around the center of mass of the protein. This last constraint was introduced to allow 
us to represent all proteins within a well-defined grid size. The constraint is only violated by a small fraction of 
the original data set.

Splits:

We provide a 10-fold split of the data, for purposes of separation into train/validation/test sets or cross validation.
In addition to the 40% sequence identity cut-off between any entry in the dataset, any two members from different splits
are guaranteed to originate from different categories at the "superfamily" level in the CATH hierarchy. In addition, 
all splits are guaranteed to have members from all categories at the level you are classifying with respect to 
(i.e., the class3 set has all 3 classes present in all splits). Note that due to the requirements of non-overlaps at the 
topology level, the splits are not always entirely of equal size.
"""

import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def load_data(path: str) -> np.lib.npyio.NpzFile:
    """
    Loads .npz data.
    Args:
        path (str): path to .npz file
    Returns
        numpy.lib.npyio.NpzFile
    """
    data = np.load(path)

    return data

def load_arrays(data: np.lib.npyio.NpzFile) -> dict[str:np.ndarray]:
    """
    Returns each array in the .npz
    file data.
    Args:
        data (NpzFile): numpy data file
    Returns:
        dict[str: numpy.ndarray]
    """
    n_atoms = data['n_atoms']
    atom_types = data['atom_types']
    res_indices = data['res_indices']
    positions = data['positions']
    labels = data['labels']

    protein_data = {
        "n_atoms": n_atoms,
        "atom_types": atom_types,
        "res_indices": res_indices,
        "positions": positions,
        "labels": labels
    }

    return protein_data

if __name__ == '__main__':
    data = load_data('cath_3class_ca.npz')

    print('Npz Data:')
    print(data)

    protein_data = load_arrays(data)

    print(protein_data['positions'])
