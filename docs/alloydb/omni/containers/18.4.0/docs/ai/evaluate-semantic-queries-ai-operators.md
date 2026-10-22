---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/evaluate-semantic-queries-ai-operators/
title: Perform intelligent SQL queries using AI functions \u00a0|\u00a0 AlloyDB Omni using containers: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:04:21.798343+00:00
---

# Perform intelligent SQL queries using AI functions  |  AlloyDB Omni using containers: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/evaluate-semantic-queries-ai-operators/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/overview)



Send feedback 

#  Perform intelligent SQL queries using AI functions Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/evaluate-semantic-queries-ai-operators)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/evaluate-semantic-queries-ai-operators)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/evaluate-semantic-queries-ai-operators)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/evaluate-semantic-queries-ai-operators)



This page shows you how to use the AlloyDB Omni AI query engine and perform intelligent SQL queries using AI functions.

AlloyDB AI functions integrate Large Language Models (LLMs) like Gemini directly with your AlloyDB Omni data to perform intelligent data operations. This feature includes built-in functions for the following:

  * Filtering (`ai.if`)
  * Semantic ranking (`ai.rank`)
  * Text generation (`ai.generate`)



These AI functions use the AlloyDB AI query engine to help your application process data using artificial intelligence models at various scales, from single-row responses to large-scale database operations. You can use the `ai.if`, `ai.rank`, and `ai.generate` operators to combine natural language with SQL queries. AlloyDB AI reserves and creates the [`ai`](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/reference/model-endpoint) schema.

**Note:** Using AI functions with your database can result in charges for processing and model token usage. For more information, see [Vertex AI pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing).

There are three categories of AI functions which differ based on how they handle input data and memory allocation: scalar, array-based, and cursor functions. Choosing the right AI function depends on the scale of your data and your performance requirements. Use the following table to learn about these functions and their use cases:

**Category** | **Description** | **Recommended use case**  
---|---|---  
Scalar | Designed for basic, one-to-one processing. Takes a single input and returns a single output. | Use when you want a basic function that provides acceptable performance for queries that make a small number—less than 50—of scalar function calls.  
Array-based | Processes data as an array of rows in a single function call. Takes an array as input and returns array as output. | Use for small-to-medium datasets where the entire array of eligible rows can fit within memory limits. This provides high throughput for set-based operations.  
Cursor | Takes a cursor as input and returns a cursor as output. | Use for processing large numbers of rows–for example, 10,000 rows.  
  
## Before you begin

  1. [Configure user access to Vertex AI models](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/register-model-endpoint). 
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



  * Use a Gemini model that's supported in your region. [Gemini 2.5 Flash Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite) is the AI query engine's default model. If you don't specify a Gemini model in the query, the AI query engine default model is chosen for the queries.



### Use a Gemini model that's supported in your region

If your AlloyDB Omni cluster is in a region where `gemini-2.5-flash-lite` isn't supported, you can use one of the other available Gemini models in your region using the `model_id` parameter.

**Note:** Verify model availability in your region. For more information, see [Gemini 2.5 Flash Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite).

Alternatively, you can register a Gemini model endpoint and provide that model ID to the AI operators. For more information, see [Register and call remote AI models using model endpoint management](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/register-model-endpoint).

The following example shows how to register another Gemini endpoint. In this example, this second Gemini endpoint is the global endpoint for `gemini-2.5-flash-lite`. You can use this registered model with AI operators by passing `model_id => 'gemini-2.5-flash-lite-global'` as an additional argument.
    
    
    CALL
      google_ml.create_model(
        model_id => 'gemini-2.5-flash-lite-global',
        model_type => 'llm',
        model_provider => 'google',
        model_qualified_name => 'gemini-2.5-flash-lite',
        model_request_url =>  'https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-2.5-flash-lite:generateContent',
        model_auth_type => 'alloydb_service_agent_iam'
    );
    

#### Use Gemini 3 models

Some Gemini models, such as `gemini-3-pro-preview`, are available only through the global endpoint. You must register such models as follows:
    
    
    CALL
      google_ml.create_model(
        model_id => 'gemini-3-preview-model',
        model_request_url => 'https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-3-pro-preview:generateContent',
        model_qualified_name => 'gemini-3-pro-preview',
        model_provider => 'google',
        model_type => 'llm',
        model_auth_type => 'alloydb_service_agent_iam'
    );
    

