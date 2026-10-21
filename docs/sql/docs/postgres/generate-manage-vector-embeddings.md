---
url: https://docs.cloud.google.com/sql/docs/postgres/generate-manage-vector-embeddings/
title: Generate and manage vector embeddings \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:11.132755+00:00
---

# Generate and manage vector embeddings  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/generate-manage-vector-embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Generate and manage vector embeddings Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings "View this page for the MySQL database engine") | PostgreSQL | SQL Server

This page describes how to generate and store vector embeddings based on a model.

For more information, see [Build generative AI applications using Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/ai-overview).

Cloud SQL lets you use an embedding model hosted by Vertex AI to translate a text string into an _embedding_ , which is the model's representation of the given text's semantic meaning as a numeric vector.

Cloud SQL implements embeddings as arrays of `real` values. You can use generated embeddings as inputs for `pgvector` extension functions.

## Before you begin

Some requirements differ depending on whether you want to use Cloud SQL to generate embeddings, or whether you only need to work with embeddings that are stored in your database from another source.

### Regional restrictions

To generate Vertex AI embeddings with Cloud SQL, your instance must reside in a region where [generative AI foundational models are supported](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#available-regions). The Vertex AI models that Cloud SQL can use for embeddings, `text-embedding` and `gemini-embedding`, are located in that region.

**Note:** This restriction doesn't prevent Cloud SQL instances from integrating with Vertex AI, no matter where those instances are located.

### Required database extensions

To work with embeddings, install the [`google_ml_integration`](https://docs.cloud.google.com/sql/docs/postgres/extensions#miscellaneous-extensions) extension on your Cloud SQL instance. For Vertex AI models, install version `1.2` or later. For third-party or custom models, install version `1.4.2` or later.

Optionally, if you want to store these embeddings, and use vector functions and operators with the embeddings, then you also need the [`pgvector`](https://github.com/pgvector/pgvector) extension.

Cloud SQL has both of these extensions. You can install them on any database in your instance. For more information, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

**Note:** Refer to `pgvector` as `vector` in SQL commands, including the `CREATE EXTENSION` command when you install the extensions. For more information, see [Getting started](https://github.com/pgvector/pgvector#getting-started).

### Set up model access

Before you can generate embeddings from a Cloud SQL instance, you must configure Cloud SQL to work with a text embedding model.

To work with the cloud-based `text-embedding` or `gemini-embedding` model, you need to [integrate Cloud SQL with Vertex AI](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai).

### Grant database users access to generate embeddings

Grant permission for database users to use the `embedding` function to run predictions:

  1. Connect a `psql` client to the primary instance, as described in [Connect using a psql client](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip).

  2. At the `psql` command prompt, connect to the database and grant permissions:
         
         \c DB_NAME
         
         GRANT EXECUTE ON FUNCTION embedding TO USER_NAME;
         

Replace the following:

     * DB_NAME: the name of the database for which you're granting permissions

     * USER_NAME: the name of the user for whom you're granting permissions




## Generate embeddings

Cloud SQL provides a function that lets you translate text into a vector embedding. You can then store that embedding in your database as vector data, and optionally use `pgvector` functions to run queries on it.

### Generate an embedding

To generate an embedding using Cloud SQL, use the `embedding` function that the `google_ml_integration` extension provides:
    
    
    SELECT embedding( 'MODEL_ID_WITH_VERSION', 'TEXT');
    

Make the following replacements:

  * MODEL_ID_WITH_VERSION: the fully qualified ID of the model to query.

If you're using the [Vertex AI Model Garden](https://cloud.google.com/model-garden), then specify `text-embedding-004` or   
`text-multilingual-embedding-002`. These are the cloud-based models that Cloud SQL can use for text embeddings. For more information, see [Text embeddings](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings).

Cloud SQL strongly recommends that you avoid specifying a model without a version.
  * TEXT: the text to translate into a vector embedding.




The following example uses the `text-embedding-004` model to generate an embedding based on a provided literal string:
    
    
    SELECT embedding( 'text-embedding-004', 'Cloud SQL is a managed, cloud-hosted SQL database service.');
    

### Store a generated embedding

The return value of the `embedding()` function is an array of `real` values. To store this value in a table, add a `real[]` column:
    
    
    ALTER TABLE TABLE ADD COLUMN EMBEDDING_COLUMN real[DIMENSIONS];
    

Make the following replacements:

  * TABLE: the table name

  * EMBEDDING_COLUMN: the name of the new embedding column

  * DIMENSIONS: the number of dimensions that the model supports.

If you're using one of the `text-embedding` models with Vertex AI, then specify `768`.




Optionally, if you have installed the `pgvector` extension, then you can store embeddings as `vector` values:
    
    
    ALTER TABLE TABLE ADD COLUMN EMBEDDING_COLUMN vector(DIMENSIONS);
    

After you create a column to store embeddings, you can populate it based on the values already stored in another column in the same table:
    
    
    UPDATE TABLE SET EMBEDDING_COLUMN = embedding('MODEL_ID_WITH_VERSION', SOURCE_TEXT_COLUMN);
    

Make the following replacements:

  * TABLE: the table name.

  * EMBEDDING_COLUMN: the name of the embedding column.

  * MODEL_ID_WITH_VERSION: the fully qualified ID of the model to query.

If you're using the [Vertex AI Model Garden](https://cloud.google.com/model-garden), then specify `text-embedding-004` or   
`text-multilingual-embedding-002`. These are the cloud-based models that Cloud SQL can use for text embeddings. For more information, see [Text embeddings](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings).

Cloud SQL strongly recommends that you avoid specifying a model without a version.
  * SOURCE_TEXT_COLUMN: the name of the column that's storing the text. You translate this text into embeddings.




The previous command works for both `real[]` and `vector` embedding columns. If your embedding column is of the `vector` type, then Cloud SQL casts the return value of `embedding()` from a `real` array to a `vector` value implicitly.

The following example uses the `text-embedding-004` model to populate the `messages.message_vector` column with embeddings based on the content of the `messages.message` column:
    
    
    UPDATE messages SET message_vector = embedding( 'text-embedding-004', message);
    

## Query and index embeddings using `pgvector`

The `pgvector` PostgreSQL extension lets you use vector-specific operators and functions when you store, index, and query text embeddings in your database. Cloud SQL has its own optimizations for working with `pgvector`, letting you create indexes that can speed up queries that involve embeddings.

### Create a nearest-neighbor index

`pgvector` supports approximate nearest-neighbor (ANN) searches through [indexing](https://github.com/pgvector/pgvector#indexing).

To create an `HNSW` index, use the [`hnsw`](https://github.com/pgvector/pgvector#hnsw) function, as shown in the following example:
    
    
    CREATE INDEX ON TABLE
      USING hnsw (EMBEDDING_COLUMN DISTANCE_FUNCTION)
      WITH (m = M, ef_construction = EF_CONSTRUCTION);
    

Make the following replacements:

  * TABLE: the table to which you're adding the index.

  * EMBEDDING_COLUMN: a column that stores `vector` data.

  * DISTANCE_FUNCTION: the distance function to use with this index. Choose one of the following:

    * **L2 distance** : `vector_l2_ops`

    * **Inner product** : `vector_ip_ops`

    * **Cosine distance** : `vector_cosine_ops`

  * M (optional): the maximum number of connections with neighboring data points in a graph. We recommend a range of 5 to 48. The default is 16.

  * EF_CONSTRUCTION (optional): the size of the list that holds the closest candidates during the graph traversal when building the index. Higher values lead the algorithm to consider more candidates, allowing a better index to be created. The default size is 64.




To create this index on an embedding column that uses the `real[]` data type instead of `vector`, cast the column into the `vector` data type:
    
    
    CREATE INDEX ON TABLE
      USING hnsw ((CAST(EMBEDDING_COLUMN AS vector(DIMENSIONS))) DISTANCE_FUNCTION)
      WITH (m = M, ef_construction = EF_CONSTRUCTION);
    

Replace DIMENSIONS with the dimensional width of the embedding column.

The next section demonstrates an example of this kind of index.

### Make a nearest-neighbor query with given text

After you store and index embeddings in your database, the full range of [`pgvector` query functionality](https://github.com/pgvector/pgvector#querying) is available to you.

To find the nearest semantic neighbors to a piece of text, use the `embedding()` function to translate the text into a vector. In the same query, apply this vector to the `pgvector` nearest-neighbor operator, `<->`, to find the database rows with the most semantically similar embeddings.

Because `embedding()` returns a `real` array, you must cast the `embedding()` call to `vector` to use these values with `pgvector` operators.
    
    
      SELECT RESULT_COLUMNS FROM TABLE
        ORDER BY EMBEDDING_COLUMN
        <-> embedding('MODEL_ID_WITH_VERSION', 'TEXT')::vector
        LIMIT ROW_COUNT
    

Make the following replacements:

  * RESULT_COLUMNS: the columns to display from semantically similar rows.

  * TABLE: the table containing the embedding to which you compare the text.

  * EMBEDDING_COLUMN: the column containing the stored embeddings.

  * MODEL_ID_WITH_VERSION: the fully qualified ID of the model to query.

If you're using the [Vertex AI Model Garden](https://cloud.google.com/model-garden), then specify `text-embedding-004` or   
`text-embedding-multilingual-002`. These are the cloud-based models that Cloud SQL can use for text embeddings. For more information, see [Text embeddings](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings).

Cloud SQL strongly recommends that you avoid specifying a model without a version.
  * TEXT: the text that you want so that you can find the nearest stored semantic neighbors.

  * ROW_COUNT: the number of rows to return. If you want only the single best match, then specify `1` as the value for this parameter.




To run this query with a stored embedding column that uses the `real[]` data type instead of `vector`, cast the column into the `vector` data type:
    
    
      SELECT RESULT_COLUMNS FROM TABLE
        ORDER BY EMBEDDING_COLUMN::vector
        <-> embedding('MODEL_ID_WITH_VERSION', 'TEXT')::vector
        LIMIT ROW_COUNT
    

## Fully qualify the model ID to avoid errors

**Caution:** To avoid inconsistent results from the `embedding()` function, always specify a stable embeddings model, including a version.

Cloud SQL strongly recommends that you always use a stable version of your chosen embeddings model. For most models, this means setting a version explicitly. For example, use `gemini-embedding-001` instead of `gemini-embedding`.

Calling the `embedding()` function without specifying the version of the model is valid syntactically, but it [isn't stable and can be prone to error](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/text-embeddings-api#model_versions).

For more information about available Vertex AI model versions, see [Latest stable models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions#latest-stable).

A given Vertex AI model version always returns the same `embedding()` response to a given text input. If you don't specify the model version in your embedding calls, then it's possible that a newly published model version could abruptly change the returned vector for a given input. This can cause errors or other unexpected behavior in your applications.

## What's next

  * [Build generative AI applications using Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/ai-overview)
  * [Integrate Cloud SQL with Vertex AI](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai)
  * [Invoke online predictions from Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/invoke-online-predictions)
  * [Understand an example of an embedding workflow](https://docs.cloud.google.com/sql/docs/postgres/understand-example-embedding-workflow)
  * [Build LLM-powered applications using LangChain](https://docs.cloud.google.com/sql/docs/postgres/langchain)
  * [Manage your data using Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio)
  * [Write SQL with Gemini assistance](https://docs.cloud.google.com/sql/docs/postgres/write-sql-gemini)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
