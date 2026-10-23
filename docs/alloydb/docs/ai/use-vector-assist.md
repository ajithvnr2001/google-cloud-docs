---
url: https://docs.cloud.google.com/alloydb/docs/ai/use-vector-assist/
title: Use vector assist \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:31.741836+00:00
---

# Use vector assist  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/use-vector-assist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Use vector assist Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Vector assist**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Vector assist in AlloyDB for PostgreSQL provides a declarative SQL framework that lets you deploy, tune, and manage vector search workloads on your instances. You can define your vector search requirements, generate and apply recommended SQL configurations, and monitor workload performance. To learn more about how vector assist works, see [Vector assist overview](https://docs.cloud.google.com/alloydb/docs/ai/vector-assist-overview).

## Before you begin

  * Confirm your instance is using the correct maintenance version. vector assist requires a minimum maintenance version number of `POSTGRES_17.20260128.03_06`. For more information about performing self-service maintenance, see [Performance self-service maintenance](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance).
  * Enable the vector assist extension using the following command in the database you want to use:
        
        CREATE EXTENSION vector_assist CASCADE;
        

This generates the `vector_assist` schema, which is used by vector assist.




## Use vector assist to deploy a vector workload

To use vector assist to deploy and manage a vector workload, you must do the following:

  * Define your vector specification
  * View vector assist recommendations
  * Apply vector assist recommendations



### Define your vector specification

