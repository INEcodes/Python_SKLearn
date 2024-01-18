import numpy as np
from scipy import sparse
eye = np.eye(4)
print("Numpy array:\n", eye)
sparse_matrix = sparse.csr_matrix(eye)
print("\nScipy sparse CSR matrix:\n", sparse_matrix)