---
url: https://docs.cloud.google.com/sql/docs/postgres/langchain/
title: Build LLM-powered applications using LangChain \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:53.362990+00:00
---

# Build LLM-powered applications using LangChain  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/langchain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Build LLM-powered applications using LangChain Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/langchain "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/langchain "View this page for the SQL Server database engine")

**Preview — LangChain**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page introduces how to build LLM-powered applications using [LangChain](https://www.langchain.com/). The overviews on this page link to procedure guides in GitHub.

## What is LangChain?

LangChain is an LLM orchestration framework that helps developers build generative AI applications or retrieval-augmented generation (RAG) workflows. It provides the structure, tools, and components to streamline complex LLM workflows.

For more information about LangChain, see the [Google LangChain](https://python.langchain.com/docs/integrations/platforms/google) page. For more information about the LangChain framework, see the [ LangChain](https://python.langchain.com/docs/get_started/introduction) product documentation.

## LangChain components for Cloud SQL for PostgreSQL

Cloud SQL for PostgreSQL offers the following LangChain interfaces:

  * Vector store
  * Document loader
  * Chat message history



Learn how to use LangChain with the [LangChain Quickstart for Cloud SQL for PostgreSQL](https://github.com/googleapis/langchain-google-cloud-sql-pg-python/blob/main/samples/langchain_quick_start.ipynb).

## Vector store for Cloud SQL for PostgreSQL

Vector store retrieves and stores documents and metadata from a vector database. Vector store gives an application the ability to perform semantic searches that interpret the meaning of a user query. This type of search is a called a vector search, and it can find topics that match the query conceptually. At query time, vector store retrieves the embedding vectors that are most similar to the embedding of the search request. In LangChain, a vector store takes care of storing embedded data and performing the vector search for you.

To work with vector store in Cloud SQL for PostgreSQL, use the `PostgresVectorStore` class.

For more information, see the [LangChain Vector Stores](https://python.langchain.com/docs/modules/data_connection/vectorstores/) product documentation.

### Vector store procedure guide

The [Cloud SQL for PostgreSQL guide for vector store](https://github.com/googleapis/langchain-google-cloud-sql-pg-python/blob/main/docs/vector_store.ipynb) shows you how to do the following:

  * Install the integration package and LangChain
  * Create a `PostgresEngine` object and configure a connection pool to your Cloud SQL for PostgreSQL database
  * Initialize a table
  * Create an embedding object using `VertexAIEmbeddings`
  * Initialize a default `PostgresVectorStore`
  * Add texts
  * Delete texts
  * Search for documents
  * Search for documents by vector
  * Add an index to accelerate vector search queries
  * Re-index
  * Remove an index
  * Create a custom vector store
  * Search for documents with a metadata filter



## Document loader for Cloud SQL for PostgreSQL

The document loader saves, loads, and deletes a LangChain `Document` objects. For example, you can load data for processing into embeddings and either store it in vector store or use it as a tool to provide specific context to chains.

To load documents from document loader in Cloud SQL for PostgreSQL, use the `PostgresLoader` class. `PostgresLoader` returns a list of documents from a table using the first column for page content and all other columns for metadata. The default table has the first column as page content and the second column as JSON metadata. Each row becomes a document. Use the `PostgresDocumentSaver` class to save and delete documents.

For more information, see the [LangChain Document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/) topic.

### Document loader procedure guide

The [Cloud SQL for PostgreSQL guide for document loader](https://github.com/googleapis/langchain-google-cloud-sql-pg-python/blob/main/docs/document_loader.ipynb) shows you how to do the following:

  * Install the integration package and LangChain
  * Load documents from a table
  * Add a filter to the loader
  * Customize the connection and authentication
  * Customize Document construction by specifying customer content and metadata
  * How to use and customize a `PostgresDocumentSaver` to store and delete documents



## Chat message history for Cloud SQL for PostgreSQL

Question and answer applications require a history of the things said in the conversation to give the application context for answering further questions from the user. The LangChain `ChatMessageHistory` class lets the application save messages to a database and retrieve them when needed to formulate further answers. A message can be a question, an answer, a statement, a greeting or any other piece of text that the user or application gives during the conversation. `ChatMessageHistory` stores each message and chains messages together for each conversation.

Cloud SQL for PostgreSQL extends this class with `PostgresChatMessageHistory`.

### Chat message history procedure guide

The [Cloud SQL for PostgreSQL guide for chat message history](https://github.com/googleapis/langchain-google-cloud-sql-pg-python/blob/main/docs/chat_message_history.ipynb) shows you how to do the following:

  * Install LangChain and authenticate to Google Cloud
  * Create a `PostgresEngine` object and configure a connection pool to your Cloud SQL for PostgreSQL database
  * Initialize a table
  * Initialize the `PostgresChatMessageHistory` class to add and delete messages
  * Create a chain for message history using the LangChain Expression Language (LCEL) and Google's Vertex AI chat models



## What's next

  * [Build generative AI applications using Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/ai-overview)

  * [Integrate Cloud SQL with Vertex AI](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai)

  * [Work with vector embeddings](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors)

  * [Invoke online predictions from Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/invoke-online-predictions)

  * [Understand an example of an embedding workflow](https://docs.cloud.google.com/sql/docs/postgres/understand-example-embedding-workflow)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
