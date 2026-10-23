---
url: https://docs.cloud.google.com/sql/docs/sqlserver/langchain/
title: Build LLM-powered applications using LangChain \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:18.879524+00:00
---

# Build LLM-powered applications using LangChain  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/langchain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Build LLM-powered applications using LangChain Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/langchain "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/langchain "View this page for the PostgreSQL database engine") | SQL Server

**Preview — LangChain**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page introduces how to build LLM-powered applications using [LangChain](https://www.langchain.com/). The overviews on this page link to procedure guides in GitHub.

## What is LangChain?

LangChain is an LLM orchestration framework that helps developers build generative AI applications or retrieval-augmented generation (RAG) workflows. It provides the structure, tools, and components to streamline complex LLM workflows.

For more information about LangChain, see the [Google LangChain](https://python.langchain.com/docs/integrations/platforms/google) page. For more information about the LangChain framework, see the [ LangChain](https://python.langchain.com/docs/get_started/introduction) product documentation.

## LangChain components for Cloud SQL for SQL Server

Cloud SQL for SQL Server offers the following LangChain interfaces:

  * Document loader
  * Chat message history



Learn how to use LangChain with the [LangChain Quickstart for Cloud SQL for SQL Server](https://github.com/googleapis/langchain-google-cloud-sql-mssql-python).

## Document loader for Cloud SQL for SQL Server

The document loader saves, loads, and deletes a LangChain `Document` objects. For example, you can load data for processing into embeddings and either store it in vector store or use it as a tool to provide specific context to chains.

To load documents from document loader in Cloud SQL for SQL Server, use the `MSSQLLoader` class. `MSSQLLoader` methods return one or more documents from a table. Use the `MSSQLDocumentSaver` class to save and delete documents.

For more information, see the [LangChain Document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/) topic.

### Document loader procedure guide

The [Cloud SQL for SQL Server guide for document loader](https://github.com/googleapis/langchain-google-cloud-sql-mssql-python/blob/main/docs/document_loader.ipynb) shows you how to do the following:

  * Install the integration package and LangChain
  * Load documents from a table
  * Add a filter to the loader
  * Customize the connection and authentication
  * Customize Document construction by specifying customer content and metadata
  * How to use and customize a `MSSQLDocumentSaver` to store and delete documents



## Chat message history for Cloud SQL for SQL Server

Question and answer applications require a history of the things said in the conversation to give the application context for answering further questions from the user. The LangChain `ChatMessageHistory` class lets the application save messages to a database and retrieve them when needed to formulate further answers. A message can be a question, an answer, a statement, a greeting or any other piece of text that the user or application gives during the conversation. `ChatMessageHistory` stores each message and chains messages together for each conversation.

Cloud SQL for SQL Server extends this class with `MSSQLChatMessageHistory`.

### Chat message history procedure guide

The [Cloud SQL for SQL Server guide for chat message history](https://github.com/googleapis/langchain-google-cloud-sql-mssql-python/blob/main/docs/chat_message_history.ipynb) shows you how to do the following:

  * Install LangChain and authenticate to Google Cloud
  * Create a `MSSQLEngine` object and configure a connection pool to your Cloud SQL for SQL Server database
  * Initialize a table
  * Initialize the `MSSQLChatMessageHistory` class to add and delete messages
  * Create a chain for message history using the LangChain Expression Language (LCEL) and Google's Vertex AI chat models



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
