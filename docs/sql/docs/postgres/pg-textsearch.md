---
url: https://docs.cloud.google.com/sql/docs/postgres/pg-textsearch/
title: Full-text search using pg_textsearch \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:34.879235+00:00
---

# Full-text search using pg_textsearch  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/pg-textsearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Full-text search using pg_textsearch Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

The [`pg_textsearch`](https://www.tigerdata.com/blog/pg-textsearch-bm25-full-text-search-postgres) extension in Cloud SQL for PostgreSQL provides full-text search using the industry-standard [BM25 (Best Matching 25)](https://en.wikipedia.org/wiki/Okapi_BM25) scoring algorithm to deliver highly accurate relevance scoring. The extension is an [open-source project](https://github.com/timescale/pg_textsearch) available on GitHub.

The `pg_textsearch` extension requires PostgreSQL 17 or later.

Because `pg_textsearch` supports inverse document frequency, term frequency saturation, and document length normalization, it can produce more relevant results than PostgreSQL's built-in `ts_rank` function. Also, because it operates directly on standard PostgreSQL storage pages, you don't have to install an external engine like Elasticsearch, or worry about dual-cluster maintenance and data synchronization. Using `pg_textsearch`, you can build robust, scalable, and highly relevant search experiences without leaving the PostgreSQL ecosystem.

## Different ways to search

There are several options for text searching in Cloud SQL for PostgreSQL:

  * **Exact matching** : With standard SQL search, you use the `LIKE` and `ILIKE` statements to scan for an exact sequence of characters. An example query would be, `ILIKE '%smart fitness watches%'`, which would find instances like:

    * "Explore our new _smart fitness watches_ on sale."
    * "_Smart fitness watches_ make great gifts."

However, it would fail to find:

    * "Runners want a _smart_ waterproof _fitness watch_."
    * "This _watch_ is particularly _smart_ about _fitness_."
  * **Full text search** : Using the BM25 algorithm and `tsvector`, full text search breaks text into root words, ignores filter words, and scores relevance. It understands language rules, including plurals and grammar, and takes into account word frequency. A full text search for `smart AND fitness AND watches` would find the instances that the example exact matching query would miss, and also more complicated instances like these:

    * "A _smart watch_ is perfect for your daily _fitness_ routine."
    * "Not every _watch_ is this _smart_ when it comes to _fitness_."

However, it would fail to find:

    * "An intelligent health-aware _watch_ can help your exercise program."
    * "This intelligent exercise-tracking band is a bargain."
  * **Semantic search** : Using AI models, semantic search converts text into vectors and measures similarity distance. It understands meaning, intent, context, synonyms, and related concepts. A semantic search for `smart fitness watches` would find the example instances that the other search methods would miss. It would understand that an "intelligent health-aware watch" is the same as a "smart fitness watch", and that an "intelligent exercize-tracking band" could also be relevant. It might mistakenly match a pedometer band if it didn't prioritize "watch" sufficiently.




## Install the `pg_textsearch` extension

Take the following steps to install and enable `pg_textsearch`:

  1. Set the [`cloudsql.enable_pg_textsearch`](https://docs.cloud.google.com/sql/docs/postgres/pg-textsearch/) flag to `on` as described in [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags#config). This adds `pg_textsearch` to the `shared_preload_libraries`.

  2. Install the `pg_textsearch` extension
         
         CREATE EXTENSION pg_textsearch;
         

  3. Verify the installation:
         
         SELECT extversion FROM pg_extension WHERE extname = 'pg_textsearch'
         




## Search using `pg_textsearch`

Suppose the following sample table has been filled with data:
    
    
    CREATE TABLE documents (
        doc_id TEXT PRIMARY KEY,
        content TEXT,
        text_embedding vector(3072)
        GENERATED ALWAYS AS (embedding('gemini-embedding-001', content)) STORED 
      );
    

Before using full text search, first create a BM25 index:
    
    
    CREATE INDEX idx_docs_bm25
          ON documents
          USING bm25 (content)
          WITH (text_config = 'english');
    

You can then make a full text search query like this:
    
    
    SELECT doc_id, content, content <@> 'database system'
          AS score FROM documents
          ORDER BY content <@> 'database system'
          ASC LIMIT 5;
    

## Perform hybrid searches using `pg_textsearch` and `vector`

You can use `pg_textsearch` together with the `vector` semantic search extension to perform hybrid searches. Install the `vector` semantic search extension like this:
    
    
    CREATE EXTENSION IF NOT EXISTS vector CASCADE;
    

Make a hybrid semantic and full text search query like this:
    
    
    WITH
      -- Semantic search results
      vector_search AS (
        SELECT doc_id,
          RANK () OVER (ORDER BY text_embedding <=>
                                 google_ml.embedding('gemini-embedding-001',
                                                     'database')::VECTOR ) AS rank
          FROM documents
          ORDER BY text_embedding <=> google_ml.embedding('gemini-embedding-001',
                                                          'database')::VECTOR
        LIMIT 10
      ),
      -- Full text search results
      text_search AS (
        SELECT doc_id,
          RANK () OVER (ORDER BY content <@> 'database' ASC) AS rank
        FROM documents
        ORDER BY content <@> 'database' ASC
        LIMIT 10
      )
      -- RRF combining both semantic and full text search results
      SELECT
        COALESCE(vector_search.doc_id, text_search.doc_id) AS id,
        COALESCE(1.0 / (60 + vector_search.rank), 0.0) +
        COALESCE(1.0 / (60 + text_search.rank), 0.0) AS rrf_score
      FROM vector_search
        FULL OUTER JOIN text_search ON vector_search.doc_id = text_search.doc_id
      ORDER BY rrf_score DESC
      LIMIT 5;
    

## Flags for configuring the `pg_textsearch` extension

Use the following flags to configure `pg_textsearch` full text search:

  * [`pg_textsearch.bulk_load_threshold`](https://github.com/timescale/pg_textsearch): Terms per transaction before auto-spill. Set to 0 to disable. Default: 100,000.
  * [`pg_textsearch.compress_segments`](https://github.com/timescale/pg_textsearch): Compress posting blocks in new segments. Default: `on`.
  * [`pg_textsearch.default_limit`](https://github.com/timescale/pg_textsearch): The maximum number of documents scored when no `LIMIT` clause is present. Default: 1,000.
  * [`pg_textsearch.memtable_pages_threshold`](https://github.com/timescale/pg_textsearch): Number of pages to chain before auto-spill. Set to 0 to disable. Default: 64.
  * [`pg_textsearch.segments_per_level`](https://github.com/timescale/pg_textsearch): Segments per level before automatic compaction occurs. Range: 2-64. Default: 8.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
