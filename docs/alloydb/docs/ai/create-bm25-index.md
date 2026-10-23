---
url: https://docs.cloud.google.com/alloydb/docs/ai/create-bm25-index/
title: Create and manage a BM25 index \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:36.941971+00:00
---

# Create and manage a BM25 index  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/create-bm25-index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Create and manage a BM25 index Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BM25 index**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Best Matching 25 (BM25) indexes in AlloyDB for PostgreSQL let you optimize full-text search queries with high-accuracy relevance ranking. You can enable the `pg_textsearch` extension to create BM25 indexes, rank search results, configure term frequency saturation parameters, and tune document length normalization weights.

BM25 is a probabilistic ranking algorithm widely used to estimate how relevant a document is to a given query. It evaluates Term Frequency (TF), Inverse Document Frequency (IDF), and Document Length Normalization to offer more accurate search rankings than standard text search.

## Before you begin

To use a BM25 index, you must enable the `pg_textsearch` extension and meet the following requirements:

  * Use PostgreSQL 17 or 18: the `pg_textsearch` extension is supported only on AlloyDB instances running PostgreSQL major version 17 or 18.
  * Database role: you must have the [`alloydbsuperuser` database role](https://docs.cloud.google.com/alloydb/docs/database-users/overview#alloydbsuperuser). For more information, see [Add an Identity and Access Management (IAM) user or service account to a cluster](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth#create-user).



### Enable the `pg_textsearch` extension

You must enable the `pg_textsearch` extension for each database:

  1. Connect to your AlloyDB database using `psql` or another client. For more information, see [Connect to a cluster instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).
  2. Run the following SQL command to create the extension:
         
         CREATE EXTENSION IF NOT EXISTS pg_textsearch;
         




## Create a BM25 index

The following example creates a table named `documents` with a content `column` to index text data for BM25 similarity queries.

  1. Create a table named `documents`:
         
         CREATE TABLE documents (
           id SERIAL PRIMARY KEY,
           title TEXT NOT NULL,
           content TEXT NOT NULL
         );
         

  2. Populate the table with sample data:
         
         INSERT INTO documents (title, content) VALUES
           ('Database systems', 'AlloyDB is a fully managed PostgreSQL-compatible database service'),
           ('Google Cloud FTS', 'Full-text search lets you identify natural-language documents'),
           ('Probabilistic Ranking', 'BM25 uses term frequency and document length normalization');
         

  3. Create a BM25 index on the `content` column:
         
         CREATE INDEX idx_docs_bm25
         ON documents
         USING bm25 (content)
         WITH (text_config = 'english');
         




The index supports three parameters in its `WITH` clause:

  * `text_config` (Required): The PostgreSQL text search configuration to use (for example, `english`).
  * `k1` (Optional): The term frequency saturation parameter. The default value is `1.2`.
  * `b` (Optional): The document length normalization parameter. The default value is `0.75`.



## Query using a BM25 index

To perform relevance ranking against a BM25 index, use the `<@>` operator.

The `<@>` operator returns a negative BM25 score. This is because PostgreSQL only supports ascending (`ASC`) index scans on operators. A lower (more negative) score indicates a stronger relevance match.

Run a search query sorted by BM25 score in ascending order:
    
    
    SELECT title, content, content <@> 'database system' AS score
    FROM documents
    ORDER BY content <@> 'database system' ASC
    LIMIT 5;
    

The output shows the highly relevant document at the top with the lowest negative score:
    
    
          title       |                            content                                   |  score
    ------------------+----------------------------------------------------------------------+----------
     Database systems | AlloyDB is a fully managed PostgreSQL-compatible database service    | -0.9971461892127991
     Google Cloud FTS | Full-text search lets you identify natural-language documents        | 0
     Probabilistic ranking | BM25 uses term frequency and document length normalization      | 0
    (3 rows)
    

## Tune BM25 index parameters

You can adjust parameters to optimize ranking for different types of document collections.

  * Increase `k1`: If you want query terms repeated multiple times to consistently increase a document's score.
  * Increase `b`: If you want longer documents to be penalized more heavily for including miscellaneous terms.



To create an index customized for short documents prioritizing term frequency, set `k1` to `1.5` and `b` to `0.8`:
    
    
    CREATE INDEX idx_docs_bm25_tuned
    ON documents
    USING bm25 (content)
    WITH (text_config = 'english', k1 = 1.5, b = 0.8);
    

## What's next

  * Learn about [full-text search](https://docs.cloud.google.com/alloydb/docs/ai/full-text-search-overview).
  * Learn how to [Run a hybrid vector similarity search](https://docs.cloud.google.com/alloydb/docs/ai/run-hybrid-vector-similarity-search).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
