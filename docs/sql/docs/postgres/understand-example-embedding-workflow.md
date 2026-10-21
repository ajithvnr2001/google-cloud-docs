---
url: https://docs.cloud.google.com/sql/docs/postgres/understand-example-embedding-workflow/
title: Understand an example of an embedding workflow \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:23.478473+00:00
---

# Understand an example of an embedding workflow  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/understand-example-embedding-workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Understand an example of an embedding workflow Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/understand-example-embedding-workflow "View this page for the MySQL database engine") | PostgreSQL | SQL Server

This page provides an example of a workflow that demonstrates how the [`embedding()`](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors#generate-an-embedding) function works with the data that's stored in your tables and the [`pgvector` query functionality](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors#query). The example uses plain-text input to fetch a result from a database that relies on large language model (LLM)-driven semantic parsing of the text's meaning.

## An example scenario of an embedding workflow

Imagine a database running on Cloud SQL for PostgreSQL with the following aspects:

  * The database contains a table: `items`. Each row in this table describes an item that your business sells.

  * The `items` table contains a column: `complaints`. This column stores buyer complaints that are logged about each item as plain text.

  * The database integrates with the [Vertex AI Model Garden](https://cloud.google.com/model-garden), giving it access to the `gemini-embedding` LLM.




Even though this database stores complaints about items, these complaints are stored as plain text, making it challenging to query. For example, if you want to see which items have the most complaints from customers who received the wrong color of merchandise, then you can perform ordinary SQL queries on the table, looking for various keyword matches. However, this approach matches only rows that contain those exact keywords.

For example, a basic SQL query such as `SELECT * FROM item WHERE complaints LIKE "%wrong color%"` doesn't return a row where the `complaints` field contains only `The picture shows a blue one, but the one I received was red`.

SQL queries using LLM-powered embeddings can help bridge this gap. By applying embeddings, you can query the table in this example for items where complaints have semantic similarity to a given text prompt, such as "It was the wrong color".

The following steps show how to enable this in the example scenario described earlier.

## Prepare the table

Before you run LLM-based queries on the content of the `items` table, you must prepare the table to store and index embeddings based on your existing data.

### Create a column to store embeddings

Add a column to the table to store embeddings.

`sql ALTER TABLE items ADD COLUMN complaint_embedding vector(3072);`

This example specifies `3072` as an argument because that's how many dimensions the `gemini-embedding` LLM supports. For more information, see [Generate an embedding](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors#generate-an-embedding).

The example applies the `vector` data type to the column to simplify using `pgvector` functions and operators with the column's values.

### Populate the new column

Use the `embedding()`function to populate this new column with embeddings based on the value of each row's text that appears in the `complaints` column. In this example, Cloud SQL generates the embeddings using the LLM with the ID of `gemini-embedding`, version `001`.
    
    
    UPDATE items SET complaint_embedding = embedding('gemini-embedding-001', complaints);
    

This example casts the `real[]` return value of `embedding()` into a `vector` value implicitly to store the value in the `vector` column that you created in Create a column to store embeddings. 

### Create an index

To improve performance, add an index to the `items` table.
    
    
    CREATE INDEX complaint_embed_idx ON items
      USING hnsw (complaint_embedding vector_cosine_ops);
    

For more information on creating this type of index, see [Create a nearest-neighbor index](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors#index). Also, for more information on tuning the index by setting parameters, see [Query and index embeddings using `pgvector`](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors).

## Run LLM-powered queries with provided text

You can now make semantic nearest-neighbor queries on the `items` table. The following query uses the `<->` operator that `pgvector` provides to complete the following actions:

  * Sort the table's rows on semantic proximity to the text of `It was the wrong color`.
  * Return the top ten complaints.



The query displays the `id` and `name` values of the first sorted row.
    
    
    SELECT id, name FROM items
      ORDER BY complaint_embedding
      <-> embedding('gemini-embedding-001', 'It was the wrong color')::vector LIMIT 10;
    

## What's next

  * [Build generative AI applications using Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/ai-overview)

  * [Integrate Cloud SQL with Vertex AI](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai)

  * [Work with vector embeddings](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors)

  * [Invoke online predictions from Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/invoke-online-predictions)

  * [Build LLM-powered applications using LangChain](https://docs.cloud.google.com/sql/docs/postgres/langchain)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
