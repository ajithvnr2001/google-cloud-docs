---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/collection/
title: Collection (Input Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:34.976875+00:00
---

# Collection (Input Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collection (Input Stage)

## Description

Returns all documents from a given collection. The collection can be nested.

## Examples

### Web
    
    
    const results = await execute(db.pipeline()
      .collection("users/bob/games")
      .sort(field("name").ascending())
      );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2396-L2399)

##### Swift
    
    
    let results = try await db.pipeline()
      .collection("users/bob/games")
      .sort([Field("name").ascending()])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L290-L293)

##### Kotlin  
Android
    
    
    val results = db.pipeline()
        .collection("users/bob/games")
        .sort(field("name").ascending())
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1612-L1615)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> results = db.pipeline()
        .collection("users/bob/games")
        .sort(field("name").ascending())
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1858-L1861)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    results = (
        client.pipeline()
        .collection("users/bob/games")
        .sort(Field.of("name").ascending())
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L336-L343)

##### Java
    
    
    Pipeline.Snapshot results =
        firestore
            .pipeline()
            .collection("users/bob/games")
            .sort(ascending(field("name")))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L333-L339)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("users/bob/games").
    	Sort(firestore.Orders(firestore.Ascending(firestore.FieldOf("name")))).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_general.go#L877-L880)

## Behavior

In order to use the `collection(...)` stage, it must appear as the first stage in the pipeline (or sub-pipeline).

The order of documents returned from the `collection(...)` stage is unstable and cannot be relied upon. Firestore will attempt to execute the query in the most efficient way possible, which can change the order depending on the schema or index configuration. A subsequent [`sort(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/sort) stage can be used to obtain a deterministic ordering.

For example, for the following documents:

### Node.js
    
    
    await db.collection("cities").doc("SF").set({name: "San Francsico", state: "California"});
    await db.collection("cities").doc("NYC").set({name: "New York City", state: "New York"});
    await db.collection("cities").doc("CHI").set({name: "Chicago", state: "Illinois"});
    await db.collection("states").doc("CA").set({name: "California"});
    

The `collection` stage can be used to retrieve all cities in the `cities` collection and then sort them in ascending order of name.

### Node.js
    
    
    const results = await db.pipeline()
      .collection("/cities")
      .sort(field("name").ascending())
      .execute();
    

This query produces the following documents:
    
    
      { name: "Chicago", state: "Illinois" }
      { name: "New York City", state: "New York" }
      { name: "San Francisco", state: "California" }
    

### Subcollections

The `collection(...)` stage can also be used to target collections under a specific parent by providing the full path to the stage.

For example, for the following documents:

### Node.js
    
    
    await db.collection("cities/SF/departments").doc("building").set({name: "SF Building Deparment", employees: 750});
    await db.collection("cities/NY/departments").doc("building").set({name: "NY Building Deparment", employees: 1000});
    await db.collection("cities/CHI/departments").doc("building").set({name: "CHI Building Deparment", employees: 900});
    await db.collection("cities/NY/departments").doc("finance").set({name: "NY Finance Deparment", employees: 1200});
    

For this example, we only want the departments of New York city.

### Node.js
    
    
    const results = await db.pipeline()
      .collection("/cities/NY/departments")
      .sort(field("employees").ascending())
      .execute();
    

This will return all departments under the full path `cities/NY/departments`.
    
    
      { name: "NY Building Deparment", employees: 1000 }
      { name: "NY Finance Deparment", employees: 1200 }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
