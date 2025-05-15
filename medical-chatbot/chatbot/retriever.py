from .vector_store import query_vector_store

def get_context(query, top_k=1):
    results = query_vector_store(query, top_k=top_k)
    return " ".join(results)
