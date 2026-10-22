---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/example-embeddings/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:17.932800+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/example-embeddings/




Stay organized with collections  Save and categorize content based on your preferences. 

1 

An example embedding workflow Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/example-embeddings)

This page provides an example workflow that demonstrates how [the `embedding()` function](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/work-with-embeddings) works together with your table-stored data and `pgvector` feature. The example uses plain-text input to fetch a result from a database that relies on large language model (LLM)-driven semantic parsing of the text's meaning. 

## An example scenario

Imagine a database running on AlloyDB with the following aspects:

  * The database contains a table, `items`. Each row in this table describes an item that your business sells.

  * The `items` table contains a column, `complaints`. This `TEXT` column stores buyer complaints logged about each item.

  * The database integrates with the Vertex AI Model Garden, giving it access to the `textembedding-gecko` English models.




Even though this database stores complaints about items, these complaints are stored as plain text, making it challenging to query. For example, if you want to see which items have the most complaints from customers who received the wrong color of merchandise, then you can perform ordinary SQL queries on the table, looking for various keyword matches. However, this approach only matches rows that contain those exact keywords.

For example, a basic SQL query such as `SELECT * FROM item WHERE complaints LIKE "%wrong color%"` doesn't return a row whose `complaints` field contains only `The picture shows a blue one, but the one I received was red`.

SQL queries using LLM-powered embeddings can help bridge this gap. By applying embeddings, you can query the table in this example for items whose complaints have semantic similarity to a given text prompt, such as "It was the wrong color".

The following steps show how to enable this in the example setup described earlier.

## Before you begin

Make sure that you meet the following requirements:

#### Required database extension

  * Ensure that the following extensions are installed on your AlloyDB database.

    * `google_ml_integration` extension

    * `vector` extension, version `0.5.0.google-1` or later




For more information about installing and managing extensions, see [Configure database extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions).

  * Set the `google_ml_integration.enable_model_support` database flag to `off`.



#### Set up model access

Before you can generate embeddings from an AlloyDB database, you must configure AlloyDB to work with a text embedding model.

To work with the cloud-based `textembeddings-gecko` model, you need to [integrate your database with with Vertex AI](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install-with-alloydb-ai).

## Prepare the table

Before you run LLM-based queries on the `items` table's content, you must prepare the table to store and index embeddings based on your existing data.

### Create a column to store embeddings

Add a column to the table for storing embeddings.
    
    
    ALTER TABLE items ADD COLUMN complaint_embedding vector(768);
    

This example specifies `768` as an argument, because that is the number of dimensions supported by the `textembedding-gecko` English models. For more information, see [Generate an embedding](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/work-with-embeddings).

The example applies the `vector` data type to the column for ease of using `pgvector` functions and operators with its values.

### Populate the new column

If you already have embeddings in `CSV` format, follow the steps in [Store vector embeddings](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/store-embeddings) to store your embeddings.

Optionally, use the `embedding()` function to populate this new column with embeddings in case you have text stored in the`complaints` column. In this example setup, AlloyDB generates the embeddings using the `textembedding-gecko` model, version `003`.
    
    
    UPDATE items SET complaint_embedding = embedding('textembedding-gecko@003', complaints);
    

This example implicitly casts the `real[]` return value of `embedding()` into a `vector` value, in order to store the value into the `vector` column created earlier.

### Create an index

To improve performance, add an index to `items` that uses the scalar-quantization techniques.
    
    
    CREATE INDEX complaint_embed_idx ON items
      USING ivf (complaint_embedding vector_l2_ops)
      WITH (lists = 20, quantizer = 'SQ8');
    

For more information on creating approximate nearest-neighbor indexes, see [Indexing](https://github.com/pgvector/pgvector#indexing).

## Run LLM-powered queries with provided text

You can now make semantic nearest-neighbor queries on the `items` table. The following query uses the `<->` operator provided by `pgvector` to sort the table's rows on semantic proximity to the text `It was the wrong color` and return the top ten complaints. The query displays the `id` and `name` values of the first sorted row.
    
    
    SELECT id, name FROM items
      ORDER BY complaint_embedding::vector
      <-> embedding('textembedding-gecko@003', 'It was the wrong color') LIMIT 10;
    

## What's next

  * For another example workflow involving AlloyDB and `pgvector`, see [Building AI-powered apps on Google Cloud databases using pgvector, LLMs and LangChain](https://cloud.google.com/blog/products/databases/using-pgvector-llms-and-langchain-with-google-cloud-databases).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
