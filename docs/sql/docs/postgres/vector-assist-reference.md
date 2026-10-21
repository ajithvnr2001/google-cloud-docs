---
url: https://docs.cloud.google.com/sql/docs/postgres/vector-assist-reference/
title: Vector assist reference \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:51.728974+00:00
---

# Vector assist reference  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/vector-assist-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Vector assist reference Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview — Vector Assist**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Warning:** Vector assist ([Preview](https://cloud.google.com/products)) is temporarily disabled for all Cloud SQL for PostgreSQL instances.

This page provides detailed information about all available vector assist functions, and their required and optional parameters.

## `vector_assist.define_spec`

Defines a new vector specification, or _vector spec_ , and returns recommendations necessary to step up the vector workload. This function applies user-provided specifications to generate the recommendations.

### Function
    
    
    CREATE OR REPLACE FUNCTION vector_assist.define_spec(
        spec_id TEXT DEFAULT NULL,
        table_name TEXT,
        schema_name TEXT DEFAULT NULL,
        vector_column_name TEXT DEFAULT NULL,
        text_column_name TEXT DEFAULT NULL,
        vector_index_type TEXT DEFAULT NULL, -- Allowed: 'hnsw', 'ivfflat'
        embeddings_available BOOL DEFAULT NULL,
        embedding_model TEXT DEFAULT NULL,
        num_vectors INT DEFAULT NULL,
        dimensionality INT DEFAULT NULL,
        distance_func TEXT DEFAULT NULL, -- Allowed: 'cosine', 'ip', 'l2', 'l1'
        quantization TEXT DEFAULT NULL, -- Allowed: 'none', 'halfvec', 'bit'
        prefilter_column_names TEXT[] DEFAULT NULL,
        memory_budget_kb INT DEFAULT NULL, -- In KB
        target_recall FLOAT DEFAULT NULL,
        target_top_k INT DEFAULT NULL,
        tune_vector_index BOOL DEFAULT FALSE, -- Set to true if target_recall is set
    )
    RETURNS SETOF vector_assist.RECOMMENDATIONS;
    

### Parameters

Parameter | Required? | Description  
---|---|---  
`spec_id` | Required (Auto-generated) | A unique ID for the vector spec that you define.  
`table_name` | Required? | The table name to be used in the vector workload setup.  
`schema_name` | Optional | The schema containing the table to be used in the vector workload. The schema is automatically inferred based on the schema search path.  
`vector_column_name` | Optional or required | The column name for the column containing the vector embeddings.  
  
This column is required if you're using more than one vector column and the `text_column_name` is not declared. If you're only using one vector column, then this parameter is optional.  
`text_column_name` | Optional or required | The column name for the text column. If your vector workload requires embeddings generation from a text column, then this parameter is required.  
  
This column is required if the `vector_column_name` parameter is `NULL` and there are no other vector columns.  
  
This parameter uses the `google_ml_integration` extension to generate embeddings from the given text column.  
`vector_index_type` | Optional | The type of the vector index. Acceptable values include: 

  * `HNSW`
  * `IVFFlat`
  * `SCANN`

  
