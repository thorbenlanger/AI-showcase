"""
Similarity metrics for embeddings.
"""

import numpy as np

def cosine_similarity(a, b):
    """
    Cosine similarity for normalized vectors.
    """
    return float(np.dot(a, b))
