---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/generate-manage-auto-embeddings-for-tables/
title: Generate and manage auto vector embeddings for large tables \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:35.441964+00:00
---

# Generate and manage auto vector embeddings for large tables  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/generate-manage-auto-embeddings-for-tables/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Generate and manage auto vector embeddings for large tables Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/generate-manage-auto-embeddings-for-tables)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/ai/generate-manage-auto-embeddings-for-tables)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/ai/generate-manage-auto-embeddings-for-tables)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/ai/generate-manage-auto-embeddings-for-tables)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/generate-manage-auto-embeddings-for-tables)

You can generate and manage vector embeddings for an entire table column, which gives you a scalable solution for large-scale vector embedding creation. This solution is particularly useful for facilitating semantic search and Retrieval Augmented Generation (RAG) on text content, including the following: 

  * Creating initial vector embedding for a new table
  * Generating embeddings after a large data import
  * Refreshing embeddings after significant data changes
  * Maintaining embeddings incrementally



## Understand auto vector embeddings

Auto vector embeddings in AlloyDB Omni provide a scalable way to automate the generation and maintenance of vector embeddings for your data. Instead of manually generating embeddings for each new or updated piece of text, you can configure auto vector embeddings to handle this process for you. This is particularly useful for applications that rely on up-to-date embeddings for semantic search, Retrieval Augmented Generation (RAG), and other AI-powered features.

With auto vector embeddings, you can do the following:

  * Initialize embeddings for an entire table: generate embeddings for all existing data in a table column with a single command.
  * Keep embeddings in sync: automatically update embeddings when the source data changes, ensuring that your AI applications always work with the most current information.
  * Generate embeddings at scale: efficiently create embeddings for large tables with millions of rows.
  * Configure and manage embeddings for multiple columns in the same table by calling the management functions for each embedding column.



This feature simplifies the development and maintenance of AI applications by abstracting away the complexity of vector embedding creation and maintenance.

## Before you begin

**Note:** Auto vector embeddings are supported only for regular and partitioned PostgreSQL tables. They don't support temporary tables or unlogged tables.

Before you can generate and manage vector embeddings for large tables, follow these steps:

  * Check and increase Vertex AI quotas: To ensure optimal performance and avoid slow operations, low QPS, or multiple retries, verify and, if needed, increase your Vertex AI quotas.

To check and increase your quotas, follow these steps:

    1. In the Google Cloud console, go to the [**Quotas**](https://console.cloud.google.com/iam-admin/quotas) page.
    2. Filter for the following metrics relevant to your model and region: 
       * For requests per minute (RPM): `Regional online prediction requests per base model per minute per region per base_model`
       * For Gemini tokens: `Embed content input tokens per minute per region per base_model`
    3. If your current limits are insufficient for your table size, find the quota value that you want to update and select the checkbox next to the quota.
    4. Click **Edit**. The **Quota changes** dialog appears.

For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota)

