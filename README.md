# RAG Pipeline Project

## Project Structure

```
rag_v4
│
├── docs.txt          # Example documents
├── chunk.py          # Text chunking module
├── embedding.py      # Text embedding module
├── faiss_index.py    # FAISS retrieval module
├── rerank.py         # Document reranking module
├── rag_pipeline.py   # Main RAG pipeline
├── eval_dataset.py   # Evaluation dataset
├── evaluate.py       # Evaluation script
├── requirements.txt  # Dependencies
└── README.md         # This file
```

## RAG Pipeline

```
Document
↓
Chunk
↓
Embedding
↓
FAISS Retrieval
↓
Rerank
↓
Evaluation
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from rag_pipeline import RAGPipeline

# Initialize pipeline
pipeline = RAGPipeline()

# Build index from documents
pipeline.build_index('docs.txt')

# Retrieve relevant documents
query = "What is artificial intelligence?"
documents = pipeline.retrieve(query, k=3)

print("Retrieved documents:")
for i, doc in enumerate(documents):
    print(f"{i+1}. {doc}")
```