Replace `PROJECT_ID` with the ID of the project where the Vertex AI model is available. Note that the AlloyDB Omni service account must have the [Vertex AI User role](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#predefined-roles) in that project.

After registering the model, you can use it in AI functions as follows:
    
    
    SELECT ai.generate(prompt => 'What is AlloyDB?', model_id => 'gemini-3-preview-model');
    

## Use filters in your queries

AlloyDB AI offers AI-powered SQL functions that let you use natural language processing and LLMs directly within your database queries, including the `ai.if` and `ai.rank` operators.

**Note:** if you don't specify a batch size in your queries, the default batch size is 10.

### Perform filtering using scalar functions

To evaluate whether a condition stated in natural language is met, use the `ai.if`/`google_ml.if` operator. The function returns boolean true or false value, and returns `false` if the output isn't clearly detected.
    
    
    - Function signature
    FUNCTION ai.if(prompt TEXT, model_id VARCHAR(100) DEFAULT NULL) RETURNS bool
    

The following example shows the use of the `ai.if` operator as a filter to find restaurants with more than 500 positive reviews located in cities with a population greater than 100,000. The example uses `restaurant_reviews` and contains data like reviews and city location. The `ai.if` operator helps you understand the review sentiment and combine the locations from the database with Gemini general knowledge about the population in these locations.
    
    
    SELECT r.name, r.location_city
    FROM restaurant_reviews r
    WHERE
      AI.IF(r.location_city || ' has a population OF more than 100,000 AND the following is a positive review; Review: ' || r.review)
    GROUP BY r.name, r.location_city
    HAVING COUNT(*) > 500;
    

The following shows the same example using the model that you registered in Use a Gemini model that's supported in your region.
    
    
    SELECT r.name, r.location_city
    FROM restaurant_reviews r
    WHERE
      AI.IF(r.location_city || ' has a population of more than 100,000 AND the following is a positive review; Review: ' || r.review, model_id => 'gemini-2.5-flash-lite')
    GROUP BY r.name, r.location_city
    HAVING COUNT(*) > 500;
    

### Perform a join on a query that uses the if operator

To perform a join operation, use the `ai.if`/`google_ml.if` operator with join. The following sample query finds the number of reviews that mention each menu item from the restaurant menu.
    
    
        SELECT item_name, COUNT(*)
        FROM menu_items JOIN user_reviews
          ON ai.if(
            prompt => 'Does the following user review talk about the menu item mentioned ? review: ' || user_reviews.review_text || ' menu item: ' || item_name)
        GROUP BY item_name;
    

### Perform filtering using array-based functions

The following example identifies restaurants with more than 10 positive reviews by using an AI model (`gemini-2.5-flash-lite`) to analyze review sentiment and filter the results. `ARRAY_AGG` is used to transform individual rows of data into structured arrays so they can be processed by the AI model in bulk rather than one row at a time.
    
    
    WITH initial_arrays AS (
      SELECT
        ARRAY_AGG(r.id ORDER BY r.id) AS review_ids,
        -- Assuming ai.if takes an array of prompts and returns a boolean array
        ai.if(
          prompts => ARRAY_AGG('Is the review positive: ' || r.review ORDER BY r.id),
          model_id => 'gemini-2.5-flash-lite',
          batch_size => 20
        ) AS truth_values
      FROM restaurant_reviews r
    ),
    reviews AS (
    SELECT
      initial_arrays.review_ids[i] AS review_id,
      initial_arrays.truth_values[i] AS truth_value
    FROM
      initial_arrays,
      generate_series(1, array_length(initial_arrays.review_ids, 1)) AS i
    )
    SELECT rest_review.location_city, rest_review.name
    FROM restaurant_reviews rest_review JOIN reviews review ON rest_review.id=review.review_id
    WHERE review.truth_value = 't'
    GROUP BY rest_review.location_city, rest_review.name
    HAVING COUNT(*) > 10;
    

### Perform filtering using cursors

The following example shows how to filter a large set of restaurant reviews by streaming them through a cursor.

**Note:** if you don't specify a batch size, the default batch size is 10.
    
    
    CREATE TABLE filtered_results(input text, result bool);
    
    DO $$
    DECLARE
        prompt_cursor REFCURSOR;
        result_cursor REFCURSOR;
        rec RECORD;
    BEGIN
        -- 1. Open a cursor for the input data
        OPEN prompt_cursor FOR
            SELECT r.location_city || ' has a population of > 100,000 and is a positive review; Review: ' || r.review
            FROM restaurant_reviews r;
    
        -- 2. Call the array-based function using the input cursor
        result_cursor := ai.if(
            'Is the given statement true? ',
            prompt_cursor,
            model_id => 'gemini-2.5-flash-lite'
        );
    
        -- 3. Fetch results from the output cursor and store them
        LOOP
            FETCH result_cursor INTO rec;
            EXIT WHEN NOT FOUND;
            INSERT INTO filtered_results VALUES(rec.input, rec.output);
        END LOOP;
    
        CLOSE result_cursor;
    END $$;
    

## Text generation and summarization

AlloyDB AI offers text generation operators like scalar `ai.generate` and array-based and cursor-based `ai.generate`.

### Perform text generation using scalar functions

The `ai.generate` function produces text by combining provided data with the user's prompt.
    
    
    -- Function Signature
    FUNCTION ai.generate(prompt TEXT, model_id VARCHAR(100) DEFAULT NULL) RETURNS TEXT
    

For example, you can use the following query to generate a concise summary of each user review.
    
    
    SELECT
      ai.generate(
        prompt => 'Summarize the review in 20 words or less. Review: ' || review) AS review_summary
    FROM user_reviews;
    

### Perform text generation using array-based functions

The following query uses `UNNEST` and `ai.generate` to summarize multiple reviews efficiently.
    
    
    SELECT
      UNNEST(
        ai.generate(
          prompts => ARRAY_AGG('Summarize the review in 20 words or less. Review: ' || review),
          model_id => 'gemini-2.5-flash-lite'
        )
      ) AS review_summary
    FROM user_reviews;
    

### Perform text generation using cursors

To generate summaries or translations for millions of rows without hitting memory bottlenecks, use batch generation with cursors.
    
    
    CREATE TABLE summary_results(summary text);
    
    DO $$
    DECLARE
        prompt_cursor REFCURSOR;
        summary_cursor REFCURSOR;
        rec RECORD;
    BEGIN
        OPEN prompt_cursor FOR SELECT review_text FROM user_reviews ORDER BY id;
    
        summary_cursor := ai.generate(
            'Summarize the review in 20 words or less. Review:',
            prompt_cursor
        );
    
        LOOP
            FETCH summary_cursor INTO rec;
            EXIT WHEN NOT FOUND;
            INSERT INTO summary_results VALUES(rec.output);
        END LOOP;
    
        CLOSE summary_cursor;
    END $$;
    

## Score your query results

If you need to sort query results using custom, natural language instructions, use the `ai.rank` operator.

### Perform scoring using scalar functions

The following function lets you provide a prompt which describes the ranking criteria and returns a score for each item.
    
    
    -- Function signature
    FUNCTION ai.rank(prompt TEXT, model_id VARCHAR(100) DEFAULT NULL) RETURNS real
    

For example, the following query gets the top 20 most positive restaurant reviews, using scores from an LLM.
    
    
    SELECT review AS top20
    FROM user_reviews
    ORDER BY ai.rank(
      'Score the following review according to these rules:
      (1) Score OF 8 to 10 IF the review says the food IS excellent.
      (2) 4 to 7 IF the review says the food is ok.
      (3) 1 to 3 IF the review says the food is not good. Here is the review:' || review) DESC
    LIMIT 20;
    

### Perform scoring using array-based functions

This `ai.rank` function lets you score and rank query results based on custom natural language instructions.
    
    
    FUNCTION ai.rank(prompts TEXT[], batch_size INT DEFAULT NULL, model_id VARCHAR(100) DEFAULT NULL) RETURNS real[]
    

The following query uses `UNNEST` and `ai.rank` to score multiple reviews efficiently.
    
    
    SELECT
      UNNEST(
        ai.rank(
          ARRAY_AGG('Score the following review according to these rules:
      (1) Score OF 8 to 10 IF the review says the food IS excellent.
      (2) 4 to 7 IF the review says the food is ok.
      (3) 1 to 3 IF the review says the food is not good. Here is the review:' || review)
        )
      ) as review_scores
    FROM user_reviews;
    

### Perform scoring using cursors

This function is used for scoring large datasets without hitting memory limits.
    
    
    FUNCTION ai.rank(context TEXT, input_cursor REFCURSOR, batch_size INT DEFAULT NULL, model_id VARCHAR(100) DEFAULT NULL) RETURNS REFCURSOR
    

The following example shows you how to score large volumes of text according to specific natural language criteria.
    
    
    CREATE TABLE scored_results(input text, score real);
    
    DO $$
    DECLARE
        prompt_cursor REFCURSOR;
        score_cursor REFCURSOR;
        rec RECORD;
    BEGIN
        OPEN prompt_cursor FOR SELECT review FROM user_reviews ORDER BY id;
    
        score_cursor := ai.rank(
            'Score the following review: (1) 8-10 if excellent, (2) 4-7 if ok, (3) 1-3 if not good. Review:',
            prompt_cursor
        );
    
        LOOP
            FETCH score_cursor INTO rec;
            EXIT WHEN NOT FOUND;
            INSERT INTO scored_results VALUES(rec.input, rec.output);
        END LOOP;
    
        CLOSE score_cursor;
    END $$;
    

## What's next

  * [Register a model endpoint with model endpoint management](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/register-model-endpoint).

  * [Rank and score search results for RAG](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/rank-rerank-search-results-rag).

  * [Semantically filter SQL queries and rank results](https://codelabs.developers.google.com/alloydb-ai-operators).

  * [Perform time-series forecasting](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/perform-time-series-forecasting).

  * [Analyze sentiment](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/analyze-sentiment).

  * [Summarize content](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/summarize-content).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
