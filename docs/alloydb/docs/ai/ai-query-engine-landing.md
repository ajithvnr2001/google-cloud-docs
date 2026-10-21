---
url: https://docs.cloud.google.com/alloydb/docs/ai/ai-query-engine-landing/
title: AI functions overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:39.189662+00:00
---

# AI functions overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/ai-query-engine-landing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  AI functions overview Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB AI functions let you run AI models registered through model endpoint management directly within your database by using SQL operators. Integration with Gemini Enterprise Agent Platform brings intelligent filtering, semantic ranking, and text generation to your operational data in real time. 

![AI-powered filtering thumbnail](https://docs.cloud.google.com/static/alloydb/images/in-filtering.png)

###  [ AI-Powered SQL filtering and ranking ](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators)

Use simple SQL functions for powerful AI tasks. The `google_ml_integration` extension provides operators like `ai.if()` for intelligent filtering and `ai.rank()` for semantic reranking. 

![In-database text generation thumbnail](https://docs.cloud.google.com/static/alloydb/images/database.png)

###  [ In-database text generation ](https://docs.cloud.google.com/alloydb/docs/ai/work-with-embeddings)

Perform transformations for rows in your database. Using the `ai.generate()` operator, you can ask a foundation model to summarize a product review, or to transform data directly in your query. 

![Embedding and prediction functions thumbnail](https://docs.cloud.google.com/static/alloydb/images/embedding-predictions.png)

###  [ Embedding and prediction functions ](https://docs.cloud.google.com/alloydb/docs/ai/model-endpoint-overview)

Use SQL functions like `google_ml.embedding()` to generate vector embeddings or `google_ml.predict_row(` to invoke predictions from any registered model, all within your database. 

## How the AI functions works

When you embed an AI operator like `ai.if()`, `ai.rank()`, or `ai.generate()` into your SQL query, the **AI functions** detect it. This engine, available using the `google_ml_integration` extension, orchestrates the entire process. It securely packages the relevant row data and calls a pre-registered ML model from providers, such as Gemini, OpenAI, or Anthropic. The ML model evaluates the data and returns a prediction—like `true/false` for a filter or a score for ranking. The AI functions seamlessly integrates this prediction back into your query's execution, returning a standard SQL result set. You get AI-powered insights without ever moving your data.

![Visual overview of AI functions](https://docs.cloud.google.com/static/alloydb/images/query-landing-page.png)

## Benefits of AlloyDB AI functions

Traditional database query mechanisms are often rigid, forcing developers to hardcode all potential user interaction paths. AlloyDB AI functions enable a significant change in the user experience by doing the following:

  * Infuse enterprise data with world knowledge: you can bring the real-world knowledge of Large Language Models (LLMs) directly to your AlloyDB for PostgreSQL database. The following are examples of how you can use AI functions:

    * Process unstructured data using `ai.generate`: you can manage raw, noisy, or unstructured user feedback—like reviews or logs—using Gemini with SQL.
    * Determine if transactions are fraudulent using `ai.if`: give the function a sequence of user actions, transaction notes, or chat summaries and ask it to evaluate a binary outcome: `Is this fraudulent?`
  * High-performance intelligence: use the following to accelerate performance and handle intelligence at scale with AI functions:

    * Use array-based processing to handle up to thousands of rows per second, which is 2,000x faster than row-at-a-time calls. Array-based processing is available for all AI functions. For more information, see [Perform intelligent SQL queries using AI functions](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators).
    * Use smart batching for AI functions to achieve significantly higher throughput than row-at-a-time calls. For more information, see [Accelerate performance for queries with AI functions](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-ai-queries).
    * Use optimized `ai.if` to eliminate the costs of using the LLM through improved efficiency, achieving 100,000 rows per second (a 23,000x improvement over row-at-a-time calls) and reducing costs by 6,000x to 1/10th of one cent.



## AlloyDB AI functions use cases

The following table describes use cases for AlloyDB AI functions.

  
**Function** |   
**Description** |   
**Use case**  
---|---|---  
      
    
    ai.if

|   
Intelligent, cognitive filtering based on natural language. |   
Determine which customer transactions appear fraudulent based on behavior patterns.  
      
    
    ai.rank

|   
Reranks vector search results based on deep contextual nuance. |   
Prioritize breathable fabrics for a `tropical wedding` search even if your database doesn't know what "breathable fabrics" means.  
      
    
    ai.generate

|   
Generates new content or transforms data formats. |   
Convert raw server log data into a structured JSON format for easier analysis.  
      
    
    ai.analyze_sentiment

|   
Classifies the emotional tone of text as positive, negative, or neutral. |   
Classify thousands of product reviews to gauge overall customer satisfaction.  
      
    
    ai.summarize

|   
Condenses lengthy text into essential information. |   
Extract key decisions and action items from conversational transcripts.  
      
    
    ai.agg_summarize

|   
An aggregate function that processes multiple rows in a column to generate a single, unified summary for a specified group of rows. |   
Generate a single, consolidated summary for a specific movie based on all of its individual reviews in a table.  
      
    
    ai.forecast

|   
Enables time-series forecasting using the [TimesFM model](https://docs.cloud.google.com/alloydb/docs/ai/perform-time-series-forecasting). |   
Predict future inventory needs based on historical sales data.  
  
## Learn more

Explore developer resources to build your own natural language query applications with AlloyDB AI.

Video 

###  [ AlloyDB AI vector search and AI operators ](https://www.youtube.com/watch?v=Li57kMm51zc)

Empower small IT teams to harness generative AI with Google Cloud databases. 

Codelab 

###  [ AlloyDB AI operators and reranking ](https://codelabs.developers.google.com/alloydb-ai-operators)

Deploy AlloyDB AI with AI operators. Use them for tasks such as semantic search, joins, and result ranking. 

Blog 

###  [ Model endpoint management ](https://cloud.google.com/blog/products/databases/use-model-endpoint-management-on-alloydb)

Build richer generative AI experiences using model endpoint management. 

Reference 

###  [ AlloyDB AI functions reference ](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint)

Reference documentation for the `google_ml_integration` extension functions and parameters. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
