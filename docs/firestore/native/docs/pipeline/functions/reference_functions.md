---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/reference_functions/
title: Reference Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:21.403247+00:00
---

# Reference Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/reference_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Reference Functions Reference

## **Reference Functions**

The `REFERENCE` type acts as a "pointer" to other documents in the database (or even other databases). The following functions allow manipulating this type during query execution.

Name  | Description   
---|---  
`COLLECTION_ID` | Returns the ID of the leaf collection in the given reference   
`DOCUMENT_ID` | Returns the ID of the document in the given reference   
`PARENT` | Returns the parent reference   
`REFERENCE_SLICE` | Returns a subset of segments from the given reference   
  
### COLLECTION_ID

**Syntax:**
    
    
    collection_id(ref: REFERENCE) -> STRING
    

**Description:**

Returns the leaf collection ID of the given `REFERENCE`.

**Examples:**

`ref` | `collection_id(ref)`  
---|---  
`users/user1` | `"users"`  
`users/user1/posts/post1` | `"posts"`  
  
### DOCUMENT_ID

**Syntax:**
    
    
    document_id(ref: REFERENCE) -> ANY
    

**Description:**

Returns the document ID of the given `REFERENCE`.

**Examples:**

`ref` | `document_id(ref)`  
---|---  
`users/user1` | `"user1"`  
`users/user1/posts/post1` | `"post1"`  
  
### PARENT

**Syntax:**
    
    
    parent(ref: REFERENCE) -> REFERENCE
    

**Description:**

Returns the parent `REFERENCE` of the given reference, or `NULL` if the ref is a root reference already.

**Examples:**

`ref` | `parent(ref)`  
---|---  
`/` | `NULL`  
`users/user1` | `/`  
`users/user1/posts/post1` | `users/user1`  
  
### REFERENCE_SLICE

**Syntax:**
    
    
    reference_slice(ref: REFERENCE, offset: INT, length: INT) -> REFERENCE
    

**Description:**

A `REFERENCE` is a list of `(collection_id, document_id)` tuples and this allows getting a view of that list, just like `array_slice(...)`.

Returns a new `REFERENCE` that is a subset of the segments of the given `ref`.

  * `offset`: The starting index (0-based) of the slice. If negative, it is an offset from the end of the reference.
  * `length`: The number of segments to include in the slice.



**Examples:**

`ref` | `offset` | `length` | `reference_slice(ref, offset, length)`  
---|---|---|---  
`a/1/b/2/c/3` | 1L | 2L | `b/2/c/3`  
`a/1/b/2/c/3` | 0L | 2L | `a/1/b/2`  
`a/1/b/2/c/3` | -2L | 2L | `c/3`  
  
## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
