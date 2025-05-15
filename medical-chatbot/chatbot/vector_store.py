from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("paraphrase-MiniLM-L3-v2")


client = chromadb.PersistentClient(path=".chromadb")

# Create or get collection
collection = client.get_or_create_collection(name="medical-data")


def add_to_vector_store(documents):
    embeddings = model.encode(documents).tolist()
    ids = [str(i) for i in range(len(documents))]
    collection.add(documents=documents, embeddings=embeddings, ids=ids)
    print(f"Added {len(documents)} documents to vector store.")


def query_vector_store(query, top_k=1):
    query_embedding = model.encode([query]).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=top_k)
    if results["documents"] and results["documents"][0]:
        docs = results["documents"][0]
        return " ".join(docs)
    else:
        return None
