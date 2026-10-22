---
url: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/build-llm-apps-using-llamaindex/
title: Build LLM-powered applications using LlamaIndex \u00a0|\u00a0 AlloyDB Omni using containers: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:09.179027+00:00
---

# Build LLM-powered applications using LlamaIndex  |  AlloyDB Omni using containers: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/build-llm-apps-using-llamaindex/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview)



Send feedback 

#  Build LLM-powered applications using LlamaIndex Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/build-llm-apps-using-llamaindex)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/build-llm-apps-using-llamaindex)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/build-llm-apps-using-llamaindex)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/build-llm-apps-using-llamaindex)



This page describes some use cases for building LLM-powered applications using LlamaIndex integrated with AlloyDB Omni. Links to notebooks on GitHub are provided to help you explore approaches or to help you develop your application.

LlamaIndex is a generative AI orchestration framework that lets you connect and integrate data sources with large language models (LLMs). You can use LlamaIndex to build applications that access and query information from private or domain-specific data using natural language queries.

LlamaIndex acts as a bridge between custom data and LLMs, facilitating the development of knowledge assistant applications with retrieval-augmented generation (RAG) capabilities.

LlamaIndex is well suited for document-centric applications because it emphasizes structured document management, which simplifies indexing and retrieval. This framework features optimized query mechanisms that enhance the speed and relevance of information access, along with robust metadata handling for nuanced filtering.

