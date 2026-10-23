---
url: https://docs.cloud.google.com/alloydb/docs/ai/create-rum-index/
title: Create and manage RUM index \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:35.945423+00:00
---

# Create and manage RUM index  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/create-rum-index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Create and manage RUM index Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — RUM index**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

RUM indexes in AlloyDB for PostgreSQL let you accelerate full-text search queries by storing positional and attribute information alongside lexemes in the index. You can enable the `rum` extension to create RUM indexes and optimize relevance ranking, phrase searches, and timestamp-based sorting.

## Before you begin

To create the RUM extension, you must have the [`alloydbsuperuser` database role](https://docs.cloud.google.com/alloydb/docs/database-users/overview#alloydbsuperuser).

The AlloyDB Admin ([`roles/alloydb.admin`](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles)) Identity and Access Management (IAM) role grants full control over AlloyDB resources, but it doesn't grant the `alloydbsuperuser` database role. To create the extension, an administrator must explicitly grant you the `alloydbsuperuser` database role.

For more information about granting roles, see [Add an IAM user or service account to a cluster](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth#create-user).

## Create the RUM extension

You must create the RUM extension once per database.

  1. Connect to your AlloyDB database using `psql` or another client. For more information, see [Connect to a cluster instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).
  2. Run the following SQL command to create the extension:
         
         CREATE EXTENSION IF NOT EXISTS rum;
         




## Create a RUM index

To optimize full-text search queries, create a RUM index on your data. RUM offers several operator classes for different use cases.

### Types of RUM operator classes

The following table summarizes the different RUM operator classes and their primary use cases.

Operator Class | Main Use Case | Limitations  
---|---|---  
`rum_tsvector_ops` | Standard full-text search with ranking and phrase search. | N/A  
`rum_tsvector_hash_ops` | Smaller index and faster updates for full-text search. | Does not support prefix searching.  
`rum_tsvector_addon_ops` | Full-text search sorted by another column. | N/A  
`rum_anyarray_ops` | Searching within array columns. | N/A  
`rum_<TYPE>_ops` | Indexing scalar types for distance-based queries. | N/A  
`rum_tsvector_hash_addon_ops` | Hash-based full-text search sorted by another column. | Does not support prefix matching.  
`rum_tsquery_ops` | Indexing stored `tsquery` values for reverse search. | N/A  
`rum_anyarray_addon_ops` | Array search sorted by another column. | N/A  
  
### Index for basic full-text search

Use the `rum_tsvector_ops` operator class for standard text search that requires fast ranking and phrase search capabilities. This operator class stores the position of each lexeme in the index. The following example creates a table named `documents` with a `content` column.

  1. Create a table named `documents`:
         
         CREATE TABLE documents (
           id SERIAL PRIMARY KEY,
           title TEXT NOT NULL,
           content TEXT NOT NULL,
           published_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
         );
         

  2. Populate the `documents` table with sample data:
         
         INSERT INTO documents (title, content) VALUES
           ('Title', 'This search engine is working as intended');
         

  3. Add a generated `tsvector` column to your table. This column automatically stores the processed text and improves query performance:
         
         ALTER TABLE documents
         ADD COLUMN search_vector tsvector
         GENERATED ALWAYS AS (to_tsvector('english', content)) STORED;
         

  4. Create the RUM index on the new `search_vector` column:
         
         CREATE INDEX idx_docs_rum
         ON documents
         USING rum (search_vector rum_tsvector_ops);
         

  5. Query the table using the index. The `<=>` operator computes the relevance score, or distance, between the document and the query directly from the index, enabling fast sorting:
         
         SELECT title, content
         FROM documents
         WHERE search_vector @@ to_tsquery('english', 'search <-> engine')
         ORDER BY search_vector <=> to_tsquery('english', 'search <-> engine');
         

  6. Populate `documents` table with more data:
         
         INSERT INTO documents (title, content) VALUES ('Title1', 'English is my primary language.');
         INSERT INTO documents (title, content) VALUES ('Title2', 'Google has a great engineering culture');
         

  7. Run a prefix search query. This finds documents containing words that start with `eng`, such as `engineer` or `english`:
         
         SELECT title, content
         FROM documents
         WHERE search_vector @@ to_tsquery('english', 'eng:*');
         




### Index for optimized hash search

Use the `rum_tsvector_hash_ops` operator class to reduce index size and improve update speeds. This class stores a hash of each lexeme instead of the full lexeme. This approach results in a smaller index but does not support prefix searching. The following example assumes that you have a table named `documents` with a `search_vector` column.

  1. Create the RUM index using the hash operator class:
         
         CREATE INDEX idx_docs_rum_hash
         ON documents
         USING rum (search_vector rum_tsvector_hash_ops);
         

  2. Populate `documents` table with more data:
         
         INSERT INTO documents (title, content) VALUES ('Title3', 'That person was driving incredibly fast, however the routing was not very efficient');
         

  3. Run a standard match query:
         
         SELECT * FROM documents WHERE search_vector @@ to_tsquery('english', 'fast & efficient');
         
         




### Index for search sorted by timestamp

Use the `rum_tsvector_addon_ops` operator class to optimize queries that filter by text and sort by another field, such as a timestamp. This pattern stores the additional field's value directly in the index, which avoids a slow sort operation after the search. The following example assumes that you have a table named `documents` with a `search_vector` column and a `published_at` column.

  1. Create an index that includes the `published_at` timestamp:
         
         CREATE INDEX idx_docs_rum_timestamp
         ON documents
         USING rum (search_vector rum_tsvector_addon_ops, published_at)
         WITH (attach = 'published_at', to = 'search_vector');
         

  2. Run a query that finds documents containing the word `engine` and sorts them by publication date. The index handles both the search and the sort efficiently:
         
         SELECT title, published_at
         FROM documents
         WHERE search_vector @@ to_tsquery('english', 'engine')
         ORDER BY published_at DESC;
         




### Index for array search

Use the `rum_anyarray_ops` operator class to index array columns, such as a list of tags. This lets you efficiently query for arrays that overlap (`&&`), contain (`@>`), or are contained by (`<@`) other arrays. The following example adds a `tags` column to the `documents` table.

  1. Add a `tags` column and populate it with data:
         
         ALTER TABLE documents 
         ADD COLUMN tags TEXT[];
         
         INSERT INTO documents (title, content, tags) VALUES ( 'Title4', 'Sample Text', ARRAY['ai', 'ml'] );
         

  2. Create the RUM index on a `TEXT[]` column named `tags`:
         
         CREATE INDEX idx_tags_rum
         ON documents
         USING rum (tags rum_anyarray_ops);
         

  3. Run a query to find documents that have either `ai` or `ml` in their tags:
         
         SELECT * FROM documents WHERE tags && '{"ai", "ml"}';
         




### Index for scalar types

Use the `rum_<TYPE>_ops` operator classes to index columns that contain continuous values, such as integers, timestamps, or floating-point numbers. These operator classes let you use the `<=>` operator to efficiently calculate the distance between values. The following example assumes that you have a table named `documents`.

  1. Add a generic integer column, such as `rating`, to the `documents` table:
         
         ALTER TABLE documents
         ADD COLUMN rating INT;
         
         UPDATE documents 
         SET rating = floor(random() * 5 + 1);
         

  2. Create a RUM index on the `rating` column:
         
         CREATE INDEX idx_rating_rum
         ON documents
         USING rum (rating rum_int4_ops);
         

  3. Run a query to find documents with a `rating` closest to the value 5:
         
         SELECT title, rating
         FROM documents
         ORDER BY rating <=> 5;
         




### Index for optimized hash search sorted by timestamp

Use the `rum_tsvector_hash_addon_ops` operator class to combine the benefits of a hash index with the sorting capabilities of an addon index. This class stores a hash of each lexeme along with the value of an additional column. This configuration supports efficient sorting by the additional column but does not support prefix matching. The following example assumes that you have a table named `documents` with a `search_vector` column and a `published_at` timestamp column.

  1. Create a RUM index that uses the hash operator class and includes the `published_at` timestamp:
         
         CREATE INDEX idx_docs_rum_hash_timestamp
         ON documents
         USING rum (search_vector rum_tsvector_hash_addon_ops, published_at)
         WITH (attach = 'published_at', to = 'search_vector');
         

  2. Run a query that finds documents containing `engine` and sorts them by publication date:
         
         SELECT title, published_at
         FROM documents
         WHERE search_vector @@ to_tsquery('english', 'engine')
         ORDER BY published_at DESC;
         




### Index for stored queries

Use the `rum_tsquery_ops` operator class to index `tsquery` values. This lets you perform "reverse search," identifying which stored queries match a given input document. The following example creates a table named `queries`.

  1. Create a table to store queries:
         
         CREATE TABLE queries (
         query_text tsquery
         );
         INSERT INTO queries (query_text) VALUES (plainto_tsquery('AlloyDB is fast!'));
         

  2. Create a RUM index on the `query_text` column:
         
         CREATE INDEX idx_queries_rum
         ON queries
         USING rum (query_text rum_tsquery_ops);
         

  3. Run a query to find stored queries that match a document:
         
         SELECT *
         FROM queries
         WHERE to_tsvector('english', 'AlloyDB is fast') @@ query_text;
         




### Index for array search sorted by timestamp

Use the `rum_anyarray_addon_ops` operator class to index array columns along with an additional column for sorting. The following example assumes that you have a table named `documents` with a `tags` column and a `published_at` timestamp column.

  1. Create a RUM index on the `tags` column that includes the `published_at` timestamp:
         
         CREATE INDEX idx_tags_rum_timestamp
         ON documents
         USING rum (tags rum_anyarray_addon_ops, published_at)
         WITH (attach = 'published_at', to = 'tags');
         

  2. Run a query to find documents with the `ai` tag, sorted by publication date:
         
         SELECT title, published_at
         FROM documents
         WHERE tags @> '{"ai"}'
         ORDER BY published_at DESC;
         




## What's next

  * Learn about [Full-text search](https://docs.cloud.google.com/alloydb/docs/ai/full-text-search-overview).
  * Learn how to [Run a hybrid vector similarity search](https://docs.cloud.google.com/alloydb/docs/ai/run-hybrid-vector-similarity-search).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
