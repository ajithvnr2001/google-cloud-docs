---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/filtered-vector-search-overview/
title: Filtered vector search in AlloyDB Omni overview \u00a0|\u00a0 AlloyDB Omni using containers: 15.17.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:33:24.923653+00:00
---

# Filtered vector search in AlloyDB Omni overview  |  AlloyDB Omni using containers: 15.17.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/filtered-vector-search-overview/

This page documents AlloyDB Omni version **15.17.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/overview)



Send feedback 

#  Filtered vector search in AlloyDB Omni overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.17.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/filtered-vector-search-overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/filtered-vector-search-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/filtered-vector-search-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/filtered-vector-search-overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/filtered-vector-search-overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/filtered-vector-search-overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/filtered-vector-search-overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/filtered-vector-search-overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/filtered-vector-search-overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/filtered-vector-search-overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/filtered-vector-search-overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/filtered-vector-search-overview)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/filtered-vector-search-overview)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/filtered-vector-search-overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/filtered-vector-search-overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/filtered-vector-search-overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/filtered-vector-search-overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/filtered-vector-search-overview)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/filtered-vector-search-overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/filtered-vector-search-overview)

This page gives an overview of filtered vector search in AlloyDB Omni. 

A _filtered vector search_ consists of a query vector and a filter for a specific field. AlloyDB Omni uses PostgreSQL's rich querying capabilities, allowing you to perform vector search and query both structured and unstructured data from a single SQL interface.

## Filtering options

The AlloyDB Omni query optimizer plays a crucial role in determining the most efficient filtering strategy for your vector search.

To estimate the cost of different execution plans, the query optimizer analyzes your query and considers factors like filter selectivity, data distribution, and index availability.

Based on the cost estimation, the optimizer chooses an optimal filtering strategy from the following:

  * pre-filtering
  * post-filtering
  * inline filtering

**Note:** Inline filtering is supported when using the ScaNN algorithm only. Inline filtering is not compatible with the Inverted File (IVF), Inverted File Flat (IVFFlat), or Hierarchical Navigable Small Worlds (HNSW) algorithms.

### Pre-filtering

Pre-filtering is a query optimization strategy where AlloyDB Omni uses your filters to find a smaller group of items that match your criteria instead of searching through the entire dataset. Then, AlloyDB Omni runs the vector search on that smaller group.

For example, if you're looking for similar blue shirts, AlloyDB Omni first finds all the blue shirts and then searches for similar items within that group.

This strategy improves performance because it runs the computationally intensive vector similarity search on a reduced dataset.

### Post-filtering

Post-filtering is a strategy that AlloyDB Omni uses when your filters don't narrow down the results considerably. Instead of filtering first, AlloyDB Omni starts by finding a broad list of similar items based on your vector search. Then, it checks the results against your filter conditions to generate the final list.

For example, if you search for similar movies and you have a very broad filter like `genre = drama`, AlloyDB Omni first finds a large set of movies that are similar to your search and then filters them by genre since most movies might be dramas.

This strategy is efficient when you expect many results to match your filter.

### Inline filtering

Inline filtering is a query optimization strategy where AlloyDB Omni uses both vector and other secondary indexes to perform vector search and filter evaluation in tandem. AlloyDB Omni searches through the vector index to find similar vectors and also checks if each vector matches your metadata filter conditions, leveraging indexes such as B-trees, GIN, or GiST for quick evaluation of these conditions.

For example, if you search for similar shoes and you filter by `color = black`, inline filtering means AlloyDB Omni only checks the similarity of shoes that are already black. This is more efficient than checking the similarity of all shoes and then filtering by color, or filtering all shoes by color and then checking similarity.

Inline filtering excels when filters narrow down results moderately.

## Understand query plans

A query plan provides a comprehensive view of the query execution process and shows which filtering strategy AlloyDB Omni chooses for the vector scan operation in the **Execution Strategy** field.

### A query plan for inline filtering

For inline filtering, AlloyDB Omni uses a Custom Scan plan node, also known as vector scan, that relies on a Bitmap Index Scan plan node to provide the bitmap for the filter clauses.

The vector scan computes distances only for rows that satisfy the filter criteria.

The following query demonstrates inline filtering for a `shoes` search filtered by `color = black`
    
    
    EXPLAIN
    SELECT *
    FROM products
    WHERE color = 'black'
    ORDER BY embedding <=> embedding('text-embedding-005', 'shoes')::vector
    LIMIT 10;
    

The following example query plan illustrates an optimized vector search using inline filtering:
    
    
    Limit (actual rows=10)
      ->  Custom Scan (vector scan) on products
          Execution Strategy: Bitmap assisted vector Scan on products_embedding_index
          Order By: (embedding <=> '[...]')::vector)
          Limit: 10
          ->  Bitmap Index Scan on products (color_index)
              Index Cond: (color = 'black')
    

In the example query plan, `Limit (actual rows=10)` shows that the query used the SQL `LIMIT 10;` clause to restrict the output. `actual rows=10` means this node returned 10 rows during query execution.

The `-> Custom Scan (vector scan) on products` node represents a vector search operation. It is a Custom Scan because it's a special scan for vector data, and it operates on the `products` table. The example query plan for inline filtering shows `Bitmap assisted vector Scan on products_embedding_index` in the **Execution Strategy** field, which indicates that the vector scan uses the bitmap to create a shortlist of rows on which similarity search needs to be performed. The bitmap index scan is used to filter the data based on the `color = 'black'` condition.

The `Order By: (embedding <=> '[...]')::vector` attribute indicates that the results are ordered based on vector similarity, calculated using the expression `(embedding <=> '[...]')::vector`, where `embedding` refers to the vector column, `<=>` represents the nearest neighbor operator, `[...]` is the query vector, and `::vector` performs type casting to the vector data type.

The `-> Bitmap Index Scan on products (color_index)` node represents a bitmap index scan on the `colors_index`. A bitmap index scan selects rows matching the filter condition using a bitmap, and uses the `color_index` for filtering.

The `Index Cond: (color = 'black')` attribute specifies the filter condition used by the `color = 'black'` index scan from the query's `WHERE` clause.

## Best practices for filtered vector search

Regardless of the vector index type you use (ScaNN, HNSW, or IVFFlat), if your vector search queries include filters, we recommend creating a [B-tree index](https://www.postgresql.org/docs/15/indexes-types.html#indexes-type-btree) on the columns used in your query filters. This helps the query planner to quickly evaluate the filter conditions and select the most efficient execution strategy such as pre-filtering, post-filtering, or inline filtering, which can significantly reduce query execution time.

## What's next

  * [Adaptive filtering in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/adaptive-filtering)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