For more information about the LlamaIndex framework, see the [LlamaIndex product documentation](https://www.llamaindex.ai/framework).

## LlamaIndex components

AlloyDB Omni offers the following LlamaIndex interfaces:

  * Vector Store
  * Document Store
  * Index Stores
  * Chat Stores
  * Document Reader



Learn how to use LlamaIndex with the [Quickstart for AlloyDB Omni](https://github.com/googleapis/llama-index-alloydb-pg-python/blob/main/samples/llama_index_quick_start.ipynb).

## Vector Store

This LlamaIndex integration lets you use the robust and scalable nature of AlloyDB Omni to store and manage your LlamaIndex data. By combining the indexing and querying capabilities of LlamaIndex with the high performance and reliability of AlloyDB Omni, you can build more efficient and scalable LLM-powered applications.

LlamaIndex breaks down a document—doc, text, and PDFs—into document components called _nodes_. The [VectorStore](https://developers.llamaindex.ai/python/framework/module_guides/storing/vector_stores/) can only contain the embedding vectors of ingested node contents and the text of nodes. A node contains text content, vector embeddings, and metadata. You can apply filters on these metadata fields to restrict node retrieval to those that match specified metadata criteria.

To work with vector stores in AlloyDB Omni, use the `AlloyDBVectorStore` class. For more information, see [LlamaIndex Vector Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/vector_stores/).

### Store vector embeddings with the AlloyDBVectorStore class

The [AlloyDB Omni notebook](https://github.com/googleapis/llama-index-alloydb-pg-python/blob/main/samples/llama_index_vector_store.ipynb) for vector store shows you how to do the following:

  * Create an `AlloyDBEngine` to connect to your AlloyDB Omni instance using `AlloyDBEngine.from_connection_string()`.
  * Initialize a table to store vector embeddings.
  * Create an embedding class instance using any [LlamaIndex embeddings model](https://developers.llamaindex.ai/python/framework/module_guides/models/embeddings/).
  * Initialize a default `AlloyDBVectorStore` vector store.
  * Create and query an index from the vector store by using [VectorStoreIndex](https://developers.llamaindex.ai/python/framework/module_guides/indexing/vector_store_index/).
  * Create a custom Vector Store to store and filter metadata.
  * Add an ANN index to improve search latency.



## Document and Index Stores

LlamaIndex Document Stores integration manages structured document storage and retrieval, optimizing for LlamaIndex document-centric capabilities. Document Store stores the content related to the vectors in the vector store.

For more information, see the [LlamaIndex Document Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/docstores/) product documentation.

Index Stores facilitate the management of indexes to enable rapid querying and data retrieval, for example, summary, keyword, and Tree index. `Index` in LlamaIndex is a lightweight storage only for the node metadata. Updates to node metadata don't require re-indexing (read embedding generation) of the full node or all nodes in a document.

For more information, see [LlamaIndex Index Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/index_stores/).

### Store documents and indexes

The [AlloyDB Omni notebook](https://github.com/googleapis/llama-index-alloydb-pg-python/blob/main/samples/llama_index_doc_store.ipynb) for Document Stores shows you how to use AlloyDB Omni to store documents and indexes using the `AlloyDBDocumentStore` and `AlloyDBIndexStore` classes. You learn how to do the following:

  * Create an `AlloyDBEngine` to connect to your AlloyDB Omni instance using `AlloyDBEngine.from_connection_string()`.
  * Create tables for the DocumentStore and IndexStore.
  * Initialize a default `AlloyDBDocumentStore`.
  * Set up an `AlloyDBIndexStore`.
  * Add documents to the `Docstore`.
  * Use Document Stores with multiple indexes.
  * Load existing indexes.



## Chat Stores

Chat Stores maintain conversation history and context for chat-based applications, enabling personalized interactions. Chat Stores provide a central repository that stores and retrieves chat messages within a conversation, allowing the LLM to maintain context and provide more relevant responses based on the ongoing dialog.

Large language models are stateless by default, which means that they don't retain previous inputs unless those inputs are explicitly provided each time. By using a chat store, you can preserve the context of the conversation, which lets the model generate more relevant and coherent responses over time.

The memory module in LlamaIndex enables efficient storage and retrieval of conversational context, allowing for more personalized and context-aware interactions in chat applications. You can integrate the memory module in LlamaIndex with a [ChatStore](https://developers.llamaindex.ai/python/framework/module_guides/storing/chat_stores/) and a [ChatMemoryBuffer](https://developers.llamaindex.ai/python/framework-api-reference/memory/chat_memory_buffer/). For more information, see [LlamaIndex Chat Stores](https://developers.llamaindex.ai/python/framework/module_guides/storing/chat_stores/).

### Store chat history

The [AlloyDB Omni notebook](https://github.com/googleapis/llama-index-alloydb-pg-python/blob/main/samples/llama_index_chat_store.ipynb) for Chat Stores shows you how to use AlloyDB Omni to store chat history using the `AlloyDBChatStore` class. You learn how to do the following:

  * Create an `AlloyDBEngine` to connect to your AlloyDB Omni instance using `AlloyDBEngine.from_connection_string()`.
  * Initialize a default `AlloyDBChatStore`.
  * Create a `ChatMemoryBuffer`.
  * Create an LLM class instance.
  * Use the `AlloyDBChatStore` without a storage context.
  * Use the `AlloyDBChatStore` with a storage context.
  * Create and use the Chat Engine.



## Document Reader

Document Reader efficiently retrieves and transforms data from AlloyDB Omni into LlamaIndex-compatible formats for indexing. The Document Reader interface provides methods to load data from a source as `Documents`.

[Document](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/) is a class that stores a piece of text and associated metadata. You can use Document Readers to load documents that you want to store in Document Stores or used to create Indexes.

### Retrieve data as documents

The [AlloyDB Omni notebook](https://github.com/googleapis/llama-index-alloydb-pg-python/blob/main/samples/llama_index_reader.ipynb) for Document Reader shows you how to use AlloyDB Omni to retrieve data as documents using the `AlloyDBReader` class. You learn how to do the following:

  * Create an `AlloyDBEngine` to connect to your AlloyDB Omni instance using `AlloyDBEngine.from_connection_string()`.
  * Create `AlloyDBReader`.
  * Load Documents using the `table_name` argument.
  * Load Documents using a SQL query.
  * Set page content format.
  * Load the documents.



## What's next

\- Learn how to [Install AlloyDB Omni](/alloydb/omni/containers/current/docs/deploy-vm). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
