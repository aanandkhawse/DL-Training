Programming, AI & Machine Learning Learning Repository
A collection of hands-on learning exercises and prototype applications covering C++, Python, Streamlit, retrieval-augmented generation (RAG), large language models (LLMs), and convolutional neural networks (CNNs).
This repository brings together programming notes, notebooks, and small applications. The examples are intended for learning and experimentation, not production deployment.
Repository contents
Programming and Streamlit
File	Description
`CPP.txt`	C++ notes and reference material.
`StreamTutorial.py`	Streamlit demonstration app using NumPy and Pandas.
RAG and LLM experiments
File	Description
`RAGTutorial.ipynb`	Notebook demonstrating document loading, text splitting, Hugging Face embeddings, FAISS indexing, and similarity retrieval.
`AI_chatBoat.py`	Streamlit-based chatbot/RAG experiment.
`CPP_app.py`	Streamlit app for retrieving information from C++ source material.
`LLM_CPP_app.py`	C++ document retrieval with an Ollama-backed language-model workflow.
`ragChatbotLLM.py`	RAG chatbot experiment using LangChain and Ollama.
`chatBotDemo.py`	Basic document-based chatbot demonstration.
`app.py`	Streamlit and Ollama prompt/chat application.
CNN experiments
File	Description
`CNN.py`	Streamlit interface for CNN/image-classification experiments.
`cnn_model.py`	TensorFlow/Keras CNN model definition.
`GAN.ipynb`	Notebook for generative adversarial network (GAN) experiments.
`task.ipynb` is an empty notebook placeholder and is included as supplied.
Requirements
Python 3.10 or newer is recommended.
Some examples require locally installed external software or model files:
Ollama must be installed and running for the Ollama-based applications.
TensorFlow installation depends on your operating system and Python version.
Hugging Face embedding models may be downloaded the first time they are used.
Setup
Create and activate a virtual environment:
```bash
python -m venv .venv
```
On Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```
Install the Python dependencies:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
The full requirements file includes packages for the different experiments. TensorFlow is a large dependency; if you only want to run the RAG or Streamlit examples, you can install only the packages needed for that example (see below).
Run examples
Streamlit tutorial
```bash
streamlit run StreamTutorial.py
```
RAG notebook
```bash
jupyter notebook
```
Open `RAGTutorial.ipynb` and run its cells. Keep `CPP.txt` in the same folder if the notebook loads it using a relative path. The notebook builds a FAISS index for similarity retrieval; it does not necessarily generate a natural-language answer.
RAG / LLM Streamlit applications
Run the relevant script, for example:
```bash
streamlit run AI_chatBoat.py
```
Other experiments can be started similarly, such as `streamlit run CPP_app.py` or `streamlit run LLM_CPP_app.py`.
Ollama-based scripts require Ollama to be installed, running, and configured with the model name expected by the script. Check each script before running it.
CNN application
```bash
streamlit run CNN.py
```
The CNN application uses TensorFlow/Keras. Check the script's expected dataset/input format before running it.
Dependency groups
For a smaller installation, install only what the selected experiment needs:
Streamlit tutorial
```bash
pip install streamlit pandas numpy
```
RAG and Hugging Face / FAISS
```bash
pip install streamlit langchain-community langchain-text-splitters langchain-huggingface langchain-ollama langchain-core langchain-classic faiss-cpu sentence-transformers
```
CNN experiments
```bash
pip install streamlit tensorflow matplotlib numpy
```
Notes and limitations
These files are independent learning experiments; they are not one unified application.
Dependency compatibility may vary by Python version and operating system.
Ollama applications need a separate Ollama installation and a compatible model.
CNN scripts may require datasets and files that are not included in this repository.
Review file paths, model names, and input requirements before running an individual experiment.
Do not commit API keys, credentials, private datasets, large model weights, or local virtual environments.
Author
Anand Khawse
