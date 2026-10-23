---
url: https://docs.cloud.google.com/alloydb/docs/ai/rank-rerank-search-results-rag/
title: Rank search results \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:36.449622+00:00
---

# Rank search results  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/rank-rerank-search-results-rag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Rank search results Stay organized with collections  Save and categorize content based on your preferences. 

The `ai.rank()` function in AlloyDB for PostgreSQL lets you rank and rerank search results in your SQL queries by using Gemini Enterprise Agent Platform ranking models, such as `semantic-ranker-default-003`, or large language models (LLMs). You can score candidate documents based on their semantic relevance to a query to improve retrieval-augmented generation (RAG) and vector search ordering.

The Agent Platform ranking API takes a list of documents and ranks those documents based on how relevant the documents are to a given query (a search string). When you use the `ai.rank()` function, it returns scores for how well a document answers a given query.

AlloyDB provides two different ranking capabilities through the `ai.rank()` function:

  * Ranking search results with the Ranking API: ranks a list of candidate document strings against a search query by using dedicated ranking models such as `semantic-ranker-default-003` or registered third-party rerankers, and returns a table that contains the `index` and `score` columns.
  * LLM-based semantic scoring: evaluates custom natural language scoring criteria row by row by using Gemini models in SQL queries—for example, in an `ORDER BY` clause. For more information, see [Score your query results](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators#score-query-results).



To use instructions on this page, you must have an understanding of AlloyDB and be familiar with generative AI concepts.

AlloyDB reserves, and creates, the `ai` schema.

**Note:** Agent Platform model support is governed by Agent Platform model versioning and lifecycle guidelines. For more information about stable versions, see [Model versions and lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions).

## Before you begin

Before you rank search results, do the following:

**Note:** AlloyDB doesn't charge for AI function calls. However, when you call Gemini Enterprise Agent Platform, third-party, or self-hosted models and services (such as for hybrid search) from your database, the model or infrastructure provider charges you directly. For more information about Gemini Enterprise Agent Platform costs, see [Pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing).

  * [Verify that the `google_ml_integration` extension is installed](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai#verify-installed-extension).
  * [Verify that the `google_ml_integration.enable_model_support` flag is set to `on`](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).
  * [Integrate with Agent Platform](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai).
  * Enable the Discovery Engine API.
  * Get the required roles to use ranking models.



### Enable the Discovery Engine API

###  Console 

  1. [Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=discoveryengine.googleapis.com)
  2. In the **Confirm project** step, click **Next** to confirm the name of the project you are going to make changes to.
  3. In the **Enable APIs** step, click **Enable** to enable the Discovery Engine API. If you already enabled this API, you won't see it listed here.



###  gcloud 

To use ranking models, you must enable the Discovery Engine API.  
Replace `PROJECT_ID` with your Google Cloud project ID and `PROJECT_NUMBER` with your corresponding project number.
    
    
        # Enable Discovery Engine API
        gcloud services enable discoveryengine.googleapis.com --project=PROJECT_ID
        gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com" \
        --role="roles/discoveryengine.viewer"

Model registration for ranking isn't required for Agent Platform models. You can use the Agent Platform model name as the `model_id`, which is shown in the following example. 
    
    
        SELECT index, score
        FROM
          ai.rank(
            model_id => 'semantic-ranker-default-003',
            search_string => 'Affordable family-friendly vacation spots in Southeast Asia?',
            documents =>
        ARRAY[
          'Luxury resorts in South Korea',
          'Family vacation packages for Vietnam: Ha Long Bay and Hoi An',
          'Budget-friendly beaches in Thailand perfect for families',
          'A backpacker guide to solo travel in India'])

A common use case for the semantic ranker is to rerank the results returned by vector search for better query ordering. The following example shows how to use the semantic ranking model for this use case. The example retrieves an initial result set for the query `personal fitness equipment` using vector search. These results are then re-ranked to return the top five results. 
    
    
        WITH initial_ranking AS (
          SELECT id, description, ROW_NUMBER() OVER () AS ref_number
          FROM product
          ORDER BY
            embedding <=> google_ml.embedding(
              'gemini-embedding-001', 'personal fitness equipment')::vector
          LIMIT 10
        ), reranked_results AS (
          SELECT index, score
          FROM ai.rank(
              model_id => 'semantic-ranker-default-003',
              search_string => 'personal fitness equipment',
              documents => (SELECT ARRAY_AGG(description ORDER BY ref_number) FROM initial_ranking),
              top_n => 5)
        )
        SELECT id, description
        FROM initial_ranking, reranked_results
        WHERE initial_ranking.ref_number = reranked_results.index
        ORDER BY reranked_results.score DESC;
      

For a list of available models and use cases, see [Supported models](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking#models).

### Integrate with Agent Platform and install the extension

  1. [Configure user access to Agent Platform models](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai).
  2. Verify that the latest version of `google_ml_integration` is installed. 
     1. To check the installed version, run the following command:
            
            SELECT extversion FROM pg_extension WHERE extname = 'google_ml_integration';
            extversion 
            ------------
            1.5.2
            (1 row)

     2. If the extension isn't installed or if the installed version is earlier than 1.5.2, update the extension.
            
            CREATE EXTENSION IF NOT EXISTS google_ml_integration;
            ALTER EXTENSION google_ml_integration UPDATE;

If you experience issues when you run the preceding commands, or if the extension isn't updated to version 1.5.2 after you run the preceding commands, contact [Google Cloud support](https://cloud.google.com/support).

  3. To use the AlloyDB AI query engine functionality, set the `google_ml_integration.enable_ai_query_engine` flag to `on`.

### SQL

     1. Enable the AI query engine for the current session.  

            
            SET google_ml_integration.enable_ai_query_engine = on;

     2. Enable features for a specific database across sessions.  

            
            ALTER DATABASE DATABASE_NAME SET google_ml_integration.enable_ai_query_engine = 'on';

     3. Enable the AI query engine for a specific user across sessions and databases.  

            
            ALTER ROLE postgres SET google_ml_integration.enable_ai_query_engine = 'on';

### Console

To modify the value of the `google_ml_integration.enable_ai_query_engine` flag, follow the steps in [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags#console). 

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

You can modify the value of the `google_ml_integration.enable_ai_query_engine` flag. For more information, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags#console). 
    
    gcloud alloydb instances update INSTANCE_ID \
      --database-flags google_ml_integration.enable_ai_query_engine=on \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --project=PROJECT_ID




### Required roles

To get the permissions that you need to use ranking models from Discovery Engine, ask your administrator to grant you the Discovery Engine Viewer (`roles/discoveryengine.viewer`) Identity and Access Management (IAM) role on `your project`. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Rank your search results

To rank your search results, run the following SQL query:

**Note:** For API limits related to Agent Platform ranking models, see [Rank (or rerank) a set of records according to a query](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking#rank_or_rerank_a_set_of_records_according_to_a_query).
    
    
    SELECT index, score
    FROM
      ai.rank(
        model_id => 'MODEL_ID',
        search_string => 'SEARCH_STRING',
        documents => ARRAY['DOCUMENT_1', 'DOCUMENT_2', 'DOCUMENT_3'],
        top_n => TOP_N); -- Optional
    

Replace the following:

Parameter | Description  
---|---  
`MODEL_ID` | The ranking model to use, such as `semantic-ranker-default-003`, `semantic-ranker-512`, or the identifier of a registered ranking model.  
`SEARCH_STRING` | The search query against which the candidate documents are evaluated and ranked.  
`DOCUMENT_1, DOCUMENT_2, DOCUMENT_3` | The candidate document strings to rank, passed as elements of a PostgreSQL text array (`text[]`).  
`TOP_N` (Optional) | The number of top-ranked results to return. If omitted or set to `NULL`, the function returns all ranked documents.  
  
### Return values

The `ai.rank()` function returns a table that contains the following columns:

Column | Type | Description  
---|---|---  
`index` | `integer` | The 1-based index corresponding to the position of the document in the input `documents` array.  
`score` | `real` | The relevance score assigned to the document. A higher score indicates greater relevance to the search query.  
  
For a list of the supported Agent Platform ranking models, see [Supported models](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking#models).

## Examples

To rank search results using a Agent Platform ranking model, run the following query:
    
    
    SELECT index, score
    FROM
      ai.rank(
        model_id => 'semantic-ranker-default-003',
        search_string => 'AlloyDB is a PostgreSQL compatible AI database that is ready for production.',
        documents =>
          ARRAY[
            'Alloys are made from combination of metals',
            'The best enterprise-ready PostgreSQL database.',
            'You can feel the heat in Alloy apartments.']);
    

The response is a table that shows each document and the score based on relevance to the search query. The following is the sample response:
    
    
     index | score
    -------+------------
         2 |  0.33
         1 |  0.28
         3 |  0.16
    (3 rows)
    

Consider an example AlloyDB database with a list of review descriptions that are converted to embeddings. The following sample code snippet shows how to use the ranking model to retrieve the name of the top-ranked products based on their review descriptions' semantic similarity to a query.
    
    
    WITH initial_ranking AS (
        SELECT product_id, name, review, review_id, ROW_NUMBER() OVER () AS ref_number
        FROM user_reviews
        ORDER BY
          review_desc_embedding <=> google_ml.embedding(
            'gemini-embedding-001', 'good desserts')::vector
        LIMIT 10
      ), reranked_results AS (
        SELECT index, score
        FROM
          ai.rank(
            model_id => 'semantic-ranker-512',
            search_string => 'good desserts',
            documents => (SELECT ARRAY_AGG(review ORDER BY ref_number) FROM initial_ranking),
            top_n => 5)
      )
    SELECT product_id, name
    FROM initial_ranking, reranked_results
    WHERE initial_ranking.ref_number = reranked_results.index
    ORDER BY reranked_results.score DESC;
    

**Note:** You get the 'semantic-ranker-default-003' model after you enable the Discovery Engine API and grant required permissions. For more information, see Before you begin.

## What's next

  * [Register a model endpoint with model endpoint management](https://docs.cloud.google.com/alloydb/docs/ai/register-model-endpoint).

  * [Perform intelligent SQL queries using AI functions](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators).

  * [Perform time-series forecasting](https://docs.cloud.google.com/alloydb/docs/ai/perform-time-series-forecasting)

  * Learn about the [model endpoint management reference](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
