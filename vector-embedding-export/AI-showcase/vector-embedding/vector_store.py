"""
Minimal in-memory vector store.
"""

from similarity import cosine_similarity

class VectorStore:
    def __init__(self):
        self.texts = []
        self.vectors = []

    def add(self, text, vector):
        self.texts.append(text)
        self.vectors.append(vector)

    def query(self, query_vector, top_k=3):
        scores = []
        for text, vec in zip(self.texts, self.vectors):
            scores.append((text, cosine_similarity(query_vector, vec)))
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
