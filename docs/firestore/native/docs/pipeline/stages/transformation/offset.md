---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/offset/
title: Offset (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:55.480526+00:00
---

# Offset (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/offset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Offset (Transformation Stage)

## Description

Skips the first `N` input documents.

## Examples

##### Node.js
    
    
    const results = await db.pipeline()
      .collection("cities")
      .offset(10)
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L556-L559)

### Web
    
    
    const results = await execute(db.pipeline()
      .collection("cities")
      .offset(10));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L1847-L1849)

##### Swift
    
    
    let results = try await db.pipeline()
      .collection("cities")
      .offset(10)
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a9512e6e882ad3f5aa32d9d929b77893bc1f1d1e/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1841-L1844)

##### Kotlin  
Android
    
    
    val results = db.pipeline()
        .collection("cities")
        .offset(10)
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L3273-L3276)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> results = db.pipeline()
            .collection("cities")
            .offset(10)
            .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L3575-L3578)

##### Python
    
    
    results = client.pipeline().collection("cities").offset(10).execute()
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L2430-L2430)

##### Java
    
    
    Pipeline.Snapshot results =
        firestore.pipeline().collection("cities").offset(10).execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L2518-L2519)

##### Go
    
    
    snapshot := client.Pipeline().Collection("cities").Offset(10).Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_general.go#L1200-L1200)

## Behavior

The `offset(...)` stage will skip the first `N` input documents. Unless a [`sort(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/sort) stage is used before the offset, the order in which documents are returned is unstable and repeated executions might produce different results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
