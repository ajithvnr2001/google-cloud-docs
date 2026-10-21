---
url: https://docs.cloud.google.com/bigquery/docs/vector-index-intro/
title: Introduction to vector indexes \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:18:15.785857+00:00
---

# Introduction to vector indexes  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/vector-index-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to vector indexes

**Note:** This feature may not be available when using reservations that are created with certain BigQuery editions. For more information about which features are enabled in each edition, see [Introduction to BigQuery editions](https://docs.cloud.google.com/bigquery/docs/editions-intro).

A vector index is a data structure designed to let the [`VECTOR_SEARCH` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions#vector_search) and [`AI.SEARCH` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-search) execute more efficiently, especially on large datasets.

## Use cases

Vector indexes improve the efficiency of vector search, which is typically performed on text or multimodal embeddings of your data. BigQuery vector indexes help you perform the following tasks more efficiently:

  * Perform semantic search
  * Detect similar or duplicate images, audio, or videos
  * Perform clustering, targeting, or classification
  * Build recommendation systems
  * Find the top K most similar images or reviews to a given input



For more information, see the [Introduction to vector search](https://docs.cloud.google.com/bigquery/docs/vector-search-intro).

## Pricing

The `CREATE VECTOR INDEX` statement uses [BigQuery compute pricing](https://cloud.google.com/bigquery/pricing#analysis_pricing_models). There is no charge for the processing required to build and refresh your vector indexes as long as the total size of the indexed table data is below your per-organization [limit](https://docs.cloud.google.com/bigquery/quotas#vector_index_maximum_table_size). To support indexing beyond this limit, you must [provide your own reservation](https://docs.cloud.google.com/bigquery/docs/vector-index#use_your_own_reservation) for handling the index management jobs.

Storage is also a consideration for indexes. The amount of bytes stored as an index is subject to [active storage costs](https://cloud.google.com/bigquery/pricing#storage).

  * Vector indexes incur storage costs when they are active.
  * You can find the index storage size by using the [`INFORMATION_SCHEMA.VECTOR_INDEXES` view](https://docs.cloud.google.com/bigquery/docs/information-schema-vector-indexes). If the vector index is not yet at 100% coverage, you are still charged for whatever has been indexed. You can check index coverage by using the `INFORMATION_SCHEMA.VECTOR_INDEXES` view.



## Quotas and limits

For more information, see [Vector index limits](https://docs.cloud.google.com/bigquery/quotas#vector_index_limits).

## What's next

  * Learn more about [creating and managing vector indexes](https://docs.cloud.google.com/bigquery/docs/vector-index).
  * Learn more about [embeddings and vector search](https://docs.cloud.google.com/bigquery/docs/vector-search-intro).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
