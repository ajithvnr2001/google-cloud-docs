---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/debugging_functions/
title: Debugging Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:05.912273+00:00
---

# Debugging Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/debugging_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Debugging Functions Reference

## **Debugging Functions**

Name  | Description   
---|---  
`EXISTS` | Returns `TRUE` if the value is not an absent value   
`IS_ABSENT` | Returns `TRUE` if the value is an absent value   
`IF_ABSENT` | Replaces the value with an expression if it is absent   
`IS_ERROR` | Catches and checks if an error has been thrown by the underlying expression   
`IF_ERROR` | Replaces the value with an expression if it has thrown an error   
`ERROR` | Terminates evaluation and returns an error with the specified message   
  
### EXISTS

**Syntax:**
    
    
    exists(value: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` is not the absent value.

**Examples:**

`value` | `exists(value)`  
---|---  
0L | `TRUE`  
"foo" | `TRUE`  
`NULL` | `TRUE`  
`ABSENT` | `FALSE`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("rating").exists().as("hasRating"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1658-L1661)

### Web

**Example:**
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("rating").exists().as("hasRating"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2935-L2938)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("rating").exists().as("hasRating")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L869-L872)

##### Kotlin  
Android

**Example:**
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("rating").exists().alias("hasRating"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2207-L2210)

##### Java  
Android

**Example:**
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("rating").exists().alias("hasRating"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2453-L2456)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("rating").exists().as_("hasRating"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1126-L1133)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(exists(field("rating")).as("hasRating"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1020-L1026)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.FieldExists(firestore.FieldOf("rating")).As("hasRating"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_logical.go#L28-L33)

### IS_ABSENT

**Syntax:**
    
    
    is_absent(value: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` is the absent value, and `FALSE` otherwise. Absent values are values that are missing from the input, such as a missing document field.

**Examples:**

`value` | `is_absent(value)`  
---|---  
0L | `FALSE`  
"foo" | `FALSE`  
`NULL` | `FALSE`  
`ABSENT` | `TRUE`  
  
### IF_ABSENT

**Syntax:**
    
    
    if_absent(value: ANY, replacement: ANY) -> ANY
    

**Description:**

If `value` is an absent value, evaluates and returns `replacement`. Otherwise returns `value`.

**Examples:**

`value` | `replacement` | `if_absent(value, replacement)`  
---|---|---  
5L | 0L | 5L  
`NULL` | 0L | `NULL`  
`ABSENT` | 0L | 0L  
  
### IS_ERROR

**Syntax:**
    
    
    is_error(try: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if an error is thrown during the evaluation of `try`. Returns `FALSE` otherwise.

### IF_ERROR

**Syntax:**
    
    
    if_error(try: ANY, catch: ANY) -> ANY
    

**Description:**

If an error is thrown during the evaluation of `try`, evaluates and returns `replacement`. Otherwise returns the resolved value of `try`.

### ERROR

**Syntax:**
    
    
    error(message: STRING) -> ANY
    

**Description:**

Evaluation of the `error` function results in the evaluation of the pipeline to terminate with an error. The given `message` is included in the error.

**Examples:**

`cond` | `res` | `switch_on(cond, res, error("no condition matched"))`  
---|---|---  
`TRUE` | 1L | 1L  
`FALSE` | 1L | `ERROR ("no condition matched")`  
  
## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
