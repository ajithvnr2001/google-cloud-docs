---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/limit/
title: Limit (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:37.000136+00:00
---

# Limit (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/limit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Limit (Transformation Stage)

## Description

Limits the number of documents returned by the pipeline.

## Examples

### Web
    
    
    const pipeline = db.pipeline()
      // Step 1: Start a query with collection scope
      .collection("cities")
      // Step 2: Filter the collection
      .where(field("population").greaterThan(100000))
      // Step 3: Sort the remaining documents
      .sort(field("name").ascending())
      // Step 4: Return the top 10. Note applying the limit earlier in the
      // pipeline would have unintentional results.
      .limit(10);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2165-L2174)

##### Swift
    
    
    let pipeline = db.pipeline()
      // Step 1: Start a query with collection scope
      .collection("cities")
      // Step 2: Filter the collection
      .where(Field("population").greaterThan(100000))
      // Step 3: Sort the remaining documents
      .sort([Field("name").ascending()])
      // Step 4: Return the top 10. Note applying the limit earlier in the pipeline would have
      // unintentional results.
      .limit(10)
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L67-L76)

##### Kotlin  
Android
    
    
    val pipeline = db.pipeline()
        // Step 1: Start a query with collection scope
        .collection("cities")
        // Step 2: Filter the collection
        .where(field("population").greaterThan(100000))
        // Step 3: Sort the remaining documents
        .sort(field("name").ascending())
        // Step 4: Return the top 10. Note applying the limit earlier in the pipeline would have
        // unintentional results.
        .limit(10)
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1368-L1377)

##### Java  
Android
    
    
    Pipeline pipeline = db.pipeline()
        // Step 1: Start a query with collection scope
        .collection("cities")
        // Step 2: Filter the collection
        .where(field("population").greaterThan(100000))
        // Step 3: Sort the remaining documents
        .sort(field("name").ascending())
        // Step 4: Return the top 10. Note applying the limit earlier in the pipeline would have
        // unintentional results.
        .limit(10);
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1608-L1617)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    pipeline = (
        client.pipeline()
        .collection("cities")
        .where(Field.of("population").greater_than(100_000))
        .sort(Field.of("name").ascending())
        .limit(10)
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L58-L66)

##### Java
    
    
    Pipeline pipeline =
        firestore
            .pipeline()
            .collection("cities")
            .where(field("population").greaterThan(100_000))
            .sort(ascending(field("name")))
            .limit(10);
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L63-L69)

##### Go
    
    
    pipeline := client.Pipeline().
    	Collection("cities").
    	Where(firestore.FieldOf("population").GreaterThan(100000)).
    	Sort(firestore.Orders(firestore.Ascending(firestore.FieldOf("name")))).
    	Limit(10)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_general.go#L1709-L1713)

## Behavior

The `limit(...)` stage will only return the first `N` documents. Unless a [`sort(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/sort) stage is used before the limit, the order in which documents are returned is unstable and repeated executions may produce different results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
