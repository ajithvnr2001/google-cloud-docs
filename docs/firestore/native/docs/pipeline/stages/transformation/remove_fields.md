---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/remove_fields/
title: Remove Fields (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:37.237965+00:00
---

# Remove Fields (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/remove_fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Remove Fields (Transformation Stage)

## Description

Remove fields from the documents produced by the previous stage.

The generated documents will contain all fields from the previous stage except for the fields specified to be removed.

## Examples

##### Node.js
    
    
    const results = await db.pipeline()
      .collection("cities")
      .removeFields("population", "location.state")
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L458-L461)

### Web
    
    
    const results = await execute(db.pipeline()
      .collection("cities")
      .removeFields("population", "location.state"));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L1755-L1757)

##### Swift
    
    
    let results = try await db.pipeline()
      .collection("cities")
      .removeFields(["population", "location.state"])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a9512e6e882ad3f5aa32d9d929b77893bc1f1d1e/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1742-L1745)

##### Kotlin  
Android
    
    
    val results = db.pipeline()
        .collection("cities")
        .removeFields("population", "location.state")
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L3173-L3176)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> results = db.pipeline()
            .collection("cities")
            .removeFields("population", "location.state")
            .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L3464-L3467)

##### Python
    
    
    results = (
        client.pipeline()
        .collection("cities")
        .remove_fields("population", "location.state")
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L2307-L2312)

##### Java
    
    
    Pipeline.Snapshot results =
        firestore
            .pipeline()
            .collection("cities")
            .removeFields("population", "location.state")
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L2362-L2368)

##### Go
    
    
    snapshot := client.Pipeline().Collection("cities").
    	RemoveFields(firestore.Fields("population", "location.state")).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_general.go#L657-L659)

## Behavior

### Remove Nested Fields

The `remove_fields(...)` stage respects nested field syntax, and will remove keys from a map.

For example, to remove the nested state field from the dataset:

### Node.js
    
    
    await db.collection("cities").doc("SF").set({name: "San Francisco", location: {country: "USA", state: "California"}});
    await db.collection("cities").doc("TO").set({name: "Toronto", location: {country: "Canada", province: "Ontario"}});
    

The following pipeline can be used:

### Node.js
    
    
    const results = await db.pipeline()
      .collection("/cities")
      .removeFields("location.state")
      .execute();
    

Which produces the following documents:
    
    
    { name: "San Francisco", location: { country: "USA" } }
    { name: "Toronto", location: { country: "Canada", province: "Ontario" } }
    

Removal of elements within an array is unsupported.

### Remove on Non-Existent Fields

If a nested or top-level field given to `remove_fields(...)` does not exist in a document, the stage won't edit the document for that field. Other existing fields will still be removed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
