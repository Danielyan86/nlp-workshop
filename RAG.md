- [Retrieval-Augmented Generation (RAG) Knowledge Sharing](#retrieval-augmented-generation-rag-knowledge-sharing)
  - [1. Why Do We Need RAG?](#1-why-do-we-need-rag)
    - [1.1 Limitations of Traditional LLMs](#11-limitations-of-traditional-llms)
  - [2. Use Cases for RAG](#2-use-cases-for-rag)
    - [2.1 Common Scenarios](#21-common-scenarios)
  - [3. RAG Architecture and Principles](#3-rag-architecture-and-principles)
    - [3.1 Basic Components](#31-basic-components)
      - [Overview Diagram](#overview-diagram)
      - [Core Concepts](#core-concepts)
      - [Vector Embedding Example](#vector-embedding-example)
      - [Document Processing Pipeline](#document-processing-pipeline)
      - [Query Processing Pipeline](#query-processing-pipeline)
      - [Response Generation Pipeline](#response-generation-pipeline)
      - [Vector Store Details](#vector-store-details)
  - [4. DIFY DEMO for RAG](#4-dify-demo-for-rag)
    - [4.1 Main Features](#41-main-features)
    - [4.2 RAG Implementation Steps](#42-rag-implementation-steps)
    - [4.3 Verification](#43-verification)

# Retrieval-Augmented Generation (RAG) Knowledge Sharing

## 1. Why Do We Need RAG?

### 1.1 Limitations of Traditional LLMs

1. **Hallucination Issues**

   - Outdated training data
   - Unable to access private data

2. **High Cost for Fine-tuning**

## 2. Use Cases for RAG

### 2.1 Common Scenarios

- Enterprise knowledge base chatbots
- Legal document analysis
- Medical research assistance

## 3. RAG Architecture and Principles

### 3.1 Basic Components

#### Overview Diagram

```mermaid
flowchart TD
    %% Document Processing
    subgraph subGraph0["📄 Document Processing"]
        B["📥 Unstructured Loader"]
        C["✂ Text Processing"]
    end

    %% Vector Storage
    subgraph subGraph1["📂 Vector Storage"]
        E["🔢 Embedding Model"]
        G["🗃️ Vector Store"]
    end

    %% Query & Retrieval
    subgraph subGraph2["🔍 Query & Retrieval"]
        H["🔍 Query"]
        I["🔢 Embedding Model"]
        J["🧩 Query Vector"]
        K["🔍 Text Search"]
        L["📑 Related Text Chunks"]
    end

    %% Response Generation
    subgraph subGraph3["🤖 Response Generation"]
        M["📝 Prompt"]
        N["🤖 LLM"]
        O["📩 Answer"]
    end

    %% Flow connections
    A["📂 Local Documents"] --> B
    B --> C
    C --> E
    E --> G
    H --> I
    I --> J
    J --> K
    K --> L
    L --> M
    M --> N
    N --> O
    G --> K
```

#### Core Concepts

1. **Document Processing**

   - Converts various document formats into plain text
   - Splits text into manageable chunks

2. **Embedding Model**

   - Converts text into numerical vectors
   - Used for both document and query processing

3. **Vector Store**

   - Database for storing document vectors
   - Enables efficient similarity search

4. **Text Search**

   - Retrieves relevant documents using vector similarity
   - Returns context for LLM processing

5. **Response Generation**
   - Combines retrieved context with query
   - Generates contextual responses using LLM

#### Vector Embedding Example

This example demonstrates how text is processed through the RAG pipeline:

1. **Document Processing**

   ```text
   Input Text: "The Eiffel Tower is in Paris, France."

   Tokenized: [
     "The", "Eiffel", "Tower", "is", "in",
     "Paris", ",", "France", "."
   ]

   Embedding Vector (1536D):
   [0.23, -0.75, 0.12, ...] # 1536 dimensions
   ```

2. **Query Processing**

   ```text
   User Query: "Where is the Eiffel Tower?"

   Tokenized: [
     "Where", "is", "the", "Eiffel",
     "Tower", "?"
   ]

   Query Vector (1536D):
   [0.22, -0.74, 0.13, ...]
   ```

3. **Retrieval Process**
   - Vector database calculates similarity scores
   - Finds relevant text chunks based on vector similarity
   - Returns matched content to LLM for response generation

#### Document Processing Pipeline

1. **Local Documents**: Source materials (e.g., PDF, Word, TXT)
2. **Unstructured Loader**: Converts file formats to plain text
3. **Text Splitting**: Breaks text into manageable chunks for processing
4. **Tokenization**: Breaks text into tokens
5. **Embedding Model**: Converts tokens to numerical vectors
6. **Vector Store**: Stores and manages vector data

#### Query Processing Pipeline

1. **Query Input**: User's natural language query
2. **Query Tokenization**: Breaks query into tokens
3. **Query Embedding**: Converts query tokens to vector
4. **Vector Search**: Finds similar vectors in Vector Store
5. **Context Retrieval**: Retrieves relevant text chunks

#### Response Generation Pipeline

1. **Prompt Construction**: Combines query and retrieved context
2. **LLM Processing**: Generates response using the prompt
3. **Response Output**: Final answer to the user

#### Vector Store Details

In a RAG system, each text chunk is converted into a vector and stored in the vector database along with its original content (or reference). Typically, each record contains:

| Field               | Description                                          |
| ------------------- | ---------------------------------------------------- |
| id                  | Unique identifier for the chunk (e.g., UUID)         |
| embedding vector    | Semantic vector (e.g., 768D, 1536D)                  |
| text / metadata     | Original chunk text (with context)                   |
| additional metadata | Document title, source, page number, tags (optional) |

Example record:

```json
{
    "id": "chunk_001",
    "embedding": [0.34, -0.12, 0.77, ...],  // high-dimensional vector
    "text": "The Eiffel Tower is in Paris, France.",
    "metadata": {
        "source": "travel_guide.pdf",
        "page": 23
    }
}
```

This structure enables:

- Efficient vector similarity search
- Original content retrieval
- Source tracking and context preservation

## 4. DIFY DEMO for RAG

DIFY is an open-source LLM application development platform that simplifies the creation of AI applications.

### 4.1 Main Features

- No-code/Low-code development interface
- Built-in RAG pipeline support
- Various LLM provider support
- Visual knowledge base management

### 4.2 RAG Implementation Steps

1. **Environment Setup**

   - Start and setup DIFY in local environment

2. **Knowledge Base Creation**

3. **Document Processing**

   - Upload documents
   - Configure chunk settings
   - Select index mode
     ![RAG Index](./imgs/rag_index.jpg)

4. **Select the Embedding Model**

5. **Retrieval Settings**

   - Vector search: Finds similar content by comparing document vectors in high-dimensional space
   - Full-text search: Traditional keyword-based search across document content

6. **Chunk Preview**
   ![RAG Preview](./imgs/dify_rag_preview.jpg)

7. **Knowledge Created**
   ![Knowledge Created](./imgs/dify_knowledge_created.png)

### 4.3 Verification

1. **Retrieval Testing**
   ![Retrieval Testing](./imgs/dify_knowledge_retreivial.png)

2. **Chat Testing**
   - **Without RAG Example**
     ![Chat Without Knowledge](./imgs/dify_without_knowledge_example.png)
   - **With RAG Example**
     ![Chat With Knowledge](./imgs/dify_with_knowledge_example.png)
