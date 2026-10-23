---
url: https://docs.cloud.google.com/alloydb/docs/ai/what-is-alloydb-ai/
title: What is AlloyDB AI \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:34.114624+00:00
---

# What is AlloyDB AI  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/what-is-alloydb-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  What is AlloyDB AI Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB AI brings generative AI directly to your operational data in AlloyDB for PostgreSQL and AlloyDB Omni. By integrating AI model inference, PostgreSQL vector search, hybrid search, and AI agent interfaces directly into the database engine, AlloyDB AI lets your database process and query data by using AI models. You can build low-latency, production-grade AI applications without the complexity, latency, and cost of managing separate transactional, full-text, and vector engines. 

[ Learn more about AlloyDB AI](https://docs.cloud.google.com/alloydb/docs/ai)

![AlloyDB AI search overview](https://docs.cloud.google.com/static/alloydb/images/ai-powered-search.png)

###  [ AI search → ](https://docs.cloud.google.com/alloydb/docs/ai/vector-search-landing)

Combine PostgreSQL vector search, keyword search, and reranking. Get 10x faster ScaNN search with Adaptive Filtering, and 4x faster HNSW with the AlloyDB columnar engine. 

![AlloyDB AI functions overview](https://docs.cloud.google.com/static/alloydb/images/inference.png)

###  [ AI functions → ](https://docs.cloud.google.com/alloydb/docs/ai/ai-query-engine-landing)

Run in-database model inference and embedding generation directly in SQL. Use smart batching, local proxy models, and TimesFM forecasting to accelerate and scale AI features. 

![Agent development and interfaces](https://docs.cloud.google.com/static/alloydb/images/natural-language.png)

###  [ AI tooling → ](https://docs.cloud.google.com/alloydb/docs/ai/use-alloydb-mcp)

Ground AI agents in real-time records. Build with MCP, manage memory, and use LangChain or LlamaIndex. Enable conversational analytics and natural language queries using the QueryData API. 

## Generative AI capabilities in AlloyDB

AlloyDB AI organizes its features into three pillars to make it easier to build AI applications.

### AI search

AlloyDB AI provides a unified search experience by combining high-performance vector search, keyword full-text search (FTS), structured SQL filtering, and reranking within a single database engine. For more information, see [AI search](https://docs.cloud.google.com/alloydb/docs/ai/vector-search-landing).

  * Fast vector search: Perform PostgreSQL-compatible filtered vector search up to 10x faster than standard pgvector using Google's [ScaNN index](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index) and [Adaptive Filtering](https://docs.cloud.google.com/alloydb/docs/ai/activate-adaptive-filtering). Accelerate HNSW queries up to 4x using the built-in [Columnar Engine](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-with-ce) in AlloyDB.
  * Unified [hybrid search](https://docs.cloud.google.com/alloydb/docs/ai/run-hybrid-vector-similarity-search): Process semantic vector similarity and exact keyword searches concurrently using your choice of [full-text search indexes](https://docs.cloud.google.com/alloydb/docs/ai/full-text-search-overview) such as BM25, RUM, GIN and reranking models for reciprocal rank fusion, semantic cross-encoders, and LLM-based reranking.
  * Automated ScaNN indexes: Use [Auto mode](https://docs.cloud.google.com/alloydb/docs/ai/maintain-vector-indexes) to automatically configure and maintain ScaNN indexes for your workload, which eliminates manual tuning.



### AI functions

Run AI models directly within your SQL queries to analyze data, generate text, or predict trends. AlloyDB AI handles the model connections, so you don't need external orchestration tools or complex code. Because everything runs inside the database, you don't have to export your data to external vector engines. For more information, see [AI functions](https://docs.cloud.google.com/alloydb/docs/ai/ai-query-engine-landing).

  * Embedding functions: Generate query embeddings for semantic search at runtime using the [`ai.embedding()`](https://docs.cloud.google.com/alloydb/docs/ai/work-with-embeddings) function, and bulk generate millions of embeddings in minutes using [`ai.initialize_embeddings()`](https://docs.cloud.google.com/alloydb/docs/ai/generate-manage-auto-embeddings-for-tables) and [`ai.refresh_embeddings()`](https://docs.cloud.google.com/alloydb/docs/ai/generate-manage-auto-embeddings-for-tables).
  * Task-specific functions: Run semantic evaluations using [`ai.if()`](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators) and [`ai.rank()`](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators), determine user sentiment using [`analyze_sentiment()`](https://docs.cloud.google.com/alloydb/docs/ai/analyze-sentiment), and summarize text using [`summarize()`](https://docs.cloud.google.com/alloydb/docs/ai/summarize-content).
  * Smart batching: Optimize query performance and lower network latency using [Smart Batching for AI Functions](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-ai-queries) to achieve faster inference than row-at-a-time calls (supports [`ai.if()`](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators) and [`ai.rank()`](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators)).
  * Proxy models: Train high-accuracy, local surrogate models using [Optimized Functions](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions) to run [`ai.if()`](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators) evaluations faster and at a lower cost than remote LLM calls.
  * TimesFM forecasting: Predict future trends directly from your database tables using the built-in time-series forecasting function [`ai.forecast()`](https://docs.cloud.google.com/alloydb/docs/ai/perform-time-series-forecasting).



### Agent development, RAG, and built-in interfaces

AlloyDB AI grounds your AI agents in real-time database records through built-in interfaces. For more information, see [AI tooling](https://docs.cloud.google.com/alloydb/docs/ai/use-alloydb-mcp).

  * Remote MCP server: Connect autonomous AI agents to your database using a fully managed [Model Context Protocol (MCP) server](https://docs.cloud.google.com/alloydb/docs/ai/use-alloydb-mcp) integrated with Identity and Access Management (IAM) authentication, Agent Registry, and Model Armor.
  * Agent memory: Store your agent's conversation history, knowledge context, and state using [hybrid search](https://docs.cloud.google.com/alloydb/docs/ai/run-hybrid-vector-similarity-search) for low-latency retrieval.
  * Open framework ecosystem: Ground your agentic workflows using official AlloyDB integrations for [LangChain](https://docs.cloud.google.com/alloydb/docs/ai/langchain), [LlamaIndex](https://docs.cloud.google.com/alloydb/docs/ai/build-llm-powered-applications-using-llamaindex), and the [MCP Toolbox for Databases](https://docs.cloud.google.com/alloydb/docs/connect-ide-using-mcp-toolbox).
  * [QueryData](https://docs.cloud.google.com/alloydb/docs/ai/querydata): Allow business users and analysts to query database schemas using everyday language. The [QueryData API](https://docs.cloud.google.com/alloydb/docs/ai/querydata) powers conversational analytics. It uses context sets, which include templates, facets, and value search queries, to translate natural language into secure SQL queries.



## Use cases

AlloyDB AI lets you build many types of generative AI applications directly on your database.

![Search and database information retrieval](https://docs.cloud.google.com/static/alloydb/images/search-icon.svg) **Search and information retrieval** |  Retail search: Serve highly relevant product search results to your users with low latency by using the best of keyword lexical matching, semantic search, and intelligent reranking with the hybrid search capabilities in AlloyDB. Clinical trial matching: Accelerate medical research and patient enrollment by matching patients to active clinical trials, blending structured medical metrics with unstructured doctor notes and clinical symptoms. Patent search: Streamline intellectual property research by combining exact patent classification code lookups with abstract conceptual similarity searches, and automatically summarize matched filings for legal teams.  
---|---  
![Generative AI and database agents](https://docs.cloud.google.com/static/alloydb/images/smart-toy-icon.svg) **Generative AI and agents** |  Retrieval-augmented generation (RAG): Automate the embedding generation and indexing of unstructured documents directly within your database to build high-performance RAG knowledge bases. Intelligent customer support: Resolve customer queries using keyword and semantic search. Retrieve troubleshooting steps, and use agent tools to securely access purchase history for personalized support. Conversational BI and natural language to SQL reporting: Empower non-technical business users to run complex database queries using natural language, and dynamically translate plain-English questions into secure SQL queries.  
![Data analytics and database inference](https://docs.cloud.google.com/static/alloydb/images/speed-icon.svg) **Analytics and inference** |  Transaction enrichment and fraud detection: Parse and enrich raw, messy credit card transaction memos into clean, structured merchant and risk data in real time, and execute predictive checks directly in SQL. Manufacturing preventive maintenance: Predict and minimize machinery downtime by forecasting sensor failures directly on time-series telemetry data, and match equipment anomalies with repair tickets and equipment manuals using hybrid search. Automated feedback and sentiment analysis: Process and analyze raw customer reviews, survey answers, or call logs directly inside your SQL database using built-in AI functions to extract sentiment and generate summaries without external ETL pipelines.  
  
## Customer stories

Learn how customers use AlloyDB AI to build generative AI applications.

![ID.me databases illustration representing customer story](https://docs.cloud.google.com/static/alloydb/images/id-me.jpg)

###  [ ID.me scales and fights AI fraud ](https://cloud.google.com/blog/products/databases/id-me-scales-and-fights-ai-fraud-with-alloydb)

Learn how ID.me uses AlloyDB AI and Gemini Enterprise Agent Platform to scale digital identity for 160M members and detect AI-driven fraud in real-time. 

![Nuro story thumbnail](https://docs.cloud.google.com/static/alloydb/images/nuro.jpg)

###  [ Nuro drives autonomous innovation with AlloyDB AI ](https://cloud.google.com/blog/products/databases/nuro-drives-autonomous-innovation-with-alloydb-for-postgresql)

Learn how AlloyDB AI enables Nuro to perform complex similarity searches on vector embeddings, supporting continuous improvement. 

![Target customer story thumbnail](https://docs.cloud.google.com/static/alloydb/images/target-customer-story.jpg)

###  [ Inside Target's search bar overhaul ](https://cloud.google.com/blog/topics/retail/from-query-to-cart-inside-targets-search-bar-overhaul-with-alloydb-ai)

From query to cart: Inside Target's search bar overhaul with AlloyDB AI. 

## Latest videos

Watch the latest videos about AlloyDB AI.

## Latest blogs

Read the latest blogs about AlloyDB AI.

![URBN storefront and digital shopping illustration representing URBN customer story](https://docs.cloud.google.com/static/alloydb/images/urbn.png)

###  [ URBN modernizes retail infrastructure with AlloyDB ](https://cloud.google.com/customers/urbn?e=48754805)

Learn how URBN (parent company of Urban Outfitters, Anthropologie, and Free People) modernizes infrastructure to elevate employee creativity and global shopper experiences using AlloyDB and Gemini. 

![Neuropace thumbnail](https://docs.cloud.google.com/static/alloydb/images/neuropace.png)

###  [ Enhancing iEEG seizure identification and similarity search with Google Cloud ](https://cloud.google.com/blog/products/databases/neuropace-uses-alloydb-for-postgresql-as-vector-database/)

Learn how NeuroPace searched for more than a million iEEG records to identify similar records, in milliseconds using AlloyDB AI. 

![Vector search acceleration illustration](https://docs.cloud.google.com/static/alloydb/images/pgvector-aloydb-hnsw.png)

###  [ Supercharge pgvector: 4x Faster HNSW with AlloyDB ](https://cloud.google.com/blog/products/databases/supercharge-pgvector-4x-faster-hnsw-with-alloydb)

Learn how AlloyDB accelerates pgvector HNSW query performance by up to 4x using the built-in Columnar Engine. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
