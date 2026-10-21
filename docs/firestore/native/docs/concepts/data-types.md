---
url: https://docs.cloud.google.com/firestore/native/docs/concepts/data-types/
title: Supported data types \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:29.061831+00:00
---

# Supported data types  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/concepts/data-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supported data types

This page describes the data types that Firestore supports.

## Data types

The following table lists the data types supported by Firestore. It also describes the sort order used when comparing values of the same type:

Data type | Sort order | Notes  
---|---|---  
32-bit integer | Numeric |  32-bit, signed **Note:** Supported only in Enterprise edition.  
64-bit integer | Numeric | 64-bit, signed  
Array | By element values |  In Standard edition databases, an array cannot contain another array value as one of its elements. In Enterprise edition databases, an array can contain an array value as one if its elements. Within an array, elements maintain the position assigned to them. When sorting two or more arrays, arrays are ordered based on their element values. When comparing two arrays, the first elements of each array are compared. If the first elements are equal, then the second elements are compared, continuing until a difference is found. If an array runs out of elements to compare but is equal up to that point, then the shorter array is ordered before the longer array.  For example, `[1, 2, 3] < [1, 2, 3, 1] < [2]`. The array `[2]` has the greatest first element value. The array `[1, 2, 3]` has elements equal to the first three elements of `[1, 2, 3, 1]` but is shorter in length.   
Boolean | `false` < `true` | —  
BSON timestamp | Chronological |  A 64-bit timestamp value comprising Unix seconds and an increment counter. **Note:** Supported only in Enterprise edition.  
Bytes | Byte order | In Standard edition databases, the value must not exceed 1,048,487 bytes (1 MiB - 89 bytes) and only the first 1,500 bytes are considered by queries. In Enterprise edition databases, there is no limit on the size of the value (other than document and index entry size limits) and the full value is considered by queries.  
Bytes with subtype | Byte order (subtype, then value) |  Binary byte sequence with a BSON subtype indicator. **Note:** Supported only in Enterprise edition.  
Date and time | Chronological | When stored in Firestore, precise only to microseconds; any additional precision is rounded down.  
Decimal128 | Numeric |  128-bit decimal floating-point number for high-precision arithmetic. **Note:** Supported only in Enterprise edition.  
Floating-point number | Numeric | 64-bit double precision according to [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754), including (normalized) `NaN` & `+/-Infinity`.  
Geographical point | By latitude, then longitude | To search based on distance, see [Geospatial search](https://docs.cloud.google.com/firestore/native/docs/geospatial-search).  
Map | By keys, then by value | Represents an object embedded within a document. When indexed, you can query on subfields. If you exclude this value from indexing, then all subfields are also excluded from indexing. Key ordering is always sorted. For example, if you write `{c: "foo", a: "bar", b: "qux"}` the map is sorted by key and saved as `{a: "bar", b: "qux", c: "foo"}`.  Map fields are sorted by key and compared by key-value pairs, first comparing the keys and then the values. If the first key-value pairs are equal, the next key-value pairs are compared, continuing until a difference is found. If two maps have all of the same key-value pairs, then map length is considered. For example, the following maps are in ascending order:  `{a: "aaa", b: "baz"}`  
`{a: "foo", b: "bar"}`  
`{a: "foo", b: "bar", c: "qux"}`  
`{a: "foo", b: "baz"}`  
`{b: "aaa", c: "baz"}`  
`{c: "aaa"}`  
  
Max key | None |  Special value that compares higher than all other values. **Note:** Supported only in Enterprise edition.  
Min key | None |  Special value that compares lower than all other values (except null). **Note:** Supported only in Enterprise edition.  
Null | None | —  
ObjectId | Byte order |  A 12-byte object identifier. **Note:** Supported only in Enterprise edition.  
Reference | By path elements (collection, document ID, collection, document ID...) | For example, `projects/[PROJECT_ID]/databases/[DATABASE_ID]/documents/[DOCUMENT_PATH]`.  
Regular expression | By pattern, then by options |  A regular expression pattern and options. **Note:** Supported only in Enterprise edition.  
Text string | UTF-8 encoded byte order | In Standard edition databases, the value must not exceed 1,048,487 bytes (1 MiB - 89 bytes) and only the first 1,500 bytes are considered by queries. In Enterprise edition databases, there is no limit on the size of the value (other than document and index entry size limits) and the full value is considered by queries.  
Vector | By dimension and then by individual element values | The max supported embedding dimension is 2048. To store vectors with larger dimensions, use [dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction).  
  
## Value type ordering

When a query involves a field with values of mixed types, Firestore uses a deterministic ordering based on the internal representations. The following list shows the order:

  1. Null values
  2. Min key values (Enterprise edition only)
  3. Boolean values
  4. 64-bit integer and floating-point values, sorted in numerical order. In Enterprise edition databases, 32-bit integer and Decimal128 values are also included.
  5. Date values
  6. Text string values
  7. Byte values. In Enterprise edition, bytes with subtype values are also included.
  8. Firestore references
  9. ObjectId values (Enterprise edition only)
  10. Geographical point values
  11. Regular Expression (Enterprise edition only)
  12. Array values
  13. Vector embeddings
  14. Map values
  15. Max key values (Enterprise edition only)



## Numeric ordering

Firestore sorts all numeric values (`Integer` & `Floating point`) interleaved with each other. Floating point comparison follows the total ordering of [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) with the notable exception being that Firestore normalizes all `NaN` values, and considers it less than `-Infinity`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
