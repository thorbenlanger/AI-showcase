"""
End-to-end demo for vector embeddings.
"""

from embeddings import embed
from vector_store import VectorStore

def main():
    documents = [
        "Vector embeddings are used to enable semantic search in large document collections.",
        "The payment service returns HTTP 403 when the API key is missing or invalid.",
        "User passwords are stored as salted hashes to improve security.",
        "Cosine similarity is commonly used to compare embedding vectors.",
        "Rate limiting prevents clients from sending too many requests in a short time window."
    ]

    store = VectorStore()
    vectors = embed(documents)

    for text, vec in zip(documents, vectors):
        store.add(text, vec)

    query = "How do we search documents by meaning instead of keywords?"
    query_vec = embed([query])[0]

    results = store.query(query_vec)

    print("Query:", query)
    print("Results:")
    for text, score in results:
        print(f"{score:.3f} | {text}")

if __name__ == "__main__":
    main()
