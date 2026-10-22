---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/rank-rerank-search-results-rag/
title: Rank search results \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:40.092741+00:00
---

# Rank search results  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/rank-rerank-search-results-rag/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Rank search results Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/ai/rank-rerank-search-results-rag)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/ai/rank-rerank-search-results-rag)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/rank-rerank-search-results-rag)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/ai/rank-rerank-search-results-rag)

Learn how to rank and rerank your search results for applications using Vertex AI ranking models such as `semantic-ranker-default-003`. You can use the `ai.rank()` function to score documents based on relevance to a query, and improve vector search results by reranking them for better query ordering. 

The Vertex AI ranking API takes a list of documents and ranks those documents based on how relevant the documents are to a given query (a search string). When you use the `ai.rank()` function, it returns scores for how well a document answers a given query.

To use instructions on this page, you must have an understanding of AlloyDB Omni and be familiar with generative AI concepts.

AlloyDB Omni reserves, and creates, the `ai` schema.

**Note:** Vertex AI model support is governed by Vertex AI model versioning and lifecycle guidelines. For more information about stable versions, see [Model versions and lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions).

## Before you begin

Before you rank search results, do the following:

  1. [Configure user access to Vertex AI models](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-with-alloydb-ai#with-cloud).
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

  4. Enable the Discovery Engine API.

  5. Get the required roles to use ranking models.




### Enable the Discovery Engine API
    
    
    <p>To use ranking models, you must enable the Discovery Engine API.<br>
        Replace <code><var>PROJECT_ID</var></code> with your
        Google Cloud project ID and <code><var>PROJECT_NUMBER</var></code>
        with your corresponding project number.</p>
    
    <pre class="prettyprint lang-terminal">
        # Enable Discovery Engine API
        gcloud services enable discoveryengine.googleapis.com --project=<var>PROJECT_ID</var>
        gcloud projects add-iam-policy-binding <var>PROJECT_ID</var> \
        --member="serviceAccount:service-<var>PROJECT_NUMBER</var>@iam.gserviceaccount.com" \
        --role="roles/discoveryengine.viewer"
    </pre>
    
    <p>Model registration for ranking isn't required for Vertex AI models.
        You can use the Vertex AI model name as the
        <code>model_id</code>, which is shown in the following example.
    </p>
    
    <pre class="prettyprint lang-sql">
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
          'A backpacker guide to solo travel in India']);
    </pre>
    
    <p>A common use case for the semantic ranker is to rerank the results returned
        by vector search for better query ordering. The following example shows how to
        use the semantic ranking model for this use case. The example retrieves an
        initial result set for the query <code>personal fitness
        equipment</code> using vector search. These results are then re-ranked to
        return the top five results.
    </p>
    
    <pre class="prettyprint lang-sql">
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
      </pre>
    
      <p>For a list of available models and use cases, see <a href="/generative-ai-app-builder/docs/ranking#models">Supported models</a>.</p>
    

### Integrate with Vertex AI and install the extension

For more information, see [Configure your AlloyDB Omni installation to query cloud-based models](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-with-alloydb-ai#with-cloud).

### Required roles

To get the permissions that you need to use ranking models from Discovery Engine, ask your administrator to grant AlloyDB Omni service account the Discovery Engine Viewer (`roles/discoveryengine.viewer`) Identity and Access Management (IAM) role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Rank your search results

The following SQL query shows how to rank your search results:

**Note:** For API limits related to Vertex AI ranking models, see [Rank (or rerank) a set of records according to a query](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking#rank_or_rerank_a_set_of_records_according_to_a_query).
    
    
    SELECT index, score
    FROM
      ai.rank(
        model_id => 'MODEL_ID',
        search_string => 'SEARCH_STRING',
        documents => ARRAY['DOCUMENT_1', 'DOCUMENT_2', 'DOCUMENT_3'],
        top_n => TOP_N);
    

Replace the following:

Parameter | Description  
---|---  
`MODEL_ID` | A unique ID for the model endpoint that you define.  
`SEARCH_STRING` | A search string against which the records are ranked.  
`DOCUMENT_1`, `DOCUMENT_2`, `DOCUMENT_3` | An array of unique text strings that you want to rank.  
`TOP_N` | Optional: an integer that specifies the number of top-ranked documents to return.  
  
For a list of the supported Vertex AI ranking models, see [Supported models](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking#models).

## Examples

To rank search results using a Vertex AI ranking model, run the following query:
    
    
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
    

Consider an example AlloyDB Omni database with a list of review descriptions that are converted to embeddings. The following sample code snippet shows how to use the ranking model to retrieve the name of the top-ranked products based on their review descriptions' semantic similarity to a query.
    
    
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

  * [Register a model endpoint with model endpoint management](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/register-model-endpoint).

  * [Query using AI powered SQL operators](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/evaluate-semantic-queries-ai-operators).

  * [Perform time-series forecasting](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/perform-time-series-forecasting)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
