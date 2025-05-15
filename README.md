# 🩺 Medical Chatbot (AI-Powered)

This is an AI-powered medical chatbot built using Python, Sentence Transformers, and ChromaDB. It allows users to ask health-related questions and provides relevant medical context from preloaded documents.

## 🚀 Features
- Embedding-based context retrieval using Sentence Transformers
- Fast vector search with ChromaDB
- Web UI powered by Flask
- Modular design for easy extension

## 📁 Project Structure
```
medical-chatbot/
│
├── chatbot/               # Core modules (vector store, retriever)
├── data/                  # Your medical text data (e.g., health.txt)
├── templates/             # HTML template(s) for web UI
├── app.py                 # Flask-based web interface
├── load_data.py           # Load documents into vector store
├── requirements.txt       # Python dependencies
└── .gitignore             # Excludes venv, cache, system files
```

## 🛠️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/Demodox/medical-chatbot.git
   cd medical-chatbot
   ```

2. Create & activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Load data (if needed):
   ```bash
   python load_data.py
   ```

5. Start the chatbot web UI:
   ```bash
   python app.py
   ```

Then visit: `http://127.0.0.1:5000`

## ⚠️ Notes
- Avoid pushing large files like model binaries or virtual environments.
- Make sure `.gitignore` is correctly excluding unnecessary files.

---

Feel free to contribute or extend the functionality!
