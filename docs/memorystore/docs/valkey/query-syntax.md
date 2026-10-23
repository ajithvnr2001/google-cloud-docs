---
url: https://docs.cloud.google.com/memorystore/docs/valkey/query-syntax/
title: Query syntax \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:32.712828+00:00
---

# Query syntax  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/query-syntax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Query syntax Stay organized with collections  Save and categorize content based on your preferences. 

Vector queries operate by searching a vector database to find vectors that are best matched to your query vector across the entire cluster. This page provides details about how this works.

## Find similar vectors

Vector search queries use two strategies:

  * K-Nearest Neighbors (KNN): Finds the k closest vectors to your query vector.
  * Approximate Nearest Neighbors (ANN): Finds the approximate k closest vectors to your query vector



To use KNN, indexes should be created with the FLAT vector index type. With KNN, search queries will be exact, but will be slower. To use ANN, indexes should be created with the HNSW vector index type. With ANN, search queries will be approximate, but will be faster. ANN accuracy can be improved by adjusting the HNSW index parameters and the EF_RUNTIME parameter in the query. 

### Query syntax breakdown
    
    
    FT.SEARCH index "(hybrid_filter_expression)=>[KNN num_neighbours @my_vector_hash_key $my_vector_query_param]" PARAMS 2 my_vector_query_param "query_embedding" DIALECT 2
    

  * `index`: The name of the index containing your vector field.

  * `(hybrid_filter_expression)`: This is the hybrid filter expression. Only tag and numeric indexes are supported in filter expressions. See Hybrid queries for more details on filter expressions.

    * `(*)` can be used to perform queries that don't require filtering.
  * `=>`: Separates the filter from the vector search.

  * `[KNN num_neighbours @field $vector]`: The KNN search expression. Replace `num_neighbors` with the chosen number of results and `@field` with your vector field's name.

  * `PARAMS 2 my_vector_query_param "query_embedding"`:

    * The value `2` after `PARAMS` indicates that two additional arguments must be supplied.
    * `my_vector_query_param` is the query parameter vector name, as specified in the KNN search expression.
    * Replace `query_embedding` with your embedded query vector.
  * `DIALECT 2`: Specifies that you're using query dialect version 2 or later (required for vector search).




### Hybrid queries

The initial expression enclosed within the parentheses () is a filter expression. Filter expressions allow you to filter vectors during execution of the vector search. A query that utilizes a filter expression to filter results is called a hybrid query. Any combination of tag and numeric indexes can form a hybrid query.

Memorystore for Valkey uses two approaches for filtering vector searches:

  1. Pre-filtering: Pre-filtering relies on secondary indexes (e.g. tag, numeric) to first find the matches to the filter expression regardless of vector similarity. Once the filtered results are calculated a brute-force search is performed to sort by vector similarity.
  2. Inline-filtering: Inline-filtering performs the vector search algorithm (e.g. HNSW), ignoring found vectors which don't match the filter.



Pre-filtering is faster when the filtered search space is much smaller than the original search space. When the filtered search space is large, inline-filtering becomes faster. Memorystore for Valkey automatically chooses between the two strategies based on the provided filter.

Filter expressions support both tag and numeric indexes.

#### Tag Index

Tags are text fields that are interpreted as a list of tags delimited by a separator character. Generally, tags are small sets of values with finite possible values like color, book genre, city name, or author.

  * Only indexed fields can be used as a tag filter.
  * TAG fields are tokenized by a separator character, which is a comma "," by default but configurable during index creation.
  * No stemming is performed while indexing a tag field.
  * Only prefix, exact pre filters can be performed on a tag field. Suffix, infix queries are not supported.
  * By default, tags are case insensitive. For example, "Blue" and "BLUE" both will be indexed as "blue" and will yield the same result in a hybrid query.
  * Empty strings are neither indexed or queried.
  * During indexing and querying, any trailing whitespace is removed.



##### Syntax

Here `{` and `}` are part of syntax and `|` is used as a OR operator to support multiple tags:
    
    
    @:{  |  | ...}
    

For example, the following query will return documents with blue OR black OR green color. 
    
    
    @color:{blue | black | green}
    

As another example, the following query will return documents containing "hello world" or "hello universe"
    
    
    @color:{hello world | hello universe}
    

#### Numeric Index

Numeric indexes allow for filtering queries to only return values that are in between a given start and end value.

  * Both inclusive and exclusive queries are supported.
  * For open ended queries, +inf, -inf can be used to express start and end ranges.



As an example, the following query will return books published between 2021 and 2024 (Both inclusive). The equivalent mathematical expression is `2021 <= year <= 2024`.
    
    
    "@year:[2021 2024]"
    

The following query will return books published between 2021 (exclusive) and 2024 (inclusive). The equivalent mathematical expression is `2021 < year <= 2024`.
    
    
    @year:[(2021 2024]
    

The following query will return books published before 2024 (inclusive). The equivalent mathematical expression is `year <= 2024`.
    
    
    @year:[(-inf 2024]
    

The following query will return books published after 2015 (exclusive). The equivalent mathematical expression is `year >= 2015`.
    
    
    @year:[2015 +inf]
    

Use the following table as a guide for mapping mathematical expressions to prefiltering queries:

Mathematical expression | Filter expression  
---|---  
min <= field <= max | @field:[min max]  
min < field <= max | @field:[(min max]  
min <= field < max | @field:[min (max]  
min < field < max | @field:[(min (max]  
field => min | @field:[min +inf]  
field > min | @field:[(min +inf]  
field <= max | @field:[-inf max]  
field < max | @field:[-inf (max]  
field == val | @field:[val val]  
  
#### Logical Operators

Multiple tags and numeric fields can be used to construct complex queries using logical operators.

##### Logical AND

To set a logical AND, use a space between the predicates. For example:
    
    
    query1 query2 query3
    

##### Logical OR

To set a logical OR, use the '|' character between the predicates. For example:
    
    
    query1 | query2 | query3
    

##### Logical Negation

Any query can be negated by prepending `-` before each query. Negative queries return all entries that don't match the query. This also includes documents that don't have the field.

For example, a negative query on `@genre:{comedy}` will return all books that are not comedy AND all books that don't have a genre field.

The following query will return all books with "comedy" genre that are not published between 2015 and 2024, or that have no year field:
    
    
    @genre:[comedy] -@year:[2015 2024]
    

##### Examples of Combining Logical Operators

Logical operators can be combined to form complex filter expressions.

The following query will return all books with "comedy" or "horror" genre (AND) published between 2015 and 2024:
    
    
    @genre:[comedy|horror] @year:[2015 2024]
    

The following query will return all books with "comedy" or "horror" genre (OR) published between 2015 and 2024:
    
    
    @genre:[comedy|horror] | @year:[2015 2024]
    

The following query will return all books that either don't have a genre field, or have a genre field not equal to "comedy", that are published between 2015 and 2024:
    
    
    -@genre:[comedy] @year:[2015 2024]
    

Refer to [FT.SEARCH](https://docs.cloud.google.com/memorystore/docs/valkey/ftsearch) info for usage.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
