# LLM Setup and Configuration

This document outlines the steps to set up an open-source Large Language Model (LLM) like LLaMA 3 or Mistral 7B for the ADVOKC Chatbot project. We will use the Hugging Face `transformers` library for loading the model and `bitsandbytes` for 4-bit quantization to make it more resource-friendly.

## 1. Prerequisites

- Python 3.8+
- Pip (Python package installer)
- Basic understanding of Hugging Face Transformers and PyTorch

## 2. Installation

Install the necessary Python libraries:

```bash
pip install transformers torch bitsandbytes accelerate langchain
```

- `transformers`: For loading and using LLMs from Hugging Face.
- `torch`: The PyTorch library, a dependency for `transformers`.
- `bitsandbytes`: For 4-bit quantization, reducing memory and computational load.
- `accelerate`: Simplifies running PyTorch models on various hardware setups (CPU, GPU, multi-GPU).
- `langchain`: To build the RAG pipeline.

## 3. Choosing and Loading a Model

You can choose between models like LLaMA 3 (e.g., `meta-llama/Meta-Llama-3-8B`) or Mistral 7B (e.g., `mistralai/Mistral-7B-v0.1`).

### Example: Loading Mistral 7B with 4-bit Quantization

Here's how you can load the Mistral 7B model with 4-bit quantization:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

# Define the model ID from Hugging Face Hub
model_id = "mistralai/Mistral-7B-v0.1" # Or use a LLaMA 3 model ID

# Configure 4-bit quantization
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16, # or torch.bfloat16 for newer GPUs
    bnb_4bit_use_double_quant=True,
)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Load the model with quantization config
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    device_map="auto", # Automatically uses GPU if available
)

print(f"Model {model_id} loaded successfully with 4-bit quantization.")

# Example usage (simple prompt)
# prompt = "What is the capital of Nigeria?"
# inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
# outputs = model.generate(**inputs, max_new_tokens=50)
# print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

**Notes:**

- **Model Access:** For some models like LLaMA 3, you might need to request access through their Hugging Face page and authenticate your Hugging Face CLI.
- **`device_map="auto"`:** This will automatically place the model on a GPU if one is available and configured correctly. Ensure you have the necessary CUDA drivers if using an NVIDIA GPU.
- **`bnb_4bit_compute_dtype`:** `torch.float16` is widely supported. `torch.bfloat16` can offer better performance on newer GPUs (e.g., Ampere architecture and later).

## 4. Integrating with LangChain for RAG

LangChain will be used to build the Retrieval Augmented Generation (RAG) pipeline. This involves:

1.  **Loading Documents:** Your curated civic documents.
2.  **Splitting Documents:** Breaking them into smaller chunks.
3.  **Creating Embeddings:** Using a model like `Instructor-Embeddings` (e.g., `hkunlp/instructor-xl`) to generate vector representations of the chunks.
4.  **Storing in VectorDB:** Storing these embeddings in ChromaDB.
5.  **Retrieval:** When a user query comes in, search ChromaDB for relevant document chunks.
6.  **Augmentation & Generation:** Inject the retrieved context into the prompt for the LLM, which then generates the answer.

### Example Snippet (Conceptual LangChain Integration)

```python
# (Assuming 'model' and 'tokenizer' are loaded as shown above)

# from langchain.llms import HuggingFacePipeline
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import pipeline

# Create a Hugging Face pipeline for text generation
text_generation_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    # torch_dtype=torch.float16, # Already handled by bitsandbytes if compute_dtype is set
    # device_map="auto" # Already handled by model loading
)

llm_pipeline = HuggingFacePipeline(pipeline=text_generation_pipeline)

# This 'llm_pipeline' can now be used in LangChain chains, for example:
# from langchain.chains import RetrievalQA
# from langchain.vectorstores import Chroma # Your ChromaDB instance
# from langchain.embeddings import HuggingFaceInstructEmbeddings

# embeddings_model = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
# vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embeddings_model)
# retriever = vector_store.as_retriever()

# qa_chain = RetrievalQA.from_chain_type(
#    llm=llm_pipeline,
#    chain_type="stuff", # Or other chain types like "map_reduce", "refine"
#    retriever=retriever,
#    return_source_documents=True
# )

# query = "What are the duties of a Nigerian citizen?"
# result = qa_chain({"query": query})
# print(result["result"])
# print(result["source_documents"])
```

## 5. Deployment Considerations

-   **GPU Requirements:** Even with 4-bit quantization, running these models (especially larger ones like LLaMA 3 13B) requires a GPU with sufficient VRAM (e.g., NVIDIA RTX 30xx/40xx series with at least 12-16GB VRAM for comfortable operation, more for larger models or batch processing).
-   **Deployment Platforms:** Platforms like Railway, Render, or DigitalOcean offer GPU instances. You'll need to configure your deployment environment to include the necessary drivers and libraries.
-   **Model Caching:** Hugging Face models are downloaded to a cache directory (`~/.cache/huggingface/hub` by default). Ensure this is handled correctly in your deployment environment to avoid re-downloading large models on every startup.

This document provides a starting point. Specific configurations may need adjustments based on the chosen model, hardware, and further development of the RAG pipeline.
