# Programming, Streamlit & RAG Learning Repository

A hands-on learning repository containing C++ notes, a Streamlit demonstration, and a notebook that builds a small retrieval-augmented generation (RAG) retrieval workflow over a local text file.

## Repository contents

| File | Purpose |
|---|---|
| `CPP.txt` | Source text loaded by the RAG notebook |
| `StreamTutorial.py` | Streamlit demo application |
| `RAGTutorial.ipynb` | Demonstrates loading text, splitting documents, creating Hugging Face embeddings, indexing with FAISS, and similarity search |
| `requirements.txt` | Python dependencies for the app and notebook |
| `.gitignore` | Excludes local environments and generated files |

## Requirements

- Python 3.10 or newer recommended
- Internet access on the first run so the Hugging Face embedding model can be downloaded

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\\Scripts\\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the Streamlit demo

```bash
streamlit run StreamTutorial.py
```

## Run the RAG notebook

Start Jupyter:

```bash
jupyter notebook
```

Open `RAGTutorial.ipynb` and run the cells from top to bottom. Keep `CPP.txt` in the same directory as the notebook because the notebook loads it using a relative path.

The notebook creates embeddings with `sentence-transformers/all-MiniLM-L6-v2`, stores them in a local in-memory FAISS index, and retrieves text chunks similar to a query. It performs retrieval; it does not itself generate an answer with a language model.

## Notes

- The first embedding-model run may download model files.
- The notebook builds the FAISS index during execution; the index is not persisted to disk.
- This is a learning project. Verify and adapt examples before using them in production.

## Author

**Anand Khawse**

# 

# GitHub: \[@aanandkhawse](https://github.com/aanandkhawse)

# 

