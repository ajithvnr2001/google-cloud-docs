---
url: https://docs.cloud.google.com/alloydb/docs/ai/langchain/
title: Build LLM-powered applications using LangChain \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:30:34.712481+00:00
---

# Build LLM-powered applications using LangChain  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/langchain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Build LLM-powered applications using LangChain Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — LangChain**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The LangChain integration for AlloyDB for PostgreSQL lets you build large language model (LLM) and retrieval-augmented generation (RAG) applications backed by your database. You can use the [LangChain](https://www.langchain.com/) classes for AlloyDB to perform semantic search with a vector store, load and save documents, and persist chat message history. Each component overview links to a step-by-step procedure guide in GitHub.

## What is LangChain?

LangChain is an LLM orchestration framework that helps developers build generative AI applications or retrieval-augmented generation (RAG) workflows. It provides the structure, tools, and components to streamline complex large language model (LLM) workflows. For more information about LLMs, their use cases, and the specific models and services that Google offers, see an [overview of LLM concepts and services in Google Cloud](https://docs.cloud.google.com/ai/llms).

For more information about LangChain, see the [Google LangChain](https://python.langchain.com/docs/integrations/platforms/google) page. For more information about the LangChain framework, see the [ LangChain](https://python.langchain.com/docs/get_started/introduction) product documentation.

## LangChain components for AlloyDB

  * Vector store
  * Document loader
  * Chat message history



Learn how to use LangChain with the [LangChain Quickstart for AlloyDB](https://github.com/googleapis/langchain-google-alloydb-pg-python/blob/main/samples/langchain_quick_start.ipynb). This quickstart creates an application that accesses a Netflix Movie dataset so that users can interact with movie data.

## Vector store for AlloyDB

Vector store retrieves and stores documents and metadata from a vector database. Vector store gives an application the ability to perform semantic searches that interpret the meaning of a user query. This type of search is a called a vector search, and it can find topics that match the query conceptually. At query time, vector store retrieves the embedding vectors that are most similar to the embedding of the search request. In LangChain, a vector store takes care of storing embedded data and performing the vector search for you.

To work with vector store in AlloyDB, use the `AlloyDBVectorStore` class.

For more information, see the [LangChain vector stores](https://python.langchain.com/docs/how_to/#vector-stores) product documentation.

### Vector store procedure guide

The [AlloyDB guide for vector store](https://github.com/googleapis/langchain-google-alloydb-pg-python/blob/main/docs/vector_store.ipynb) shows you how to do the following:

  * Install the integration package and LangChain
  * Create an `AlloyDBEngine` object and configure a connection pool to your AlloyDB database
  * Initialize a table for the vector store
  * Set up an embedding service using `VertexAIEmbeddings`
  * Initialize `AlloyDBVectorStore`
  * Add and delete documents
  * Search for similar Documents
  * Add a vector index to improve search performance
  * Create a custom vector store to connect to a pre-existing AlloyDB for PostgreSQL database that has a table with vector embeddings



## Document loader for AlloyDB

The document loader saves, loads, and deletes a LangChain `Document` objects. For example, you can load data for processing into embeddings and either store it in vector store or use it as a tool to provide specific context to chains.

To load documents from AlloyDB, use the `AlloyDBLoader` class. `AlloyDBLoader` returns a list of documents from a table using the first column for page content and all other columns for metadata. The default table has the first column as page content and the second column as JSON metadata. Each row becomes a document. Instructions for customizing these settings are in the procedure guide.

Use the `AlloyDBSaver` class to save and delete documents.

For more information, see the [LangChain Document loaders](https://python.langchain.com/docs/how_to/#document-loaders) topic.

### Document loader procedure guide

The [AlloyDB guide for document loader](https://github.com/googleapis/langchain-google-alloydb-pg-python/blob/main/docs/document_loader.ipynb) shows you how to do the following:

  * Install the integration package and LangChain
  * Load documents from a table
  * Add a filter to the loader
  * Customize the connection and authentication
  * Customize Document construction by specifying customer content and metadata
  * How to use and customize a `AlloyDBSaver` to store and delete documents



## Chat message history for AlloyDB

Question and answer applications require a history of the things said in the conversation to give the application context for answering further questions from the user. The LangChain `ChatMessageHistory` class lets the application save messages to a database and retrieve them when needed to formulate further answers. A message can be a question, an answer, a statement, a greeting or any other piece of text that the user or application gives during the conversation. `ChatMessageHistory` stores each message and chains messages together for each conversation.

AlloyDB extends this class with `AlloyDBChatMessageHistory`.

### Chat message history procedure guide

The [AlloyDB guide for chat message history](https://github.com/googleapis/langchain-google-alloydb-pg-python/blob/main/docs/chat_message_history.ipynb) shows you how to do the following:

  * Install the integration package and LangChain
  * Create an `AlloyDBEngine` object and configure a connection pool to your AlloyDB database
  * Initialize a table
  * Initialize the `AlloyDBChatMessageHistory` class to add and delete messages
  * Create a chain for message history using the LangChain Expression Language (LCEL)



## What's next

  * [Migrate data from a vector database to AlloyDB using LangChain](https://docs.cloud.google.com/alloydb/docs/ai/migrate-data-from-langchain-vector-stores-to-alloydb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
