---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/full-text-search-overview/
title: Full-text search overview \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:11:46.745574+00:00
---

# Full-text search overview  |  AlloyDB Omni using the container orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/full-text-search-overview/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)



Send feedback 

#  Full-text search overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/full-text-search-overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/full-text-search-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/full-text-search-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/full-text-search-overview)

Full-text search (FTS) lets you identify natural-language documents that satisfy a query. This approach is more effective than standard string matching because it accounts for linguistic nuances, such as ignoring common words like "the" and matching different forms of a word, such as "run", "running", or "ran". 

AlloyDB Omni supports all full-text-search features and capabilities, including support for GIN and GiST indexes.

## Core concepts of full-text search

To effectively implement full-text search (FTS), you should understand how PostgreSQL processes and searches text. The unit of search, a _document_ , is typically a text column or a combination of columns from a row. The index build process parses this document to associate words (or _lexemes_ , the base form of a word) with the row.

This process involves a preprocessing pipeline that transforms raw text into a searchable format by:

  * Breaking text into tokens.
  * Removing common stop words.
  * Normalizing words to their root form; for example, "run" is the lexeme for "run," "runs," "running," and "ran."



Using full-text search also requires that you learn about specialized data types, operators, and various indexing strategies, including built-in PostgreSQL indexes and the high-performance [RUM](https://github.com/postgrespro/rum) indexes.

PostgreSQL uses two primary data types and a match operator to manage FTS:

  * `tsvector`: Represents a document in a searchable format—as a sorted list of distinct lexemes.
  * `tsquery`: Represents search terms, including boolean operators that let you combine lexemes.
  * `@@`: Checks if a `tsvector` matches a `tsquery`, allowing for linguistically-aware searches.



AlloyDB Omni supports all index types for full-text search that built-in PostgreSQL supports. The choice of index depends on the balance between search speed, index build time, update speed, and the specific search functionalities required, such as phrase searching or relevance ranking.

For more information about how to create and use RUM indexes in AlloyDB Omni, see [Create and manage a RUM index in AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/ai/create-rum-index).

## Combine full-text and semantic search

The most powerful search implementations often combine full-text search using RUM indexes and vector search. Use hybrid search to merge the strengths of semantic understanding and exact keyword matching, merging the distinct result sets for a comprehensive ranking.

For example, in an ecommerce application, you could first use full-text search with RUM to find products containing specific keywords like "running shoes" and use vector search to find results based on semantic similarity to a user's more detailed query, such as "comfortable footwear for long-distance training." The database then fuses the ranked results from both search components into a single, unified list using the Reciprocal Rank Fusion (RRF) algorithm to produce a final ranking. For more information about using this hybrid approach, see [Run a hybrid vector similarity search](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/run-hybrid-vector-similarity-search). 

## What's next

  * Learn how to [Create and manage a RUM index in AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/ai/create-rum-index). 
  * Learn how to [Run a hybrid vector similarity search](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/run-hybrid-vector-similarity-search). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
