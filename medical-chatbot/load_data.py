from chatbot.vector_store import add_to_vector_store

def load_documents():
    documents = []
    # List all data files 
    file_paths = [
        'data/fever.txt',
        'data/medical_knowledge.txt'
    ]

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if content:
                documents.append(content)

    return documents

if __name__ == "__main__":
    print("Loading medical documents into vector store...")
    docs = load_documents()
    add_to_vector_store(docs)
    print(f"✅ Loaded {len(docs)} documents.")