`embeddings_available` | Optional | A boolean that checks if vector embeddings exist in the selected table. This field is set to `FALSE` if no vector columns are detected and the `text_column_name` parameter is set.  
`embedding_model` | Optional or required | The model ID from [`google_ml.models`](https://docs.cloud.google.com/sql/docs/postgres/generate-manage-vector-embeddings#embedding-generation) to be used to generate the embeddings. This field is optional, unless the `embeddings_available` parameter is `FALSE` or `NULL`.  
`num_vectors` | Optional | The number of vectors in the table.  
`dismensionality` | Optional | The dimension of the given vectors.  
`distance_func` | Optional | The distance function to be used to compare vector. Acceptable values include `cosine`, `ip`, `l2`, or `l1`.  
`quantization` | Optional | The quantization for the vector indexes. Acceptable values include `none`, `halfvec`, or `bit`.  
`prefilter_column_names` | Optional | Creates an index for specified column for prefiltering. This might help improve performance for queries with a high selectivity filter on the column.  
`memory_budget_kb` | Optional | The maximum memory (in KB) for index building.  
`target_recall` | Optional | The target recall for standard vector queries.  
`target_top_k` | Optional | The top-K matching values to retrieve for recall calculation. This value is used if the `target_recall` parameter is specified.  
`tune_vector_index` | Optional | Tunes the vector indexes in your workload. If enabled, vector assist auto-tunes the vector index or search query using the vector spec, and computes the optimal database and index parameters Acceptable values include `TRUE` or `FALSE`.  
  
### Return value

Returns a table of recommendations that must be applied to set up the requested vector workload. Each row is a single recommendation that contains an executable SQL query and a detailed explanation of why to apply the recommendation. The recommendation can be applied using the `apply_recommendation()` function.

**Note:** This function is a long-running operation (LRO). If you're using a client with a timeout (such as Cloud SQL studio with a 5-minute timeout), then the function call might be terminated. To mitigate this issue, you can either increase the timeout threshold, or create a copy of the table you're using with only a subset of data to meet the timeout requirements.

The recommendations table contains the following columns:

Column name | Type | Description  
---|---|---  
`recommendation_id` | Text | The ID of the recommendation. The recommendation is applied using this ID.  
`vector_spec_id` | Text | The ID of the vector spec that is associated with the recommendation.  
`table_name` | Text | The table name associated with the recommendation.  
`schema_name` | Text | The schema name containing the given table.  
`query` | Text | The executable SQL query to be run to achieve the outcome of the recommendation.  
`recommendation` | Text | The explanation for the recommendation, including the expected outcome once the recommendation is applied. This column also contains the reason and rationale for the recommendation. You can use this context to tune the query as necessary and regenerate recommendations.  
`applied` | Boolean | Shows whether the recommendation has been applied.  
`modified` | Boolean | Shows whether the recommendation has been modified by the user.  
`created_at` | Timestamp with time zone | The time when the recommendation was generated in the `timestamp with time zone` format. For example, `2024-07-18 09:00:00-08`.  
  
## `vector_assist.list_specs`

Returns the current vector spec for a given table and column.

### Function
    
    
    CREATE OR REPLACE FUNCTION vector_assist.list_specs(
      table_name      TEXT,
      column_name     TEXT DEFAULT NULL
    )
    RETURNS SETOF vector_assist.VECTOR_SPECS
    

### Parameters

Parameter | Required? | Description  
---|---|---  
`table_name` | Required? | The name of the table that the vector spec is retrieved for.  
`column_name` | Optional | The column name to filter the table on before returning the spec. If the column name is specified, then specifications that contain text or vector column names that match this column name are returned.  
  
### Return value

Returns a table of specifications for the given table and optionally, column name.

## `vector_assist.modify_spec`

Modifies an existing vector spec. When the vector spec is modified, the associated recommendations are regenerated based on the new specs.

### Function
    
    
    CREATE OR REPLACE FUNCTION vector_assist.modify_spec(
      spec_id                TEXT,
      table_name             TEXT DEFAULT NULL,
      schema_name            TEXT DEFAULT NULL,
      vector_column_name     TEXT DEFAULT NULL,
      text_column_name       TEXT DEFAULT NULL,
      vector_index_type      TEXT DEFAULT NULL,
      embeddings_available   BOOL DEFAULT NULL,
      num_vectors            INT DEFAULT NULL,
      dimensionality         INT DEFAULT NULL,
      embedding_model        TEXT DEFAULT NULL,
      prefilter_column_names TEXT[] DEFAULT NULL,
      distance_func          TEXT DEFAULT NULL,
      quantization           TEXT DEFAULT NULL,
      memory_budget_kb       INT DEFAULT NULL,
      target_recall          FLOAT DEFAULT NULL,
      target_top_k           INT DEFAULT NULL,
      tune_vector_index      BOOL DEFAULT NULL
    )
    RETURNS SETOF vector_assist.RECOMMENDATIONS
    

### Parameters

Parameter | Required? | Description  
---|---|---  
`spec_id` | Required (Auto-generated) | A unique ID for the vector spec that you define.  
`table_name` | Required? | The table name to be used in the vector workload setup.  
`schema_name` | Optional | The schema containing the table to be used in the vector workload. The schema is automatically inferred based on the schema search path.  
`vector_column_name` | Optional or required | The column name for the column containing the vector embeddings.  
  
This column is required if you're using more than one vector column and the `text_column_name` is not declared. If you're only using one vector column, then this parameter is optional.  
`text_column_name` | Optional or required | The column name for the text column. If your vector workload requires embeddings generation from a text column, then this parameter is required.  
  
This column is required if the `vector_column_name` parameter is `NULL` and there are no other vector columns.  
  
This parameter uses the `google_ml_integration` extension to generate embeddings from the given text column.  
`vector_index_type` | Optional | The type of the vector index. Acceptable values include: 

  * `HNSW`
  * `IVFFlat`
  * `SCANN`

  
`embeddings_available` | Optional | A boolean that checks if vector embeddings exist in the selected table. This field is set to `FALSE` if no vector columns are detected and the `text_column_name` parameter is set.  
`embedding_model` | Optional or required | The model ID from [`google_ml.models`](https://docs.cloud.google.com/sql/docs/postgres/generate-manage-vector-embeddings#embedding-generation) to be used to generate the embeddings. This field is optional, unless the `embeddings_available` parameter is `FALSE` or `NULL`.  
`num_vectors` | Optional | The number of vectors in the table.  
`dismensionality` | Optional | The dimension of the given vectors.  
`distance_func` | Optional | The distance function to be used to compare vector. Acceptable values include `cosine`, `ip`, `l2`, or `l1`.  
`quantization` | Optional | The quantization for the vector indexes. Acceptable values include `none`, `halfvec`, or `bit`.  
`prefilter_column_names` | Optional | Identifies the columns that are made available for prefiltering in vector search queries.  
`memory_budget_kb` | Optional | The maximum memory (in KB) for index building.  
`target_recall` | Optional | The target recall for standard vector queries.  
`target_top_k` | Optional | The top-K matching values to retrieve for recall calculation. This value is used if the `target_recall` parameter is specified.  
`tune_vector_index` | Optional | Tunes the vector indexes in your workload. If enabled, vector assist auto-tunes the vector index or search query using the vector spec, and computes the optimal database and index parameters Acceptable values include `TRUE` or `FALSE`.  
  
### Return value

Returns an updated table of recommendations that must be applied to set up the requested vector workload. Each row is a single recommendation that contains an executable SQL query and a detailed explanation of why to apply the recommendation. The recommendation can be applied using the apply_recommendation() function.

The recommendations table contains the following columns:

Column name | Type | Description  
---|---|---  
`recommendation_id` | Text | The ID of the recommendation. The recommendation is applied using this ID.  
`vector_spec_id` | Text | The ID of the vector spec that is associated with the recommendation.  
`table_name` | Text | The table name associated with the recommendation.  
`schema_name` | Text | The schema name containing the given table.  
`query` | Text | The executable SQL query to be run to achieve the outcome of the recommendation.  
`recommendation` | Text | The explanation for the recommendation, including the expected outcome once the recommendation is applied. This column also contains the reason and rationale for the recommendation. You can use this context to tune the query as necessary and regenerate recommendations.  
`applied` | Boolean | Shows whether the recommendation has been applied.  
`modified` | Boolean | Shows whether the recommendation has been modified by the user.  
`created_at` | Timestamp with timezone | The time when the recommendation was generated.  
  
## `vector_assist.get_recommendations`

Returns recommendations associated with a specific vector `spec_id`.

### Function
    
    
    CREATE OR REPLACE FUNCTION vector_assist.get_recommendations (
        spec_id TEXT
    )
    RETURNS SETOF vector_assist.RECOMMENDATIONS;
    

### Parameters

Parameter | Required? | Description  
---|---|---  
`spec_id` | Required? | Gets recommendations for the specified vector `spec_id`.  
  
### Return value

Returns a table of requested recommendations.

The recommendations table contains the following columns:

Column name | Type | Description  
---|---|---  
`recommendation_id` | Text | The ID of the recommendation. The recommendation is applied using this ID.  
`vector_spec_id` | Text | The ID of the vector spec that is associated with the recommendation.  
`table_name` | Text | The table name associated with the recommendation.  
`schema_name` | Text | The schema name containing the given table.  
`query` | Text | The executable SQL query to be run to achieve the outcome of the recommendation.  
`recommendation` | Text | The explanation for the recommendation, including the expected outcome once the recommendation is applied. This column also contains the reason and rationale for the recommendation. You can use this context to tune the query as necessary and regenerate recommendations.  
`applied` | Boolean | Shows whether the recommendation has been applied.  
`modified` | Boolean | Shows whether the recommendation has been modified by the user.  
`created_at` | Timestamp with timezone | The time when the recommendation was generated.  
  
## `vector_assist.apply_recommendation`

Applies a single recommendation using the `recommendation_id`.

### Function
    
    
    CREATE OR REPLACE FUNCTION vector_assist.get_recommendations (
        spec_id TEXT
    )
    RETURNS SETOF vector_assist.RECOMMENDATIONS;
    

### Parameters

Parameter | Required? | Description  
---|---|---  
`recommenation_id` | Required? | The ID of the vector recommendation to apply.  
  
### Return value

Returns a boolean that confirms if a recommendation was successfully applied and update the `vector_assist.RECOMMENDATIONS` table column `applied` to `TRUE`.

If vector assist is unable to apply the recommendation, then it raises an error message on failure.

## `vector_assist.apply_spec`

Applies all recommendations associated with a specific vector `spec_id` or table name. This function goes through all recommendations and runs the `vector_assist.apply_recommendation` function on each recommendation.

Must specify either a `spec_id` or `table_name` to run function.

### Function
    
    
    CREATE OR REPLACE FUNCTION vector_assist.apply_spec(
        spec_id TEXT DEFAULT NULL,
        table_name TEXT DEFAULT NULL,
        schema_name TEXT DEFAULT NULL,
        column_name TEXT DEFAULT NULL -- text_column_name or vector_column_name
    )
    RETURNS BOOLEAN;
    

### Parameters

Parameter | Required? | Description  
---|---|---  
`spec_id` | Optional | Applies all recommendations for the given vector `spec_id`.   
`table_name` | Optional | Applies all recommendations for the given table.  
`schema_name` | Optional | The schema containing the specified table.  
`column_name` | Optional | Identifies the `text_column_name` or `vector_column_name` to use if the table contains multiple vector specs.  
  
### Return value

Returns a boolean that confirms if all recommendations were successfully applied and sets the value in the `vector_assist.RECOMMENDATIONS` table column `applied` to `TRUE` for all recommendations.

If vector assist is unable to apply the recommendation, then it raises an error message on failure.

## `vector_assist.modify_recommendation`

Modifies the query for a specific recommendation and sets the `modified` field in the `vector_assist.RECOMMENDATIONS` table for the associated recommendation to `TRUE`.

### Function
    
    
    CREATE OR REPLACE FUNCTION vector_assist.modify_recommendation(
        recommendation_id TEXT,
        modified_query TEXT
    )
    RETURNS BOOLEAN;
    

### Parameters

Parameter | Required? | Description  
---|---|---  
`recommendation_id` | Required? | The ID of the recommendation to modify.  
`modified_query` | Required? | A user-modified SQL query for the recommendation.  
  
## Return value

Returns a boolean that confirms if a recommendation was successfully updated and sets the `vector_assist.RECOMMENDATIONS` table column `modified` to `TRUE`.

If vector assist is unable to update the recommendation, then it raises an error message on failure.

## `vector_assist.generate_query`

Generates an optimized vector search query based on the defined vector spec and search parameters. This function might tune the `ef_search` value to meet the set `target_recall` if applicable.

### Function
    
    
    CREATE OR REPLACE FUNCTION vector_assist.generate_query(
        spec_id TEXT DEFAULT NULL,
        table_name TEXT DEFAULT NULL,
        schema_name TEXT DEFAULT NULL,
        column_name TEXT DEFAULT NULL, -- text_column_name or vector_column_name of the spec
        search_text TEXT DEFAULT NULL,
        search_vector VECTOR DEFAULT NULL, -- e.g. '[1.0,2.0,3.0]'::vector
       output_column_names TEXT[] DEFAULT NULL, -- Columns to retrieve, NULL for SELECT *
        top_k INT DEFAULT NULL,
        filter_expressions TEXT[] DEFAULT NULL,
        target_recall FLOAT DEFAULT NULL, -- Inherited from spec, can be overridden
        iterative_index_search BOOL DEFAULT NULL
    )
    RETURNS TEXT; -- Returns the text representing the search query
    

### Parameters

Parameter | Required? | Description  
---|---|---  
`spec_id` | Optional | Specifies the `spec_id` to generate the query for.  
`table_name` | Optional | Specifies the table name to generate the search query for if the `spec_id` isn't provided. If a table contains multiple specs, then the parameter returns an error.  
`column_name` | Optional | Specifics the column name to generate the search query for if the `spec_id` isn't provided. If the column contains multiple specs, then the parameter returns an error. The `column_name` might be the `text_column_name` or the `vector_column_name`.  
`output_column_name` | Optional | The column names to retrieve in the output query. To retrieve all columns, set this parameter to `NULL`.  
`search_text` | Optional | The search text to generate embeddings for. Requires the `embedding_model` in the vector spec. The embedding is generated using the model from the spec. You can only set either the `search_text` or the `search_vector` parameter.  
`search_vector` | Optional | The vector for the search query. You can only set either the `search_text` or the `search_vector` parameter  
`top_k` | Optional | The number of nearest neighbors to return.  
`filter_expressions` | Optional | The filter expressions to apply in the search query. The filters can be applied to fields in the table, such as price < 100.  
`iterative_index_search` | Optional | Sets whether to perform [iterative index search](https://github.com/pgvector/pgvector?tab=readme-ov-file#iterative-index-scans) for filtered queries.This parameter overrides the settings in the vector spec.  
`target_recall` | Optional | The target recall for the search query only. This parameter overrides the settings in the vector spec and tunes `ef_search`.  
  
### Return value

Returns a text containing the vector search query for the given parameters. This query can be executed or saved to run later.

## `vector_assist.evaluate_query_recall`

Evaluates the recall of the vector index for a given query. This function uses the database and index configurations in a JSON string as inputs.

### Function
    
    
    CREATE OR REPLACE FUNCTION vector_assist.evaluate_query_recall(
      IN ann_query text,
      IN vector_search_configurations json DEFAULT NULL,
      OUT recall float,
      OUT ann_execution_time float,
      OUT ground_truth_execution_time float,
      OUT index_type text)
    RETURNS RECORD
    

### Parameters

Parameter | Required? | Description  
---|---|---  
`ann_query` | Required? | The SQL query for which recall needs to be evaluated. This query should be a `pgvector` ANN query.  
`vector_search_configurations` | Optional | The configurations that can be set for the ANN query. This parameter must be in JSON format.  
  
### Return value

Returns a table that evaluates the recall of the vector index for the given query.

The table contains the following columns:

Column name | Type | Description  
---|---|---  
`recall` | Float | The percentage of vectors that the index returns, which are true nearest neighbors. This metric is used to quantify search quality. This function lets you tune the parameters to return the expected vector query recall results.  
`ann_execution_time` | Float | The time it takes a vector query to execute using index scans.  
`ground_truth_execution_time` | Float | The time it takes the query to run using a sequential scan.  
  
### Example

The following example evaluates the recall for a `HNSW` index and overrides the `HNSW.ef_search` configuration parameter:
    
    
    SELECT * FROM vector_assist.evaluate_query_recall(
      ann_query => 'SELECT id FROM items ORDER BY embedding <=> ''[1,2,3]'' LIMIT 10',
      vector_search_configurations => '{"hnsw.ef_search": 30}'
    );
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
