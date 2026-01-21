"""Test all required imports for the cosmetic sales segmentation project"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import hdbscan
import umap
import scipy
import numba

print("✅ ALL LIBRARIES IMPORTED SUCCESSFULLY!")
print("\n" + "="*60)
print("INSTALLED VERSIONS:")
print("="*60)
print(f"  • Pandas:        {pd.__version__}")
print(f"  • NumPy:         {np.__version__}")
print(f"  • Matplotlib:    {plt.matplotlib.__version__}")
print(f"  • Seaborn:       {sns.__version__}")
print(f"  • Scikit-learn:  {__import__('sklearn').__version__}")
print(f"  • UMAP:          {umap.__version__}")
print(f"  • HDBSCAN:       {hdbscan.__version__}")
print(f"  • SciPy:         {scipy.__version__}")
print(f"  • Numba:         {numba.__version__}")
print("="*60)
print("\n🎉 Your environment is ready for the analysis!")
