# DL Training & Applied AI Learning

A hands-on collection of Python, machine learning, deep learning, LLM, and Retrieval-Augmented Generation (RAG) experiments. This repository brings together small applications, notebooks, and learning exercises developed while exploring practical AI workflows.

> **Repository note:** This is a learning and experimentation repository. Individual scripts and notebooks are separate exercises; they are not one integrated application.

## Contents

| File | Description |
|---|---|
| `CPP.txt` | C++ learning notes and reference material. |
| `StreamTutorial.py` | Streamlit demonstration covering text inputs, widgets, forms, charts, CSV upload, and data preview. |
| `AI_chatBoat.py` | Streamlit-based robotics document assistant using PDF/TXT retrieval and an Ollama language model. |
| `ragChatbotLLM.py` | RAG chatbot experiment using document loading, text chunking, embeddings, FAISS, and Ollama. |
| `chatBotDemo.py` | Basic Streamlit and RAG chatbot experiment. |
| `CPP_app.py` | Streamlit application for working with text-based C++ learning material and vector search. |
| `LLM_CPP_app.py` | C++ learning assistant experiment combining retrieval with an Ollama language model. |
| `CNN.py` | Streamlit interface for training and testing a CNN with CIFAR-10 or an uploaded Cats-vs-Dogs ZIP dataset. |
| `cnn_model.py` | CNN model-building function used by `CNN.py`. |
| `app.py` | Streamlit experiment using an Ollama model and structured output parsing. |
| `RAGTutorial.ipynb` | Notebook demonstrating document loading, splitting, Hugging Face embeddings, and FAISS similarity search. |
| `GAN.ipynb` | Notebook implementing a Generative Adversarial Network (GAN) trained on the MNIST handwritten-digit dataset. |
| `task.ipynb` | Empty notebook placeholder; no exercise content is currently included. |

## Topics and technologies

- **Python** — scripting and application development
- **Streamlit** — interactive web interfaces
- **NumPy and Pandas** — numerical and tabular data handling
- **TensorFlow / Keras** — convolutional neural networks and deep learning
- **Matplotlib** — plotting training metrics and generated images
- **LangChain** — document processing and LLM application workflows
- **Hugging Face sentence-transformers** — text embeddings
- **FAISS** — vector similarity search
- **Ollama** — running local language models
- **Jupyter Notebook** — interactive experiments

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/aanandkhawse/DL-Training.git
cd DL-Training
```

Replace the placeholders with your GitHub username and repository name.

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Install the packages required by the application or notebook you want to run. These experiments use different libraries, so a single minimal installation may not cover every file.

```bash
python -m pip install --upgrade pip
pip install streamlit numpy pandas matplotlib tensorflow
pip install langchain langchain-community langchain-text-splitters langchain-huggingface langchain-ollama langchain-classic sentence-transformers faiss-cpu pypdf
pip install jupyter ipykernel
```

If TensorFlow installation is unavailable for your Python version or operating system, consult the official TensorFlow installation guide and use a supported Python environment.

## Run the applications

Run each Streamlit script from the repository root.

### Streamlit learning demo

```bash
streamlit run StreamTutorial.py
```

### Robotics RAG assistant

```bash
streamlit run AI_chatBoat.py
```

The RAG assistant accepts PDF and TXT documents through its sidebar. Save the documents, then build the knowledge base before asking questions.

### RAG chatbot experiment

```bash
streamlit run ragChatbotLLM.py
```

### C++ retrieval experiments

```bash
streamlit run CPP_app.py
```

```bash
streamlit run LLM_CPP_app.py
```

These applications are experiments and may expect their source text or knowledge files to be available in the locations specified in the scripts.

### CNN image classifier

```bash
streamlit run CNN.py
```

The interface provides CIFAR-10 training and a Cats-vs-Dogs ZIP upload option. The uploaded dataset should be arranged in class folders as expected by the application.

### Other LLM demo

```bash
streamlit run app.py
```

### Jupyter notebooks

```bash
jupyter notebook
```

Open `RAGTutorial.ipynb` or `GAN.ipynb` in the Jupyter interface and execute the cells in order.

## Local model requirement for Ollama apps

Some RAG and LLM scripts call Ollama with the model name `gemma2:2b`. To use those scripts:

1. Install and start Ollama on your computer.
2. Download the model:

   ```bash
   ollama pull gemma2:2b
   ```

3. Keep the Ollama service running while using the relevant Streamlit application.

The model download is separate from the Python package installation and may require several gigabytes of disk space.

## Dataset notes

- The GAN notebook downloads and uses the MNIST dataset through TensorFlow/Keras.
- The CNN application uses CIFAR-10 through TensorFlow/Keras or accepts a user-provided Cats-vs-Dogs ZIP dataset.
- PDF/TXT documents for the RAG assistant are supplied by the user through the app. Do not commit private or copyrighted documents without permission.

## Important considerations

- Run only the application you need; the repository contains independent experiments.
- Model downloads, datasets, and generated vector indexes may take additional disk space.
- GPU acceleration depends on the installed TensorFlow build, hardware, drivers, and operating system.
- Do not upload API keys, passwords, private documents, virtual environments, model caches, or large datasets to GitHub.
- The dependency commands above are a broad setup for the listed experiments. Some packages may be unnecessary for a particular script, and package compatibility can vary by Python version.

## Contributing

This repository is maintained as a personal learning collection. Suggestions, issue reports, and improvements are welcome.

## Author

**Anand Khawse**

GitHub: [@aanandkhawse](https://github.com/aanandkhawse)

---

*Built for learning, experimenting, and exploring practical AI and machine learning applications.*
