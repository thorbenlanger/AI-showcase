"""
Text → vector embedding module.
"""

from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts):
    """
    Convert a list of texts into normalized vector embeddings.
    """
    return _model.encode(texts, normalize_embeddings=True)
