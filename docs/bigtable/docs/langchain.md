---
url: https://docs.cloud.google.com/bigtable/docs/langchain/
title: Build LLM-powered applications using LangChain \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:36.151741+00:00
---

# Build LLM-powered applications using LangChain  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/langchain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build LLM-powered applications using LangChain

**Preview — LangChain**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Connecting [LangChain](https://www.langchain.com/) to Bigtable lets you build and scale LLM-powered generative AI applications and retrieval-augmented generation (RAG) workflows. The component overviews in this document link to implementation procedures in GitHub.

## What is LangChain?

LangChain is an LLM orchestration framework that helps developers build generative AI applications or retrieval-augmented generation (RAG) workflows. It provides the structure, tools, and components to streamline complex LLM workflows.

For more information about LangChain, see the [Google LangChain](https://python.langchain.com/docs/integrations/platforms/google) page. For more information about the LangChain framework, see the [ LangChain](https://python.langchain.com/docs/get_started/introduction) product documentation.

## LangChain components for Bigtable

Bigtable offers the following LangChain interfaces:

  * Vectore store
  * Key-value store
  * Document loader
  * Chat message history



Learn how to use LangChain with the [LangChain Quickstart for Bigtable](https://github.com/googleapis/langchain-google-bigtable-python). This quickstart creates an application that accesses a Netflix Movie dataset so that users can interact with movie data.

## Vector store for Bigtable

You can use the vector store to save text documents along with their vector embeddings and other metadata in a Bigtable table. This lets you:

  * Search your documents with techniques such as the vector similarity search or the maximal marginal relevance (MMR) search.
  * Perform extra filtering on the vector search results with the documents' metadata.



For more information, see the [LangChain vector stores](https://python.langchain.com/docs/how_to/#vector-stores) topic.

### Vector store procedure guide

The [Bigtable guide for vector stores](https://github.com/googleapis/langchain-google-bigtable-python/blob/main/docs/vector_store.ipynb) shows you how to do the following:

  * Install the integration package and LangChain
  * Set up the embedding service
  * Create and configure the Bigtable store
  * Customize the connection and authentication
  * Query the store with the kNN algorithm and filter the results by document metadata



## Key-value store for Bigtable

Bigtable provides a key-value store for LangChain in the form of a `ByteStore` class that lets you work with documents or embeddings stored as byte objects. This approach can help you significantly reduce costs and latency when performing tasks such as caching and indexing embeddings for repeated queries.

For more information, see the [LangChain key-value stores](https://python.langchain.com/docs/concepts/key_value_stores/#overview) topic.

### Key-value store procedure guide

The [Bigtable guide for key-value stores](https://github.com/googleapis/langchain-google-bigtable-python/blob/main/docs/key_value_store.ipynb) shows you how to do the following:

  * Install the integration package and LangChain
  * Initialize the required engine and tables
  * Customize the connection and authentication
  * How to use `BigtableByteStore` as a caching layer for vector embeddings



## Document loader for Bigtable

The document loader saves, loads, and deletes a LangChain `Document` objects. For example, you can load data for processing into embeddings and either store it in vector store or use it as a tool to provide specific context to chains.

To load documents from document loader in Bigtable, use the `BigtableLoader` class. `BigtableLoader` methods return one or more documents from a table. Use the `BigtableSaver` class to save and delete documents.

For more information, see the [LangChain Document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/) topic.

### Document loader procedure guide

The [Bigtable guide for document loader](https://github.com/googleapis/langchain-google-bigtable-python/blob/main/docs/document_loader.ipynb) shows you how to do the following:

  * Install the integration package and LangChain
  * Load documents from a table
  * Add a filter to the loader
  * Customize the connection and authentication
  * Customize Document construction by specifying customer content and metadata
  * How to use and customize a `BigtableSaver` to store and delete documents



## Chat message history for Bigtable

Question and answer applications require a history of the things said in the conversation to give the application context for answering further questions from the user. The LangChain `ChatMessageHistory` class lets the application save messages and retrieve them when needed to formulate further answers. A message can be a question, an answer, a statement, a greeting or any other piece of text that the user or application gives during the conversation. `ChatMessageHistory` stores each message and chains messages together for each conversation.

Bigtable extends this class with `BigtableChatMessageHistory`.

### Chat message history procedure guide

The [Bigtable guide for chat message history](https://github.com/googleapis/langchain-google-bigtable-python/blob/main/docs/chat_message_history.ipynb) shows you how to do the following:

  * Install LangChain and authenticate to Google Cloud
  * Initialize Bigtable schema
  * Initialize the `BigtableChatMessageHistory` class to add and delete messages
  * Use a client to customize the connection and authentication



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
