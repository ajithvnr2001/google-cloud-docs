---
url: https://docs.cloud.google.com/memorystore/docs/valkey/langchain/
title: Build LLM-powered applications using LangChain \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:53.115324+00:00
---

# Build LLM-powered applications using LangChain  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/langchain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Build LLM-powered applications using LangChain Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces how to build large language model (LLM)-powered applications using [LangChain](https://www.langchain.com/). The overviews on this page link to procedure guides in GitHub.

## What's LangChain?

LangChain is an LLM orchestration framework that helps developers build generative AI applications or retrieval-augmented generation (RAG) workflows. It provides the structure, tools, and components to streamline complex LLM workflows.

For more information about LangChain, see the [Google LangChain](https://python.langchain.com/docs/integrations/platforms/google) page. For more information about the LangChain framework, see the [ LangChain](https://python.langchain.com/docs/get_started/introduction) product documentation.

## LangChain components for Memorystore for Valkey

Memorystore for Valkey offers the following LangChain interfaces:

  * Vector store
  * Document loader
  * Chat message history



Learn how to use LangChain with the [LangChain Quickstart](https://github.com/googleapis/langchain-google-memorystore-redis-python).

## Vector store for Memorystore for Valkey

Vector store retrieves and stores documents and metadata from a vector database. Vector store gives an application the ability to perform semantic searches that interpret the meaning of a user query. This type of search is a called a vector search, and it can find topics that match the query conceptually. At query time, Vector store retrieves the embedding vectors that are most similar to the embedding of the search request. In LangChain, a vector store takes care of storing embedded data and performing the vector search for you.

To work with vector store in Memorystore for Valkey, use the `RedisVectorStore` class.

For more information, see the [LangChain](https://python.langchain.com/docs/modules/data_connection/vectorstores/) product documentation.

### Vector store procedure guide

The [guide for Vector store](https://github.com/googleapis/langchain-google-memorystore-redis-python/blob/main/docs/vector_store.ipynb) shows you how to do the following:

  * Install the integration package and LangChain.
  * Initialize a vector index.
  * Prepare documents for Vector store.
  * Add documents to Vector store.
  * Perform a similarity search (KNN).
  * Perform a range-based similarity search.
  * Perform a Maximal Marginal Relevance (MMR) search.
  * Use Vector store as a Retriever.
  * Delete documents from Vector store.
  * Delete a vector index.



## Document loader for Memorystore for Valkey

The document loader saves, loads, and deletes LangChain `Document` objects. For example, you can load data for processing into embeddings and either store it in Vector store or use it as a tool to provide specific context to chains.

To load documents from the document loader in Memorystore for Valkey, use the `MemorystoreDocumentLoader` class. To save and delete documents, use the `MemorystoreDocumentSaver` class.

For more information, see [Document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/).

### Document loader procedure guide

The [guide for document loader](https://github.com/googleapis/langchain-google-memorystore-redis-python/blob/main/docs/document_loader.ipynb) shows you how to do the following:

  * Install the integration package and LangChain.
  * Load documents from a table.
  * Add a filter to the document loader.
  * Customize the connection and authentication.
  * Customize document construction by specifying customer content and metadata.
  * Use and customize the `MemorystoreDocumentSaver` class to store and delete documents.



## Chat message history for Memorystore for Valkey

Question-and-answer applications require a history of the things said in the conversation to give the application context for answering further questions from the user. The LangChain `ChatMessageHistory` class lets the application save messages to a database and retrieve them when needed to formulate further answers. A message can be a question, an answer, a statement, a greeting, or any other piece of text that the user or application gives during the conversation. `ChatMessageHistory` stores each message and chains messages together for each conversation.

Memorystore for Valkey extends this class with `MemorystoreChatMessageHistory`.

### Chat message history procedure guide

The [guide for chat message history](https://github.com/googleapis/langchain-google-memorystore-redis-python/blob/main/docs/chat_message_history.ipynb) shows you how to:

  * Install LangChain and authenticate to Google Cloud.
  * Initialize the `MemorystoreChatMessageHistory` class to add and delete messages.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
