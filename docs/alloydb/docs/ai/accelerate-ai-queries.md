---
url: https://docs.cloud.google.com/alloydb/docs/ai/accelerate-ai-queries/
title: Accelerate performance for queries with AI functions \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:30.923835+00:00
---

# Accelerate performance for queries with AI functions  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/accelerate-ai-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Accelerate performance for queries with AI functions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Smart batching for AI functions**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Smart batching for AI functions in AlloyDB for PostgreSQL lets you optimize performance when you run SQL queries that invoke AI models. It provides the same or better performance than [array-based functions](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators#filter-batch-arrays) without requiring you to write complex batching queries. For more information about AI functions, see [AI functions overview](https://docs.cloud.google.com/alloydb/docs/ai/ai-query-engine-landing).

Smart batching supports the following AI functions:

  * `ai.if`: Smart batching applies only to `SELECT` queries where the function is in the `WHERE` clause. It supports a single `ai.if` function per scan, and works with sequential, index, and bitmap heap scan. If a query contains multiple table scans—for example, on different tables, relations, or Common Table Expression (CTEs), then you can accelerate one `ai.if` function per scan.
  * `ai.rank`: Smart batching applies only to `SELECT` queries where the function is in the `ORDER BY` clause. It supports a single `ai.rank` function per scan. If a query contains multiple table scans—for example, on different tables, relations, or CTEs, then you can accelerate one `ai.rank` function per scan.

**Note:** This feature is available only for AlloyDB instances created on PostgreSQL 17.

## Enable smart batching for AI functions

To enable smart batching for AI functions, set the `google_ml_integration.enable_ai_function_acceleration` flag to `on`. This flag is disabled by default and controls whether the query executor is allowed to offload eligible AI operations to the AI function apply node for acceleration. When left unset or set to `off`, all query operations are executed by the standard PostgreSQL executor.

You can configure this flag at either the session or instance level.

To enable smart batching for AI functions at the instance level, use the `gcloud alloydb instances update` command:
    
    
    gcloud alloydb instances update INSTANCE_ID \
      --database-flags google_ml_integration.enable_ai_function_acceleration=on \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --project=PROJECT_ID

Replace the following:

  * `INSTANCE_ID`: the ID of the instance you want to update.
  * `REGION_ID`: the ID of the region where the cluster is located. For more information, see [Supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite#supported-regions).
  * `CLUSTER_ID`: the ID of the cluster.
  * `PROJECT_ID`: the ID of the project.



For more information about how to set an instance-level flag, see [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

## Verify smart batching for AI functions

To verify that smart batching for AI functions is enabled, you can use the `EXPLAIN` statement to analyze your query.

### Verify smart batching for AI functions for `ai.if` queries

The following example shows how to enable smart batching for AI functions for the current session and execute a query using the `ai.if` function:
    
    
    SET google_ml_integration.enable_ai_function_acceleration = on;
    
    EXPLAIN (COSTS OFF) SELECT r.name
    FROM restaurant_reviews r
    WHERE ai.if('Is the following a positive review? Review: '||r.review) AND r.city = 'Los Angeles'
    GROUP BY r.name
    HAVING count(*) > 20
    ORDER BY r.name;
    

When you use the `EXPLAIN` statement to analyze your query, the query plan shows an `AI Function Apply` node:
    
    
                                           QUERY PLAN                                       
    ----------------------------------------------------------------------------------------
     GroupAggregate
       Group Key: name
       Filter: (count(*) > 20)
       ->  Sort
             Sort Key: name
             ->  AI Function Apply
                   Filter: ai.if((('Is the following a positive review? Review: '::text || review)), NULL::character varying)
                   ->  Index Scan using idx_restaurant_reviews_city on restaurant_reviews r
                         Index Cond: ((city)::text = 'Los Angeles'::text)
    

### Verify smart batching for AI functions for `ai.rank` queries

The following example shows how to enable smart batching for AI functions for the current session and execute a query using the `ai.rank` function:
    
    
    SET google_ml_integration.enable_ai_function_acceleration = on;
    
    EXPLAIN (COSTS OFF) SELECT r.name, r.review
    FROM restaurant_reviews r
    WHERE r.city = 'Los Angeles'
    ORDER BY ai.rank('Rank these reviews based on how much they emphasize high-quality ingredients. Review: ' || r.review) DESC
    LIMIT 50;
    

When you use the `EXPLAIN` statement to analyze your query, the query plan shows an `AI Function Apply` node:
    
    
                                           QUERY PLAN                                       
    ----------------------------------------------------------------------------------------
     Limit
      ->  Sort
            Sort Key: (ai.rank(('Rank these reviews based on how much they emphasize high-quality ingredients. Review: ' || r.review'), NULL)) DESC
            ->  AI Function Apply
                  ->  Bitmap Heap Scan on restaurant_reviews r
                        Recheck Cond: (city = 'Los Angeles')
                        ->  Bitmap Index Scan on idx_restaurant_reviews_city
                              Index Cond: (city = 'Los Angeles')
    

The `AIFunctionApply` node in the query plan indicates that the query used smart batching for AI functions. If this node isn't present, the query used standard PostgreSQL execution.

## Limitations

  * Only basic arguments to the functions are supported. For `ai.if` and `ai.rank`, the `prompt` argument must be either a column reference or a string literal concatenated with a column reference. Any other arguments must be constants. Examples of supported `prompt` arguments include the following: 
    * `ai.if(r.review)`
    * `ai.if('Is this true? : ' || r.review)`
    * `ai.rank(r.review)`
    * `ai.rank('Rate this review: ' || r.review)`
  * Only `SELECT` queries with `ai.if` in `WHERE` clauses or `ai.rank` in `ORDER BY` clauses are supported.
  * Only one AI function per table scan is supported.
  * Only the default Gemini models are supported. For more information, see [Google models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). To use a different model, you can set the `google_ml_integration.default_llm_model` flag to the model ID you want to use.
  * The feature is available only in regions that support the `gemini-2.5-flash-lite` model or the regions for the LLM model that you set using the `google_ml_integration.default_llm_model` flag. For more information, see [Supported regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite#supported-regions).



## What's next

  * [Perform intelligent SQL queries using AI functions](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators).
  * [Accelerate AI queries using optimized functions](https://docs.cloud.google.com/alloydb/docs/ai/accelerate-queries-optimized-functions).
  * [Perform filtering using array-based functions](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators#filter-batch-arrays)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
