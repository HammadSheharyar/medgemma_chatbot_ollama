# MedGemma Local Setup (CPU) with Ollama

## Overview

This project demonstrates how to run the **MedGemma medical language model locally** using **Ollama** on a **CPU-only Windows machine**.

The setup uses a **quantized GGUF model**, allowing efficient inference on systems without a GPU.

This project can later be extended to build:

* Medical chatbots
* Clinical knowledge assistants
* Medical RAG (Retrieval-Augmented Generation) systems

---

# System Requirements

Minimum requirements:

| Component | Requirement              |
| --------- | ------------------------ |
| OS        | Windows   |
| RAM       | 16 GB recommended        |
| GPU       | Not required             |
| Runtime   | Ollama                   |
| Python    | Optional (for API usage) |

Tested Configuration:

* Windows 10
* 16GB RAM
* CPU-only system
* Ollama v0.17.6

---

# Project Structure

```
medgemma-local/
│
├── models/
│   └── medgemma-4b-it-q4_k_m.gguf
│
├── Modelfile
│
└── README.md
```

Description:

* **models/** → contains the downloaded GGUF model
* **Modelfile** → configuration file used by Ollama
* **README.md** → project documentation

---

# Step 1 — Install Ollama

Download and install Ollama from:

https://ollama.com

Verify installation:

```
ollama --version
```

Example output:

```
ollama version 0.17.6
```

---

# Step 2 — Download MedGemma Model

Download the **GGUF quantized model** from Hugging Face.
https://huggingface.co/hungqbui/medgemma-4b-it-Q4_K_M-GGUF/tree/main

Example model:

```
medgemma-4b-it-q4_k_m.gguf
```

Place the model in:

```
medgemma-local/models/
```

Example path:

```
E:\medgemma-local\models\medgemma-4b-it-q4_k_m.gguf
```

---

# Step 3 — Create Modelfile

Create a file named:

```
Modelfile
```

(no extension)

Add the following configuration:

```
FROM ./models/medgemma-4b-it-q4_k_m.gguf

SYSTEM You are MedGemma, a helpful AI assistant specialized in medical knowledge. Provide clear and safe medical information but remind users to consult healthcare professionals for diagnosis.
```

---

# Step 4 — Create the Ollama Model

Navigate to the project folder:

```
cd E:\medgemma-local
```

Run:

```
ollama create medgemma-local -f Modelfile
```

Expected output:

```
creating model...
success
```

---

# Step 5 — Verify Model Installation

Run:

```
ollama list
```

Example output:

```
NAME             SIZE
medgemma-local   ~2-3GB
gemma3:1b
```

---

# Step 6 — Run the Model

Start the chatbot:

```
ollama run medgemma-local
```

Example:

```
>>> What are the symptoms of diabetes?
```

The model will generate a medical explanation.

---



#  — Build a Chatbot UI

Install Streamlit:

```
pip install streamlit
```

Example `app.py`:


Run the application:

```
streamlit run app.py
```

---

# Future Improvements

Possible extensions for this project:

### Medical RAG System

Integrate with:

* LangChain
* FAISS
* Medical datasets (PubMed, WHO)

### Knowledge-Augmented Assistant

Add:

* medical textbooks
* research papers
* clinical guidelines

### Web Application

Deploy using:

* Streamlit
* FastAPI
* Docker

---

# Disclaimer

This system provides **informational medical guidance only** and should not replace professional medical advice.
Always consult a qualified healthcare professional for diagnosis and treatment.

---

# Author

Muhammad Hammad

AI / LLM Developer
Research interests:

* Generative AI
* Retrieval Augmented Generation
* AI for Healthcare
* LLM systems
