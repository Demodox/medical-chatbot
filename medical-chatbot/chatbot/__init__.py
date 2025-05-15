from .retriever import get_context

def get_medical_response(query):
    context = get_context(query, top_k=3)
    return f"Based on medical data, here's relevant information:\n{context}"