Defining the [vector specification](https://docs.cloud.google.com/alloydb/docs/ai/vector-assist-overview#spec), or _vector spec_ , is the first step in using vector assist. Depending on the type of vector workload, the fields you use to define your vector spec might be different.

For example, if you want to enable semantic search on a specific column in a table, run the [`vector_assist.define_spec`](https://docs.cloud.google.com/alloydb/docs/reference/ai/vector-assist#define-spec) function to define your vector spec:
    
    
    SELECT
      recommendation_id,
      REGEXP_REPLACE(query, 'SET hnsw.ef_search TO \d+', 'SET hnsw.ef_search TO') AS query_1,
      recommendation,
      vector_spec_id,
      table_name,
      applied,
      modified
    FROM vector_assist.define_spec(
      table_name => 'TABLE_NAME',
      vector_column_name => 'VECTOR_COLUMN_NAME',
      target_recall => TARGET_RECALL,
      tune_vector_index => TUNE_INDEX
    );
    

Replace the following parameters:

  * `TABLE_NAME`: name of the table you want to use in your vector workload.

  * (Optional) `VECTOR_COLUMN_NAME`: column you want to perform a semantic search on. If you only have one column with vectors in your table, `vector_assist` can set this automatically. If there is more than one table with vectors, you must specify which column to use.

  * (Optional) `TARGET_RECALL`: target recall you want vector assist to meet. If specified, `vector_assist` experiments with different `ef_search` values, comparing the recall in exact, nearest-neighbor searches. `vector_assist` sets `ef_search` to the value that provides the closest target recall. The default value is `0.95`.

  * (Optional) `TUNE_INDEX`: boolean that specifies whether vector assist tunes the vector indexes in your workload. The default value is `false`, which means that only the search-related parameters (`ef_search`) are tuned—build time parameters (`m`, `ef_construction`) don't get tuned.




To see a complete list of all available parameters for the vector spec, see [Vector assist function references](https://docs.cloud.google.com/alloydb/docs/reference/ai/vector-assist).

After you run the query to create your vector spec, vector assist automatically generates steps, called recommendations, that you must run to deploy your vector workload.

### View vector assist recommendations

To view the recommendations generated by vector assist using your vector spec, run the [`vector_assist.get_recommendations`](https://docs.cloud.google.com/alloydb/docs/reference/ai/vector-assist#get-recommendations) function:
    
    
    SELECT vector_assist.get_recommendations(
      spec_id => 'SPEC_ID'
    );
    

Replace `SPEC_ID` with the spec ID of the vector spec that you want to view recommendations for. To get your list of available vector specs, see List your vector specs.

`vector_assist.get_recommendations` returns a table called `vector_assist.RECOMMENDATIONS` that contains all recommendations. Each recommendation is stored in a table with the associated `spec_id`. Each recommendation generally contains the following information:

  * SQL query you need to run
  * Detailed explanation for the recommendation
  * Other relevant information that explains the recommendation



### Apply vector assist recommendations

You can apply the generated recommendations individually or as a whole.

To apply a specific recommendation, run the [`vector_assist.apply_recommendation`](https://docs.cloud.google.com/alloydb/docs/reference/ai/vector-assist#apply-recommendation) function:
    
    
    SELECT vector_assist.apply_recommendation(
      recommendation_id => 'RECOMMENDATION_ID'
    );
    

Replace `RECOMMENDATION_ID` with the ID of the vector assist recommendation you want to apply from the `vector_assist.RECOMMENDATIONS` table.

To apply all recommendations together, run the [`vector_assist.apply_spec`](https://docs.cloud.google.com/alloydb/docs/reference/ai/vector-assist#apply-spec) function with either the `spec_id` or `table_name` parameter:
    
    
    SELECT vector_assist.apply_spec(
      spec_id => 'SPEC_ID'
    );
    

Replace `SPEC_ID` with the ID of the vector spec you want to use.

Optionally, you can also input the `schema_name` or `column_name` parameters. For information on all available query parameters, see [Vector assist function references](https://docs.cloud.google.com/alloydb/docs/reference/ai/vector-assist#apply-spec).

Once you apply the recommendations generated by vector assist, the vector index is ready for use.

## Generate search queries

You can use vector assist to help you build optimized search queries for your deployed vector workloads using the workload's vector spec and generated vector index. To generate an optimized search query, run the [`vector_assist.generate_query`](https://docs.cloud.google.com/alloydb/docs/reference/ai/vector-assist#generate-query) function:
    
    
    SELECT vector_assist.generate_query(
      spec_id => 'SPEC_ID',
      search_vector => 'SEARCH_VECTOR',
      top_k => TOP_K,
      target_recall => TARGET_RECALL,
      filter_expressions => ARRAY['FILTER_EXPRESSION']
    );
    

Replace the following parameters:

  * `SPEC_ID`: ID of the spec you want to use.

  * `SEARCH_VECTOR`: vector for your search query. For example, `[1, 2, 3]`.

  * (Optional) `TOP_K`: number of nearest neighbors to return. If not specified, the default value is `10`.

  * (Optional) `TARGET_RECALL`: target recall you want vector assist to meet. If specified, `vector_assist` experiments with different `ef_search` values, comparing the recall in exact, nearest-neighbor searches. `vector_assist` sets `ef_search` to the value that provides the closest target recall.

  * (Optional) `FILTER_EXPRESSION`: any filters for the search query. For example, filtering based on other columns.




To see a complete list of all available parameters for generating a search query, see [Vector assist function references](https://docs.cloud.google.com/alloydb/docs/reference/ai/vector-assist).

The output of this function returns text that contains a SQL query. You can run or save this SQL query as necessary.

## List your vector specs

If you need to list your existing vector specs for a table, run the `vector_assist.list_specs` function, or use `vector_assist.get_spec` to view a single vector spec by ID:
    
    
    SELECT vector_assist.list_specs(
      table_name => 'TABLE_NAME',
      column_name => 'COLUMN_NAME'
    );
    

Replace the following parameters:

  * `TABLE_NAME`: name of the table that you used to define your vector spec.

  * (Optional) `COLUMN_NAME`: name of the vector column in the table. If omitted, `vector_assist.list_specs` returns all vector specs defined on the specified table. To retrieve a specific vector spec by ID, call `SELECT vector_assist.get_spec(spec_id => 'SPEC_ID');`.




## What's next

  * Learn more about [vector assist](https://docs.cloud.google.com/alloydb/docs/ai/vector-assist-overview).
  * [Vector assist function references](https://docs.cloud.google.com/alloydb/docs/reference/ai/vector-assist).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
