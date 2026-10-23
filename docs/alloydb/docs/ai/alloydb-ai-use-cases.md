---
url: https://docs.cloud.google.com/alloydb/docs/ai/alloydb-ai-use-cases/
title: Build generative AI applications \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:31.103567+00:00
---

# Build generative AI applications  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/alloydb-ai-use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Build generative AI applications Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB for PostgreSQL supports a wide range of generative AI use cases, including semantic search, retrieval-augmented generation (RAG), and AI-powered agents. You can explore the following codelabs, notebooks, and tutorials to evaluate architectural approaches and accelerate your application development.

Use case | Description  
---|---  
Accelerate patent searches and search precision | These codelabs show you how to improve patent research by using vector search along with AlloyDB, the [pgvector extension](https://docs.cloud.google.com/alloydb/docs/ai/work-with-embeddings), embeddings, Gemini, and Java Agent Development Kit (ADK). 

  * Codelab:[Build a patent search app using AlloyDB, vector search, and Gemini Enterprise Agent Platform (formerly Vertex AI)](https://codelabs.developers.google.com/patent-search-alloydb-gemini)
  * Codelab:[ Build a Patent Search App with AlloyDB, vector search, and Java Agent Development Kit](https://codelabs.developers.google.com/patent-search-java-adk)

  
Generate multimodal Embeddings in AlloyDB | This codelab demonstrates how to use the capabilities of AlloyDB AI for semantic search using multimodal embeddings.   
  
Learn about how to perform different types of searches, including text-based semantic search, image search by image, and image search by text, as well as a hybrid approach that combines different search types. 

  * Codelab:[ Multimodal Embeddings in AlloyDB](https://codelabs.developers.google.com/alloydb-ai-mm-embeddings#0)

  
Generate SQL using AlloyDB AI natural language | This codelab provides a step-by-step guide on how to use the AlloyDB AI natural language feature to generate SQL queries.   
  
The codelab uses a fictional ecommerce dataset to demonstrate how you can ask questions in natural language (English) and have AlloyDB AI translate them into SQL. 

  * Codelab:[ Generate SQL using AlloyDB AI natural language ](https://codelabs.developers.google.com/alloydb-ai-nl-sql#0)

  
Apply semantic filters and rerank vector search results to improve search quality | This codelab shows you how to use AlloyDB AI features like AI[ Query Operators, model endpoint management](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators), and[ vector search](https://docs.cloud.google.com/alloydb/docs/ai/perform-vector-search) to help you improve your search quality and use semantic filters.  
  
Learn how to use AI Query operators for semantic filtering to unlock new experiences in SQL. Rank vector search results using LLMs and [ semantic ranking models](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking#models) to improve the accuracy of your vector search. This tutorial uses a Agent Platform semantic ranking model in AlloyDB and [Agent Platform generative AI models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * Codelab:[ AlloyDB AI Operators and Reranking](https://codelabs.developers.google.com/alloydb-ai-operators)

  
Build an AI-powered outfit recommendation app with AlloyDB and serverless runtimes | The following codelab shows you how to build an AI-powered outfit recommendation app with AlloyDB AI and serverless runtimes. It explains how users can upload a picture of clothing and receive AI-driven style recommendations and visualizations.  
  
The codelab uses Google Cloud technologies like AlloyDB AI, Gemini 2.0, and Imagen 3 to create a web application deployed in Cloud Run serverless runtime. 

  * Codelab: [Build an AI-powered outfit recommendation app with AlloyDB and serverless runtimes](https://codelabs.developers.google.com/smart-stylist-app#0)

  
Build an application that invokes a database query from your agent or a generative AI application | The following codelab shows you how to build an application that uses Gen AI Toolbox for Databases to perform a simple AlloyDB query that you can invoke from your agent or from a generative AI application.  


  * Codelab: [Installing and Setting-up Toolbox for your Generative AI & Agentic Applications on AlloyDB](https://codelabs.developers.google.com/genai-toolbox-for-alloydb#0)

  
Build and deploy a personalized fashion styling assistant | The following codelabs show you how to build and deploy a personalized style assistant with Gemini, model endpoint management, vector search, Agent Platform, and agents.  


  * Codelab: [Part 1: Build a Smart Shopping Assistant with AlloyDB and AI Applications](https://codelabs.developers.google.com/smart-shop-agent-alloydb#0)
  * Codelab: [Part 2: Deploy a Smart Shopping Assistant with AlloyDB and AI Applications](https://codelabs.developers.google.com/smart-shop-agent-vertexai#0)

  
Build an LLM and RAG-based chat application using AlloyDB AI and LangChain  | This codelab guides you through deploying the GenAI Databases Retrieval Service and then shows you how to build a sample interactive application using your newly set up environment.  


  * Codelab: [Building an LLM and RAG-based chat application using AlloyDB AI and LangChain](https://codelabs.developers.google.com/codelabs/genai-db-retrieval-app)

  
Create a chatbot to answer questions about movies | This tutorial shows you how to build a generative AI chatbot that uses [Gemini](https://docs.cloud.google.com/gemini/docs/overview), [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview), and the AlloyDB LangChain integration. You learn how to extract structured data from your database , generate embeddings, and format your data so that you can perform vector search in a [Retrieval-Augmented Generation (RAG)](https://cloud.google.com/use-cases/retrieval-augmented-generation) application.  
  
Use a movie database to ground your LLM with information about the most popular films. Grounding helps to ensure that LLM output is accurate and relevant. 

  * Tutorial: [AlloyDB LangChain integration](https://github.com/googleapis/langchain-google-alloydb-pg-python/blob/main/samples/langchain_quick_start.ipynb)

  
Create a toy store search app | The following codelab shows you how to create a personalized and seamless toy store search experience using contextual search and custom generation of the product matching the search context.  
  
You use pgvector and generative AI model extensions in AlloyDB, a real-time Cosine similarity search, Gemini 2.0 Flash, and [Gen AI Toolbox for Databases](https://cloud.google.com/blog/products/ai-machine-learning/announcing-gen-ai-toolbox-for-databases-get-started-today?e=48754805). 

  * Codelab: [Toy Store Search App with Cloud Databases, Serverless Runtimes and Open Source Integrations](https://codelabs.developers.google.com/toy-store-app#0)

  
Deploy AlloyDB Omni and a local AI model on Kubernetes | In this codelab you learn how to deploy AlloyDB Omni on Google Kubernetes Engine (GKE) and use it with an open embedding model deployed in the same Kubernetes cluster.  


  * Codelab: [Deploy AlloyDB Omni and local AI model on Kubernetes](https://codelabs.developers.google.com/alloydb-omni-gke-embeddings)

  
Deploy a RAG application with LangChain on Agent Platform | This tutorial shows you how to build and deploy an agent using the Agent Platform SDK for Python and the AlloyDB LangChain integration.  
  
Learn how to use agents and vectors with [LangChain](https://python.langchain.com/docs/get_started/introduction) to perform a similarity search and retrieve related data to ground LLM responses. 

  * Tutorial: [Deploying a RAG Application with AlloyDB to Agent Engine](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/tutorial_alloydb_rag_agent.ipynb)

  
Integrate hybrid search and AI functions into your search application | This demo illustrates the AI capabilities of Google Cloud AlloyDB, integrating hybrid search including SQL, vector, and full-text search with AI functions, all applied to a sample ecommerce dataset from Cymbal Shops.  


  * Demo: [Cymbal Shops StyleSearch AlloyDB AI Demo](https://github.com/paulramsey/stylesearch-alloydb-ai-demo)

  
Migrate data from a vector database to AlloyDB  | The following tutorial describes how to migrate data from a third-party vector database to AlloyDB leveraging LangChain vector stores.  
  
The following vector databases are supported: Pinecone, Weaviate, Chroma, Qdrant, and Milvus. 

  * Tutorial: [Migrate data from a vector database to AlloyDB](https://docs.cloud.google.com/alloydb/docs/ai/migrate-data-from-langchain-vector-stores-to-alloydb)

  
Perform a multimodal hybrid product search | This notebook shows you how to perform a hybrid search in AlloyDB for Cymbal Shops, a fictional retailer with a large eCommerce presence. The notebook combines multimodal vector embeddings, full text search (Generalized Inverted Index), and BM25 sparse embeddings (pgvector 0.7.0+) with Reciprocal Rank Fusion re-ranking for enhanced product search.  


  * Notebook: [Multimodal Hybrid Product Search on AlloyDB - With Data Prep](https://github.com/paulramsey/stylesearch-alloydb-ai-demo/blob/main/cymbal_shops_hybrid_search_alloydb_data_prep.ipynb)

  
Use a similarity search using a vector index to find relevant products  | This codelab shows you how to use AlloyDB AI features like [model endpoint management ](https://docs.cloud.google.com/alloydb/docs/ai/model-endpoint-overview)and [vector search](https://docs.cloud.google.com/alloydb/docs/ai/perform-vector-search) to help you find relevant products.  
  
Learn how to generate embeddings using model endpoint management on your database data and use your operational data to perform vector similarity searches. This tutorial uses a Agent Platform embedding model in AlloyDB and [Agent Platform generative AI models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview). 

  * Codelab: [Getting started with Vector Embeddings with AlloyDB AI](https://codelabs.developers.google.com/alloydb-ai-embedding)

  
Use MCP Toolbox for Databases with AlloyDB AI to create conversational product searches  | Learn how to use the MCP Toolbox for Databases, AlloyDB AI, and vector search to create a Shopping AI Agent designed to transform your retail experience. This tutorial demonstrates the agent's capabilities, from conversational product searches to placing orders.  


  * Codelab: [Build a Sports Shop Agent AI Assistant with ADK, MCP Toolbox and AlloyDB](https://codelabs.developers.google.com/codelabs/sports-agent-adk-mcp-alloydb)

  
  
## What's next

  * [Create indexes](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index).
  * [Register and call remote AI models using model endpoint management](https://docs.cloud.google.com/alloydb/docs/ai/register-model-endpoint).
  * Learn about [ScaNN vector query performance](https://docs.cloud.google.com/alloydb/docs/ai/scann-vector-query-perf-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