For Vertex AI embedding model limits, see [Gemini embedding model token limit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/quotas#text-embedding-limits).

For a complete list of quotas, see [Vertex AI quotas and limits](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/quotas).

**Note:** Initial embedding generation for large tables (for example, millions of rows) might be throttled by default Vertex AI quotas, leading to low QPS and frequent retries. Increasing your quota upfront is the most effective way to ensure a fast, successful initialization.

\- [Connect to your database using `psql`](/alloydb/omni/linux/18.1.0/docs/run-connect) as the `postgres` user. \- Verify that the `google_ml_integration` extension is installed and its version is 1.5.6 or higher. \- Verify that the `google_ml_integration.enable_model_support` flag and `google_ml_integration.enable_faster_embedding_generation` flags are set to `on`. 

  * Before you can generate embeddings from an AlloyDB Omni database, you must configure AlloyDB Omni to work with Vertex AI. For more information, see [Integrate your database with Vertex AI](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-with-alloydb-ai).

  * For managing and monitoring auto embedding generation, users have `Select` access to the `google_ml.embed_gen_progress` and `google_ml.embed_gen_settings` tables by default.

To let a user manage auto embedding generation, grant `INSERT`, `UPDATE`, and `DELETE` permissions on the `google_ml.embed_gen_progress` and `google_ml.embed_gen_settings` tables:
        
        GRANT INSERT, UPDATE, DELETE ON google_ml.embed_gen_progress, google_ml.embed_gen_settings TO USER_NAME;
        

Replace the following:

    * USER_NAME: the name of the user for whom the permissions are granted.
  * Finish the initial setup described in [Generate text embeddings](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/work-with-embeddings?resource=google_ml#before-begin).

  * Verify that `AUTOCOMMIT` is set to `ON` in the PostgreSQL client that you use.




### Verify the extension version

To check the version of the `google_ml_integration` extension, run the following command:
    
    
    SELECT extversion FROM pg_extension WHERE extname = 'google_ml_integration';
    

If you need to update the extension, run the following command:
    
    
    ALTER EXTENSION google_ml_integration UPDATE;
    

**Note:** If you don't have the necessary permissions, contact your database administrator to perform the update. If the extension is not installed, see [Integrate your database with Vertex AI](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-with-alloydb-ai).

### Verify that the database flags are set to `on`

To verify that the database flags are set correctly, run the following commands:
    
    
    SHOW google_ml_integration.enable_model_support;
    SHOW google_ml_integration.enable_faster_embedding_generation;
    

If these flags are set to `off`, see [Configure database flags](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/configure-database-flags). For more information about these flags, see [Supported database flags](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/reference/alloydb-flags).

## Prepare your table

Before you can generate auto embeddings, you must create a column in your table to store the resulting vectors. This column typically uses the `vector(DIMENSION)` type and must have a `DEFAULT NULL` value.

For example, to add a column for 768-dimension embeddings to a table named `user_reviews`:
    
    
    ALTER TABLE user_reviews ADD COLUMN IF NOT EXISTS content_embeddings vector(768) DEFAULT NULL;
    

## Initialize embeddings for a table

The functions for managing auto vector embeddings are available in both the `ai` and `google_ml` schemas. The `ai` schema provides a simplified interface for the latest AI features in AlloyDB Omni.

Use the `ai.initialize_embeddings()` SQL function to generate embeddings for a table's content column. This is a blocking call, meaning the database session waits for the operation to complete before returning a result and allowing you to issue new commands in that session. However, other connections to the database are not blocked and can continue to work with the table:

  * If the function returns success, the vector embedding creation is complete.
  * The function automatically attempts to recover from transient issues like model quota errors. A failure returns to you only if these recovery attempts are unsuccessful. For persistent problems, such as a misconfigured `batch_size` that causes the request to exceed size limits, or if the operation was canceled manually, you must manually reissue the call.

**Note:** If the `ai.initialize_embeddings()` call fails, you must first clean up the configuration by using the `ai.drop_embedding_config()` procedure before you reissue the call—for example, `CALL ai.drop_embedding_config(table_name => 'my_table', embedding_column => 'content_embeddings');`.

This function supports Google-provided models—for example, the Vertex AI `text-embedding-005` model—as well as custom models that you registered.

## Perform batch generation

By default, AlloyDB Omni uses batching to generate embeddings for multiple text inputs in a single request, which improves efficiency. If you don't provide a specific batch size, AlloyDB Omni applies an automatically determined default value.

### Hint batch size

The `batch_size` parameter in `ai.initialize_embeddings` lets you guide the AlloyDB Omni query optimizer by suggesting a preferred batch size for directly supported models. AlloyDB Omni might dynamically reduce this size based on model limits or quotas, but your hint helps influence the query execution plan.
    
    
    CALL ai.initialize_embeddings(
        model_id => 'text-embedding-005',
        table_name => 'user_reviews',
        content_column => 'content',
        embedding_column => 'content_embeddings',
        batch_size => 50
    );
    

### Use a custom embedding model with batch support

If you want to use a custom or externally supported model that supports batching, define the batch transform functions and specify them as `model_batch_in_transform_fn` and `model_batch_out_transform_fn` when you create a model. You can also specify a `batch_size` in the `initialize_embeddings` call. For models that support batching, we recommend that you use a `batch_size` greater than 1 for better performance.

  1. Define your custom model's input, output, and batch transform functions.
         
         -- Scalar input transform functions
         CREATE OR REPLACE FUNCTION acme_text_input_transform(model_id TEXT, input TEXT) RETURNS JSON;
         CREATE OR REPLACE FUNCTION acme_text_output_transform(model_id TEXT, model_output JSON) RETURNS real[];
         CREATE OR REPLACE FUNCTION acme_generate_headers(model_id TEXT, input TEXT) RETURNS JSON;
         -- Batch input transform functions
         CREATE OR REPLACE FUNCTION acme_text_batch_input_transform(model_id TEXT, input TEXT[]) RETURNS JSON;
         CREATE OR REPLACE FUNCTION acme_text_batch_output_transform(model_id TEXT, model_output JSON) RETURNS real[][];
         

  2. To create your model, specify the batch transform functions.
         
         CALL
           ai.create_model(
             model_id => 'custom-embedding-model',
             model_request_url => 'https://acme.com/models/text/embeddings/v1',
             model_type => 'text_embedding',
             model_in_transform_fn => 'acme_text_input_transform',
             model_out_transform_fn => 'acme_text_output_transform',
             generate_headers_fn => 'acme_generate_headers',
             model_batch_in_transform_fn => 'acme_text_batch_input_transform',
             model_batch_out_transform_fn => 'acme_text_batch_output_transform'
           );
         

  3. Generate vector embeddings with your custom model.
         
         CALL
           ai.initialize_embeddings(
             model_id => 'custom-embedding-model',
             table_name => 'user_reviews',
             content_column => 'content',
             embedding_column => 'content_embeddings',
             batch_size => 10
         );
         




You can also use the auto embedding feature with custom models that don't natively support batching. To do this, you must still define the batch transform functions `model_batch_in_transform_fn` and `model_batch_out_transform_fn`. For a non-batching model, define these functions to process a single input at a time from the input array. When you call `ai.initialize_embeddings` for this model, set the `batch_size` to `1`.

### Use custom dimensionality with batch support

To use a custom batch input transform function with the `OUTPUT_DIMENSIONALITY` parameter, you can define a function that specifies the selected dimensions in the request parameters. This is useful for optimizing embedding generation for models that support variable output sizes.

For example, the following function defines a custom batch input transform for a model that requires an output dimensionality of 768:
    
    
    CREATE OR REPLACE FUNCTION google_ml.vertexai_text_embedding_batch_input_transform_with_768_dims(model_id VARCHAR(100), input_list TEXT[])
    RETURNS JSON
    LANGUAGE SQL
    AS $$
      SELECT pg_catalog.json_build_object(
        'instances',
        pg_catalog.json_agg(pg_catalog.json_build_object('content', content)),
        'parameters',
        pg_catalog.json_build_object('outputDimensionality', 768)
      ) FROM unnest(input_list) AS content;
    $$;
    

### Use JSONB optimization with custom models

You can use the `JSONB` data type in your custom output transform functions for improved performance. When you create a custom model with batch support, the `google_ml_integration` extension automatically looks for and uses a `JSONB` variant of your transform functions.

**Note:** This optimization applies only to batch output transform functions. Batch input transform functions continue to use the `JSON` data type.

This optimization can significantly improve the performance of auto embedding generation because `JSONB` is a more efficient binary format for storing and processing JSON data in PostgreSQL.

To take advantage of this feature, you need to provide another version of your transform function that accepts a `JSONB` argument instead of `JSON`.

For example, if you have a batch output transform function with the following signature:
    
    
    CREATE OR REPLACE FUNCTION my_batch_output_transform(model_id TEXT, model_output JSON) RETURNS real[][];
    

You can create a JSONB variant like this:
    
    
    CREATE OR REPLACE FUNCTION my_batch_output_transform(model_id TEXT, model_output JSONB) RETURNS real[][];
    

The extension automatically detects the presence of the `JSONB` version of the function and uses it for batch processing. If you already created a model registration that uses a `JSON` transform function, you don't need to update your `ai.create_model` call. As long as the new `JSONB` function uses the exact same name as the existing `JSON` function, the extension transparently detects and uses the `JSONB` variant for batch processing.

## Refresh embeddings incrementally

When you refresh an embedding, it is regenerated based on the latest value in the input content column.

To give you control over consistency and performance, AlloyDB Omni supports various modes for incremental embedding refreshes. You can select a mode using the `incremental_refresh_mode` enum argument in `ai.initialize_embeddings()`. The following is a list of possible modes:

  * `transactional`: embeddings refresh as part of the transaction updating the content column. This process, which often uses a mechanism similar to a database trigger to automatically generate embeddings when the content column is updated, can introduce overhead and slow down update operations. The introduced overhead is a trade-off for maintaining transactional semantics and ensuring that embeddings are in sync with the content. This mode relies on the scalar transform functions of your model, so you must define `model_in_transform_fn` and `model_out_transform_fn` when you create the model. To use the `transactional` mode, you must have the owner role on the table.
        
        CALL
          ai.initialize_embeddings(
            model_id => 'text-embedding-005',
            table_name => 'user_reviews',
            content_column => 'content',
            embedding_column => 'content_embeddings',
            batch_size => 10,
            incremental_refresh_mode => 'transactional'
        );
        

In `transactional` mode, the `ai.refresh_embeddings()` function is disabled because embeddings are kept in sync automatically using triggers. To regenerate embeddings for the entire table or to recover from an interrupted `ai.initialize_embeddings()` call in this mode, you must first drop the configuration using the `ai.drop_embedding_config()` function and then reissue the `ai.initialize_embeddings()` call.

This automated mode is useful for demos, small datasets, or tables where the volume of inserts and updates is low compared to the initial load, for example, a few hundred daily updates on a million-row table. It is appropriate when maintaining immediate data consistency is more important than the additional latency introduced during update operations.

  * `manual`: This is the default mode. In this mode, a new boolean tracking column is added to your table to track stale embeddings. Calling the `ai.refresh_embeddings()` function performs a periodic incremental refresh by only generating embeddings for new or updated rows. We recommend this mode for users who require more control over performance, especially when handling a large number of inserts or updates after the initial load. It is useful for scenarios where minimizing write latency is a priority and where having temporarily stale or null embeddings is acceptable until a periodic incremental refresh is triggered using `ai.refresh_embeddings`. To update stale or new rows, use the `ai.refresh_embeddings()` function as described in the Refresh all embeddings for a table section.




## Choose a refresh mode

The following table compares the two incremental refresh modes to help you choose the best approach for your application.

Mode | Description | Consistency and performance | Best for  
---|---|---|---  
`transactional` |  Embeddings are updated as part of the database transaction using a mechanism similar to a trigger. Note that `ai.refresh_embeddings()` is disabled in this mode.  |  **Immediate consistency.** High write latency overhead as each `INSERT` or `UPDATE` triggers an embedding generation.  |  Demos, small datasets, or tables where data consistency is critical.   
`manual` (default) |  Uses a boolean tracking column to monitor stale or new rows. You must call `ai.refresh_embeddings()` to trigger a periodic incremental refresh.  |  **Eventual consistency.** Minimal write latency as embeddings are generated in bulk at a time of your choosing.  |  Large datasets, production environments with high write frequency, or performance-sensitive applications.   
  
## Refresh all embeddings for a table

After you successfully run `ai.initialize_embeddings()` for a table using the `manual` incremental refresh mode, you can perform a periodic incremental refresh of your embeddings, which is triggered using `ai.refresh_embeddings`. You can use a refresh operation to update embeddings for rows that are modified concurrently during the initial `initialize_embeddings` call or to perform a periodic incremental refresh.

If the embedding creation process is interrupted in manual mode, for example, by `pg_cancel`, call the `ai.refresh_embeddings()` function to complete the generation for the remaining rows.

The refresh function reuses the settings from the initial call, so you only need to specify the table and embedding column. You can also provide an optional `batch_size` to override the default value.
    
    
    CALL ai.refresh_embeddings(
        table_name => 'user_reviews',
        embedding_column => 'content_embeddings',
        batch_size => 50  -- Optional override
    );
    

**Note:** If you encounter an error like `AutoEmbeddingGeneration: Request size is greater than 4MB`, it means the request size for a batch has exceeded the maximum supported size of 4MB. To resolve, reduce the `batch_size` value in your function call and retry.

## Work with table data during vector embedding creation

While `ai.initialize_embeddings()` is a blocking call for the session that it runs in, other connections can continue to work with the table. The auto vector embedding process updates rows in batches using standard row-level locking. This means that concurrent Data Modification Language (DML) operations — such as `UPDATE` or `DELETE` — from other connections are only briefly blocked if they attempt to modify the same rows targeted by the active embedding task. Non-modifying `SELECT` queries are not blocked.

### Delete auto vector embedding settings

If you need to remove the auto vector embedding configuration for a specific table and embedding column combination, use the `ai.drop_embedding_config()` function. This function can be useful for cleanup or when you reconfigure embedding management for a column.
    
    
    CALL
      ai.drop_embedding_config(
        table_name => 'user_reviews',
        embedding_column => 'content_embeddings');
    

## Work with partitioned tables

The auto vector embedding feature supports partitioned tables. This lets you manage embeddings for large, partitioned datasets efficiently. Here are the common use cases for working with partitioned tables.

### Initialize embeddings on a partitioned table

You can only initialize embeddings on the root partition of a table. This is a one-time operation for the entire partitioned table.
    
    
    CALL ai.initialize_embeddings(
        model_id => 'text-embedding-005',
        table_name => 'documents', -- This is the root partitioned table
        content_column => 'content',
        embedding_column => 'content_embeddings'
    );
    

### Refresh embeddings on a partitioned table

After initialization, you can refresh embeddings on any partition, including the root partition, sub-partitions, or individual leaf partitions. For large datasets, you can improve performance by refreshing embeddings for distinct partitions in parallel from different database connections:

  * To refresh the entire table, run the following:


    
    
    CALL ai.refresh_embeddings(
        table_name => 'documents', -- This is the root partitioned table
        embedding_column => 'content_embeddings'
    );
    

  * To refresh a single partition, run the following:


    
    
    CALL ai.refresh_embeddings(
        table_name => 'documents_eu',
        embedding_column => 'content_embeddings'
    );
    

### Refresh embeddings for newly added or attached partitions

The auto-embedding feature supports generating embeddings for partitions that are incorporated into your main table after the initial setup. The specific steps depend on whether you are adding a completely new partition or attaching a pre-existing table.

  * Newly added partition: if you add a new partition to the table, you can generate embeddings for it by calling `ai.refresh_embeddings` on the new partition.


    
    
    -- Add a new partition
    CREATE TABLE documents_africa PARTITION OF documents
        FOR VALUES IN ('africa');
    
    -- Refresh embeddings for the new partition
    CALL ai.refresh_embeddings(
        table_name => 'documents_africa',
        embedding_column => 'content_embeddings'
    );
    

  * Newly attached partition: to attach an existing table as a partition, first use the `ai.embedding_prepare_partition` procedure to ensure its schema is compatible with the partitioned table. The auto-embedding feature supports adding or attaching partitions at any level of a hierarchical partition setup. The `ai.embedding_prepare_partition` procedure ensures the schema is compatible with any parent table in the hierarchy.



To attach an existing table as a partition, first use the `ai.embedding_prepare_partition` procedure to ensure its schema is compatible with the partitioned table:
    
    
    -- Prepare the table to be attached
    CALL ai.embedding_prepare_partition(
        parent_table => 'documents',
        child_table => 'documents_misc'
    );
    
    -- Attach the partition
    ALTER TABLE documents ATTACH partition documents_misc DEFAULT;
    
    -- Refresh embeddings for the newly attached partition
    CALL ai.refresh_embeddings(
        table_name => 'documents_misc',
        embedding_column => 'content_embeddings'
    );
    

The auto-embedding feature supports adding or attaching partitions at any level of a hierarchical partition setup. The `ai.embedding_prepare_partition` procedure ensures the schema is compatible with any parent table in the hierarchy:
    
    
    -- Prepare a sub-partition for a non-root parent table
    CALL ai.embedding_prepare_partition(
        parent_table => 'documents_eu', -- An existing partition
        child_table => 'documents_eu_germany'
    );
    
    -- Attach the new sub-partition
    ALTER TABLE documents_eu ATTACH PARTITION documents_eu_germany
        FOR VALUES IN ('germany');
    
    -- Refresh embeddings for the new sub-partition
    CALL ai.refresh_embeddings(
        table_name => 'documents_eu_germany',
        embedding_column => 'content_embeddings'
    );
    

## Monitor embedding generation progress

You can monitor the real-time status of active `initialize_embeddings` and `refresh_embeddings` calls by querying the `ai.embedding_progress_view`. This view provides details on the progress of the operation, including the percentage completed, elapsed time, and estimated time remaining.

To check the progress, run the following query:
    
    
    SELECT
      table_name,
      content_column,
      embedding_column,
      model_id,
      percent_progress,
      status,
      elapsed_time,
      rows_processed,
      partition_root
    FROM
      ai.embedding_progress_view;
    

The view provides the following information:

Column | Description  
---|---  
`table_name` | The name of the table or partition being processed.  
`content_column` | The column containing the source content for the embedding.  
`embedding_column` | The column where the embeddings are being stored.  
`model_id` | The model being used for generation.  
`percent_progress` | The percentage of the operation that is complete.  
`status` | The current status of the operation (e.g., running, success).  
`elapsed_time` | The time that has passed since the operation began.  
`rows_processed` | The number of rows processed so far.  
`partition_root` | The name of the root partitioned table.  
  
## Examples for generating embeddings in auto

This section provides examples for generating embeddings in auto using registered model endpoints.

### OpenAI embedding model

To generate embeddings using the [registered `text-embedding-3-small` model endpoint](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/register-model-endpoint#add-openai) provided by OpenAI, run the following statement:
    
    
    CALL ai.initialize_embeddings(
        model_id => 'text-embedding-3-small',
        table_name => 'user_reviews',
        content_column => 'content',
        embedding_column => 'content_embeddings'
    );
    

### Custom embedding models

For your own or externally supported models, you must define input and output transform functions and register them with `ai.create_model`. If you plan to use the auto embedding feature, you must specify both scalar transform functions—for example, `acme_text_input_transform`, `acme_text_output_transform`—and batch transform functions—for example, `acme_text_batch_input_transform`, `acme_text_batch_output_transform`.

## What's next

* [Perform vector search](/alloydb/omni/linux/18.1.0/docs/ai/perform-vector-search). 

  * [Learn how to build a smart shopping assistant with AlloyDB Omni, pgvector, and model endpoint management](https://codelabs.developers.google.com/smart-shop-agent-alloydb#0).

* [Create indexes and query vectors](/alloydb/omni/linux/18.1.0/docs/ai/store-index-query-vectors). * Learn [an example embedding workflow](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/example-embeddings). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
